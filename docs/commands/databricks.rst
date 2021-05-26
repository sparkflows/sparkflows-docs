Databricks
==========

Mounting an S3 bucket onto DBFS
-------------------

* Below are the steps for mounting an S3 bucket onto DBFS::

      aws_bucket_name = "Saprkflow-sample-data"
      mount_name = "mount_dev"
      dbutils.fs.mount("s3a://%s" % aws_bucket_name, "/mnt/%s"  % mount_name)
      display(dbutils.fs.ls "/mnt/%s"  % mount_name)
      

