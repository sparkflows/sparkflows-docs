Install Hive Metastore
=============

Below are the steps for installing Hive Metastore:

- Create a file, **hive-secrets.yaml**, that will store the secrets that will be used to create database credentials and connect with MinIO object storage for creation and management of tables. The credentials description are as follows:

  - **HIVE_METASTORE_USER:** Username for connecting to the MySQL server.
  - **HIVE_METASTORE_PASSWORD:** Password for connecting to the MYSQL Server.
  - **S3_ACCESS_KEY:** Access key for connecting to the MinIO tenant.
  - **S3_SECRET_KEY:** Secret Access key for connecting to the MinIO Tenant.
  
  .. code-block:: yml

   apiVersion: v1
   kind: Secret
   metadata:
     name: hive-credentials
     namespace: demo
   type: Opaque
   data:
     HIVE_METASTORE_USER: c3BhcmtmbG93cwo=
     HIVE_METASTORE_PASSWORD: cGFzc3dvcmQK
     S3_ACCESS_KEY: RWJjN3JQaXhzbHlOTXprYgo=
     S3_SECRET_KEY: TEJUSkN3OGltSlRFOHlHZkFiNkJhN2J3cHJ2YjZpRGMK


- Create a file **hive-deployment.yaml**, that will install hive metastore service with MinIO integration. The environment variables are required to connect to the MinIO tenant from the hive metastore service.

  .. code-block:: yml

   apiVersion: v1
   kind: Service
   metadata:
     name: metastore
     namespace: demo
   spec:
     ports:
       - port: 9083
     selector:
       app: metastore
     clusterIP: None
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: metastore
     namespace: demo
   spec:
     selector:
       matchLabels:
         app: metastore
     strategy:
       type: Recreate
     template:
       metadata:
         labels:
           app: metastore
       spec:
         containers:
           - image: sparkflows/hive-metastore:3.1.2
             name: metastore
             resources:
               limits:
                 memory: "2Gi"
               requests:
                 memory: "1Gi"
             env:
               - name: HIVE_METASTORE_JDBC_URL
                 value: jdbc:mysql://mysql.demo.svc.cluster.local:3306/objectmetastore?createDatabaseIfNotExist=true
               - name: HIVE_METASTORE_DRIVER
                 value: com.mysql.cj.jdbc.Driver
               - name: S3_ENDPOINT
                 value: https://minio.demo.svc.cluster.local
               - name: S3_PATH_STYLE_ACCESS
                 value: "true"
               - name: HIVE_METASTORE_USER
                 valueFrom:
                   secretKeyRef:
                     name: hive-credentials
                     key: HIVE_METASTORE_USER
               - name: HIVE_METASTORE_PASSWORD
                 valueFrom:
                   secretKeyRef:
                     name: hive-credentials
                     key: HIVE_METASTORE_PASSWORD
               - name: S3_ACCESS_KEY
                 valueFrom:
                   secretKeyRef:
                     name: hive-credentials
                     key: S3_ACCESS_KEY
               - name: S3_SECRET_KEY
                 valueFrom:
                   secretKeyRef:
                     name: hive-credentials
                     key: S3_SECRET_KEY
             ports:
               - containerPort: 9083
                 name: metastore
   
   
- To verify the deployment of the Hive metastore, check the pod status::
   
   $ kubectl get pod -n demo
   metastore-d7bb7658-x5rtv                        1/1     Running            0          2d22h
     
-  Check logs of the pod for further verification of Metastore::

   $ kubectl logs -f pod/metastore-d7bb7658-x5rtv -n demo
   
   .. code-block:: bash
   
      2021-10-01T05:29:10,220  INFO [main] metastore.HiveMetaStore: Added admin role in metastore
      2021-10-01T05:29:10,228  INFO [main] metastore.HiveMetaStore: Added public role in metastore
      2021-10-01T05:29:10,266  INFO [main] metastore.HiveMetaStore: No user is added in admin role, since config is empty
      2021-10-01T05:29:10,333  INFO [main] conf.HiveConf: Found configuration file file:/opt/hive/conf/hive-site.xml
      2021-10-01T05:29:10,576  INFO [main] metastore.HiveMetaStore: Starting DB backed MetaStore Server with SetUGI enabled
      2021-10-01T05:29:10,583  INFO [main] metastore.HiveMetaStore: Started the new metaserver on port [9083]...
      2021-10-01T05:29:10,583  INFO [main] metastore.HiveMetaStore: Options.minWorkerThreads = 200
      2021-10-01T05:29:10,583  INFO [main] metastore.HiveMetaStore: Options.maxWorkerThreads = 1000
      2021-10-01T05:29:10,583  INFO [main] metastore.HiveMetaStore: TCP keepalive = true
      2021-10-01T05:29:10,583  INFO [main] metastore.HiveMetaStore: Enable SSL = false

