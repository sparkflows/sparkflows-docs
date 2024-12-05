AWS EMR Spark Delta Version Compatibility
==========

EMR Versions
-----------

The below page lists the version of Apache Spark used with various versions of AWS EMR:

`AWS EMR Spark Release History <https://docs.aws.amazon.com/emr/latest/ReleaseGuide/Spark-release-history.html>`_

It also lists the compatability matrix of Spark version and Delta lake version:

`Spark and Delta Lake Compatibility Matrix <https://docs.delta.io/latest/releases.html>`_

Delta Support
------------

For delta support, in Spark workflow include the below JARs in Livy connection:

 * For **emr-6.2.1** include the JAR with the exact version: **delta-core_2.12-0.8.0.jar**

 * For **emr-6.6.0** include the two JARs with the exact version: **delta-core_2.12-2.0.1.jar** and **delta-storage-2.0.1.jar**

 * For **emr-6.9.0** include the two JARs with the exact version: **delta-core_2.12-2.1.0.jar** and **delta-storage-2.1.0.jar**

 * For **emr-6.15.0** include the two JARs with the exact version: **delta-core_2.12-2.4.0.jar** and **delta-storage-2.4.0.jar**


For delta support, in the Pyspark workflow include the below in the EMR Bootstrap script:

	::

  		aws s3 cp s3://sparkflows-release/fire/delta/delta-core_2.12-0.8.0.jar /usr/lib/spark/jars/

