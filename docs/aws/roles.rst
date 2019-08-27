Copying files to S3
===========

There would be times when you want to upload multiple files from your laptop to S3. This document describes the process for it.

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

- aws s3 ls s3://bucket_name/dir1/

Copy files to S3
---------------------

Copy all files from local_direcory to s3://bucket-name/dir1::

  aws s3 cp local_directory s3://bucket-name/dir1 --recursive


Delete All Files in Directory
-------------------------

- aws s3 rm s3://bucket_name/dir1/ --recursive


Setting Roles and Policies for EMR
--------------------------------

In order to be able to access S3 files from the EMR cluster, attach the AmazonS3FullAccess Policy to the EMRDefaultRole.

Now the EMR cluster would have access to the S3 buckets.


REFERENCE : Creating Access Key & Secret Key
--------------

1. You'll need create a user with programmatic access by following the steps here (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

 

2. Next, you'll create an IAM policy that defines what this user has access to in your AWS account.  It's important to only grant this user minimal access within your account. See this documentation for how to create IAM policies (https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html).

 

3. Finally, you'll create an access key and secret key for this user (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).

*Note* It's important to regularly rotate your access and secret keys. See this documentation for more information (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console)



