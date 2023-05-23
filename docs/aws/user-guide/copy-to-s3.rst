Copy files to S3 with AWS-CLI
===========

This document offers a step-by-step guide for seamlessly transferring multiple files from your laptop to an S3 bucket. By following the instructions provided below, you can easily copy the files to the S3 bucket using the AWS-CLI.

#. Install AWS-CLI on machine, if not already installed
#. Configure AWS Credentials
#. View the S3 Bucket
#. View the S3 Directory
#. Copy files to the S3 bucket
#. Delete all files in directory

Step 1 : Install AWS-CLI on Mac
------------------------
..  code::
 
 brew install aws-cli


Step 2 : Configure AWS Credentials
-------------------------
.. code::
  
  AWS configure

  Enter your awsAccessKeyId:
  Enter your awsSecretAccessKey:
  Enter default region name:
  Enter default output format:
  

Step 3 : View S3 Buckets
---------------
.. code::
  
  aws s3 ls

Step 4 : View S3 Directory
---------------
.. code::

  aws s3 ls s3://bucket_name/dir1/

Step 5 : Copy Files to S3
---------------------

In order to copy all files from local_direcory to s3://bucket-name/dir1/

.. code::

  aws s3 cp local_directory s3://bucket-name/dir1 --recursive


Step 6 : Delete All Files in Directory
-------------------------
.. code::

  aws s3 rm s3://bucket_name/dir1/ --recursive


Set Roles and Policies for EMR
--------------------------------

In order to be able to access S3 files from the EMR cluster, attach the AmazonS3FullAccess Policy to the EMRDefaultRole.

Now, the EMR cluster would have access to the S3 bucket.


Reference : Create Access Key & Secret Key
--------------

#. Firstly, you need to create a user with programmatic access. To create the user follow steps given in the `AWS User-Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html>`_

 

#. Secondly, you need to create an IAM policy that defines the access limit of the user in your AWS account. 
   
   It is recommended to grant restricted access to the user within your account. To create IAM policy follow the steps given in the `AWS User-Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html>`_

 
#. Lastly, you need to create an access key and secret key for this user. To create the keys follow the steps given in the `AWS User-Guide. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey>`_

.. note:: It is always recommended to rotate your access and secret keys regularly. For more details on rotation refer the `AWS documentation. <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console>`_



