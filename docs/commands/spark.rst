Apache Spark Commands
==============

* Submit a Spark Pi Job::

    spark-submit   --class org.apache.spark.examples.SparkPi --master yarn /usr/lib/spark/examples/jars/spark-examples.jar
    
    
* Submit a Spark Pi Job on CDH-7.1.3::

    spark-submit --class org.apache.spark.examples.SparkPi /opt/cloudera/parcels/CDH-7.1.3-1.cdh7.1.3.p9.14188514/lib/spark/examples/jars/spark-examples_2.11-2.4.0.7.1.3.9-1.jar
