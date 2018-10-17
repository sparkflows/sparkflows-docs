Fire Integration with HIVE
==========================

Fire seamlessly integrates with HIVE when running on AWS.

Overview
--------

On AWS, the data normally resides in S3 buckets. HIVE tables are created pointing to data in the S3 buckets.

Details
-------

* Fire would run on the master node of the EMR cluster, or on an Edge node with the cluster contiguration files.

* HIVE can be running on the same EMR cluster on running on another EMR cluster. 

* Make sure to have the correct hive-site.xml on the cluster where the Spark jobs are running.

* Fire will automatically pick it up and be able to process it.


Writing to HIVE
-------

Below is a workflow for writing to HIVE.

It reads housing.csv, creates a DataFrame and writes it out to a HIVE table.
