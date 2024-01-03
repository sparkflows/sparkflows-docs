Install Fire Insights
--------------

Below are the steps for installing Fire Insights.

- In this setup, we will be using MySQL as the database for Fire insights server. Assuming MySQL is running in the namespace **demo**, create an interactive shell using the below command::
  
   kubectl run -it --rm --image=mysql:8.0 --restart=Never mysql-client -- mysql -h mysql.demo.svc.cluster.local -p<root_password>
  
- Initialize the database and user for interacting with that database: 

  ::
   
   create database firedb;
   CREATE user 'fire'@'%' IDENTIFIED BY 'fire';
   GRANT ALL PRIVILEGES ON firedb.* TO 'fire'@'%' WITH GRANT OPTION;
   
- Create **fire-deployment.yaml** with the following configuration deploy **Fire Insights** on kubernetes:

  .. code-block:: yml

    apiVersion: v1
    kind: Service
    metadata:
      name: fire
      namespace: demo
    spec:
      type: NodePort
      ports:
        - port: 8080
      selector:
        app: fire
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: fire
      namespace: demo
    spec:
      selector:
        matchLabels:
          app: fire
      strategy:
        type: Recreate
      template:
        metadata:
          labels:
            app: fire
        spec:
          containers:
            - image: sparkflows/k8s-fire:3.1.0
              name: fire
              resources:
                limits:
                  memory: "3Gi"
                requests:
                  memory: "1Gi"
              ports:
                - containerPort: 8080
                  name: fire
                  
- Fetch the node where the service was deployed::

   kubectl get pods -n demo --selector="app=fire" --output=wide
   NAME                    READY   STATUS    RESTARTS   AGE   IP           NODE     NOMINATED NODE   READINESS GATES
   fire-5dc7cc9d88-q5szw   1/1     Running   0          44m   10.42.0.55   n1.k8s   <none>           <none>
   
- Get the port of the node, where the service is exposed::

   kubectl get svc -n demo
   NAME                                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
   fire                                      NodePort       10.43.87.85     <none>        8080:30318/TCP               45m

- Get the public IP of the node **n1.k8s** and access the Fire insights web console at http://<public-ip-node>:30318

- You can setup custom load balancer to access the above service.
