Integration with Hive
==========================

Fire seamlessly integrates with Hive where it is running on AWS.

Overview
--------

On AWS, the data normally resides in S3 buckets. Hive tables are created pointing to data in S3 buckets.

Details
-------

* Fire would run on the master node of the EMR cluster, or on an Edge node with the cluster contiguration files.

* Hive can run on the same or any other EMR cluster. 

* Make sure that hive-site.xml is available on the cluster where the Spark jobs are running.

* Fire will automatically pick it up and process it.


Write to Hive
-------

Below is a workflow for writing to Hive. It reads housing.csv, creates a DataFrame and writes it out to a Hive table.

  .. figure:: ../../_assets/aws/hive/save-as-hive-table-wf.png
     :alt: write to snowflake
     :width: 65%
   
