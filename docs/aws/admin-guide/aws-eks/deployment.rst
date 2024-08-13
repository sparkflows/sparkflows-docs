Deployment
===========
Below are the steps to deploy Fire Insights AWS Elastic Kubernetes Service (EKS).

Step 1 : Create Deployment Service
---------------------------------------

Create deployment/service using kubectl. Update image url of deploy.yaml file accordingly.

  .. code-block:: YAML

    apiVersion: v1
    kind: Service
    metadata:
      name: fire
    spec:
      type: LoadBalancer
      ports:
        - port: 8080
          targetPort: 8080
      selector:
        app: fire
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: fire
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
            - image: sparkflows/fire:py_3.3.1_3.2.53-rc81
              env:
                - name: KEYSTORE_PASSWORD
                  value: "12345678"
              name: fire
              resources:
                limits:
                  memory: "3Gi"
                requests:
                  memory: "1Gi"
              ports:
                - containerPort: 8080
                  name: fire

The above yaml file creates a service and deployment for Sparkflows.

    .. code-block:: bash

        kubectl apply -f deploy.yaml


Step 2 : Check Deployment
-------------------
On successful deployment, check the status of the pods and services using the following commands:

    .. code-block:: bash

        kubectl get pods
        kubectl get svc


Step 3 : Access Sparkflows
-------------------
Use the external IP of the service to access Sparkflows. The external IP can be found using the following command:

    .. code-block:: bash

        kubectl get svc fire

You can now use the **<external-IP>:targetPort** to access Sparkflows in the browser.

  .. note::  Two user accounts come preconfigured with Sparkflows.
            
             * admin/admin
             * test/test
             
             You may change these usernames and passwords in Fire.
