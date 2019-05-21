Setting up Roles and Policies
=============================

This document describes the Roles and Policies setup for running Fire on AWS.

In order to be able to access S3 files from the EMR cluster, attach the AmazonS3FullAccess Policy to the EMRDefaultRole.

Now the EMR cluster would have access to the S3 buckets.


Installing aws-cli on mac
------------------------

brew install awscli


Configure AWS Credentials
-------------------------

aws configure
  - Enter your awsAccessKeyId
  - Entery your awsSecretAccessKey
  

View S3 Buckets
---------------

- aws s3 ls

Copy files in a directory to S3 Bucket
---------------------

aws s3 cp local_directory s3://bucket-name --recursive


