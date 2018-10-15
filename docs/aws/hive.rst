Fire Integration with HIVE
==========================

Fire seamlessly integrates with HIVE when running on AWS.

Overview
--------

On AWS, the data normally resides in S3 buckets. HIVE tables are created pointing to data in the S3 buckets.

Details
-------

HIVE can be running on the same EMR cluster on running on another EMR cluster. 

Make sure to have the corred hive-site.xml on the cluster.

Fire will automatically pick it up and be able to process it.

