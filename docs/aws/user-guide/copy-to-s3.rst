Copying files to S3 with aws-cli
===========

This document serves as a guide to describe the process when you want to upload multiple files from your laptop to an S3 bucket. Follow the below steps for copying files to an S3 bucket using AWS-CLI.

1. *Install AWS-CLI on machine if not already installed*
2. *Configure AWS Credentials*
3. *View the S3 Bucket*
4. *View the S3 Directory*
5. *Copy files to the S3 bucket*
6. *Delete all files in directory*

Installing AWS-CLI on mac
------------------------
..  code::
 
 brew install aws-cli


Configure AWS Credentials
-------------------------
.. code::
  
  AWS configure

  Enter your awsAccessKeyId:
  Enter your awsSecretAccessKey:
  Enter default region name:
  Enter default output format:
  

View S3 Buckets
---------------
.. code::
  
  aws s3 ls

View S3 Directory
---------------
.. code::

  aws s3 ls s3://bucket_name/dir1/

Copy files to S3
---------------------

In order to copy all files from local_direcory to s3://bucket-name/dir1::
.. code::

  aws s3 cp local_directory s3://bucket-name/dir1 --recursive


Delete All Files in Directory
-------------------------
.. code::

  aws s3 rm s3://bucket_name/dir1/ --recursive


Setting Roles and Policies for EMR
--------------------------------

In order to be able to access S3 files from the EMR cluster, attach the AmazonS3FullAccess Policy to the EMRDefaultRole.

Now, the EMR cluster would have access to the S3 buckets.


REFERENCE : Creating Access Key & Secret Key
--------------

1. You need to create a user with programmatic access by following the steps here: (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

 

2. Next, you need to create an IAM policy that defines the access limit of the user in your AWS account.  It's important to grant only restricted access access to the user within your account. Refer the document available at the below link for further information on creating IAM Policies: (https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html).

 

3. Lastly, you need to create an access key and secret key for this user by following steps given at the link: (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).

.. note:: It's important to regularly rotate your access and secret keys. Refer the document available at the below link for more information: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console



