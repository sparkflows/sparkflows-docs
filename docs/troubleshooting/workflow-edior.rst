Workflow Editor
===============

Could not connect to fire
------------------

When double clicking on a node in the editor it shows "Could not connect to Fire".

If Fire is configured to submit job to a cluster with spark-submit, first try to ensure you are able to submit jobs to the cluster with spark-submit

Make sure to set SPARK_HOME and add spark/bin to your PATH.

https://spark.apache.org/docs/latest/submitting-applications.html

The above page has an example of submitting sparkpi job to the cluster.

spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master spark://207.184.161.138:7077 \
  --executor-memory 20G \
  --total-executor-cores 100 \
  /path/to/examples.jar \
  1000
  
  
  

