Deployment
===========
Below are the steps to deploy Fire Insights AWS Elastic Kubernetes Service (EKS).

Step 1 : Create Deployment Service
---------------------------------------

Create deployment/service using kubectl. Update image url of deployment.yaml file accordingly. 

.. code-block:: YAML

    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: fire-pv
    spec:
     capacity:
       storage: 5Gi
    accessModes:
      - ReadWriteOnce
    persistentVolumeReclaimPolicy: Retain
    storageClassName: standard
    hostPath:
      path: /data/fire
    
.. code-block:: YAML


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
              image: "sparkflows/fire:py_3.2.1_3.2.81-rc11"
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

.. code-block:: YAML

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


The above yaml file creates a service and deployment for Sparkflows with resource limit of 16GB ram and 1vCPU. You can configure the resources limit, as per your requirement. This will also mount the /root directory to the persistent volume which will make sure that the H2 database persists across restart of the pod.

    .. code-block:: bash

        kubectl apply -f deployment.yaml


Step 2 : Check Deployment
-------------------
On successful deployment, check the status of the pods and services using the following commands:

    .. code-block:: bash

        kubectl get po -A | grep sparkflows-app

Step 3 : Access Sparkflows
-------------------
Use the external IP of the service to access Sparkflows. The external IP can be found using the following command:

    .. code-block:: bash

        kubectl get svc sparkflows-app

You can now use the **<external-IP>:targetPort** to access Sparkflows in the browser.

  .. note::  Two user accounts come preconfigured with Sparkflows.
            
             * admin/admin
             * test/test
             
             You may change these usernames and passwords in Fire.
