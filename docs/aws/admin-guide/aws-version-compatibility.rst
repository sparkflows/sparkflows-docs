AWS Version Compatibility
==========

EMR Versions
-----------

The below page lists the version of Apache Spark used with various versions of AWS EMR.

https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Spark-release-history.html

Updates to bootstrap and wheel file
-------------

* For emr-6.6.0, in the bootstrap and wheel file version of h2o-pysparkling needs to be changed to h2o-pysparkling-3.2==3.36.1.2.post1.
* For emr-6.9.0, in the bootstrap and wheel file version of h2o-pysparkling needs to be changed to h2o-pysparkling-3.3.

Delta Support
------------

For delta support, in Spark workflow include the below jars in Livy connection.

 * emr-6.6.0: delta-core_2.12-2.0.1.jar & delta-storage-2.0.1.jar

 * emr-6.9.0: delta-core_2.12-2.1.0.jar & delta-storage-2.1.0.jar

 * emr-6.2.1: delta-core_2.12-0.8.0.jar

For delta support, in the Pyspark workflow

In EMR Bootstrap, include the:

aws s3 cp s3://sparkflows-release/fire/delta/delta-core_2.12-0.8.0.jar /usr/lib/spark/jars/

In Pyspark include the below step to import the delta package in pyspark.

spark.sparkContext.addPyFile("s3://sparkflows-release/fire/delta/delta-core_2.12-0.8.0.jar")

