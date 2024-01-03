Job Submission
==========

Fire Insights enables you to submit the Job on an Existing Kubernetes Cluster.

Below are the script takes care of setting up the classpath with Spark and its dependencies, and can support different cluster managers and deploy modes that Spark supports:

::

    spark-submit \
    --master k8s://https://<k8s-apiserver-host>:<k8s-apiserver-port> \
    --deploy-mode cluster \
    --name spark-pi \
    --class org.apache.spark.examples.SparkPi \
    --conf spark.executor.instances=5 \
    --conf spark.kubernetes.container.image=<spark-image> \
    local:///path/to/examples.jar

Some of the commonly used options are:

::

   --class: The entry point for your application (e.g. org.apache.spark.examples.SparkPi)
   --master: The master URL for the cluster 
   --deploy-mode: Whether to deploy your driver on the worker nodes (cluster) or locally as an external client (client) (default: client) †
   --conf: Arbitrary Spark configuration property in key=value format. For values that contain spaces wrap “key=value” in quotes (as shown). Multiple configurations should be passed as separate arguments. (e.g. --conf <key>=<value> --conf <key2>=<value2>)

Reference link
++++++++++++

For more details, read `Apache Spark Documentation. <https://spark.apache.org/docs/latest/submitting-applications.html>`_
