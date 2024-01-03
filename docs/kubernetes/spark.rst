Install Spark
--------------

Below are the steps for installing Apache Spark operator and History Server:

.. note:: We will be leveraging KUDO plugin to install and upgrade Spark operator and History server.

* Install KUDO plugin for kubectl::

   VERSION=0.19.0 # look up the current stable release at https://github.com/kudobuilder/kudo/releases/latest
   OS=$(uname | tr '[:upper:]' '[:lower:]')
   ARCH=$(uname -m)
   wget -O kubectl-kudo https://github.com/kudobuilder/kudo/releases/download/v${VERSION}/kubectl-kudo_${VERSION}_${OS}_${ARCH}
   chmod +x kubectl-kudo
   # add to your path
   sudo mv kubectl-kudo /usr/local/bin/kubectl-kudo

* Initialize the KUDO::
   
   kubectl kudo init
   
* Create spark config secret, using access keys from MinIO::

   cat << 'EOF' >> spark-defaults.conf
    spark.hadoop.fs.s3a.access.key <access_key>
    spark.hadoop.fs.s3a.secret.key <access_secret_key>
    spark.hadoop.fs.s3a.impl org.apache.hadoop.fs.s3a.S3AFileSystem
    spark.hadoop.fs.s3a.endpoint https://minio.demo.svc.cluster.local
    spark.hadoop.fs.s3a.path.style.access true
   EOF 
   
   kubectl create secret generic spark-conf --from-file spark-defaults.conf --namespace demo 
   
* Install Spark history server and Spark operator in the same namespace where MinIO tenant was setup::
   
   kubectl kudo install spark --instance=spark-operator --namespace demo \
   -p operatorImageName=sparkflows/spark-operator \
   -p operatorVersion=3.0.0 \
   -p imagePullPolicy=Always \
   -p enableHistoryServer=true \
   -p historyServerFsLogDirectory="s3a://spark/logs" \
   -p historyServerSparkConfSecret=spark-conf
   
* Verify that the Spark history server is up and running::

   kubectl get pod -n demo
   
   spark-operator-64cd9c8d5b-k7xns                 1/1     Running            0          2d22h
   spark-operator-history-server-f9945cf64-znft4   1/1     Running            0          2d22h
   spark-operator-init-d6p5s                       0/1     Completed          0          2d22h
   
 
