Deployment
===========
Below are the steps to deploy Fire Insights AWS Elastic Kubernetes Service (EKS).

Step 1 : Create a Persistent Volume
---------------------------------------
The following configuration will create a persistent volume which is backed by the host path, managed by kubernetes. The size we have set it up is 10GB. This storage will be mounted on the Sparkflows container, at the path where the H2 database is being stored.  

.. code-block:: YAML

    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: fire-pv
    spec:
     capacity:
       storage: 10Gi
    accessModes:
      - ReadWriteOnce
    persistentVolumeReclaimPolicy: Retain
    storageClassName: standard
    hostPath:
      path: /data/fire

    ---

    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
    name: fire-pvc
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 5Gi
      storageClassName: standard

Use the below command to create the persistent volume and claim

.. code-block:: bash

      kubectl apply -f pv.yaml



Step 2: Create Sparkflows Service/Deployment
---------------------------------------------
Create deployment/service using kubectl. Update image url of deployment.yaml file as per the latest version available. The below yaml file creates a service and deployment for Sparkflows with resource limit of 16GB ram and 1vCPU. You can configure the resources limit, as per your requirement.

.. code-block:: YAML

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: sparkflows-app
      labels:
        app: sparkflows-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: sparkflows-app
      template:
        metadata:
          labels:
            app: sparkflows-app
        spec:
          serviceAccountName: default
          volumes:
            - name: sparkflows-vol
              persistentVolumeClaim:
                claimName: fire-pvc
          containers:
            - name: sparkflows-fire
              image: "sparkflows/fire:py_3.2.1_3.2.81-rc1"
              imagePullPolicy: IfNotPresent
              resources:
                limits:
                  cpu: "1"
                  memory: "16Gi"
                requests:
                  cpu: "0.5"
                  memory: "8Gi"
              volumeMounts:
                - name: sparkflows-vol
                  mountPath: /root
              env:
                - name: KEYSTORE_PASSWORD
                  value: "12345678"

              ports:
                - name: http
                  containerPort: 8080
                  protocol: TCP
              livenessProbe:
                httpGet:
                  path: /
                  port: 8080
                initialDelaySeconds: 80
                periodSeconds: 20
              readinessProbe:
                httpGet:
                  path: /
                  port: 8080

    ---

    apiVersion: v1
    kind: Service
    metadata:
      name: sparkflows-app
      labels:
        app: sparkflows-app
    spec:
      type: LoadBalancer
      ports:
        - port: 8080
          targetPort: http
          protocol: TCP
          name: http
      selector:
        app: sparkflows-app



.. note::  Update Sparkflows Image based on release, which would be shared by Sparkflows.

    .. code-block:: bash

        kubectl apply -f deployment.yaml


Step 3 : Check Deployment
-------------------
On successful deployment, check the status of the pods and services using the following commands:

    .. code-block:: bash

        kubectl get po -A | grep sparkflows-app

Step 4 : Access Sparkflows
-------------------
Use the external IP of the service to access Sparkflows. The external IP can be found using the following command:

    .. code-block:: bash

        kubectl get svc sparkflows-app

You can now use the **<external-IP>:targetPort** to access Sparkflows in the browser.

  .. note::  Two user accounts come preconfigured with Sparkflows, also make sure to update ``app.postMessageURL`` as per Sparkflows absolute URL running and should be accessible.
            
             * admin/admin
             * test/test
             
             You may change these usernames and passwords in Fire.

Step 5 : Update/Upgrade Sparkflows
-------------------
In order to update any configuration in the deployment.yaml, like image version or container resources limits/requests you need to first delete the current deployment using the below command.

.. code-block:: bash

        kubectl delete -f deployment.yaml

Once you've deleted the deployment, re-create the service. We need to do this, because two instances can't use the same H2 database as it's a file based DB.

.. code-block:: bash

        kubectl apply -f deployment.yaml

