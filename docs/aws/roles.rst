AWS Setup
===========

Installing aws-cli on mac
------------------------

  brew install awscli


Configure AWS Credentials
-------------------------

aws configure::

  - Enter your awsAccessKeyId
  - Entery your awsSecretAccessKey
  

View S3 Buckets
---------------

- aws s3 ls

View S3 Directory
---------------

- aws s3 ls bucket_name/dir1/

Copy files to S3
---------------------

Copy all files from local_direcory to s3://bucket-name/dir1::

  aws s3 cp local_directory s3://bucket-name/dir1 --recursive


Setting Roles and Policies for EMR
--------------------------------

In order to be able to access S3 files from the EMR cluster, attach the AmazonS3FullAccess Policy to the EMRDefaultRole.

Now the EMR cluster would have access to the S3 buckets.


