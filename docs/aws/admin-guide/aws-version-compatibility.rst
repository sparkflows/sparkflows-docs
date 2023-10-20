AWS Version Compatibility
==========

EMR Versions
-----------

For emr-6.6.0, in the bootstrap and wheel file version of h2o-pysparkling needs to be changed to h2o-pysparkling-3.2==3.36.1.2.post1.
For emr-6.9.0, in the bootstrap and wheel file version of h2o-pysparkling needs to be changed to h2o-pysparkling-3.3.

The above update will allow normal Pyspark workflow to run.

For delta support, in Pyspark workflow include the below jars in Livy connection.

 emr-6.6.0: delta-core_2.12-2.0.1.jar & delta-storage-2.0.1.jar
 emr-6.9.0: delta-core_2.12-2.1.0.jar & delta-storage-2.1.0.jar
 emr-6.2.1: delta-core_2.12-0.8.0.jar

