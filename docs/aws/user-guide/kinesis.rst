Integration with Kinesis
==============================

This document describes Fire integration with Kinesis. Fire uses Apache Spark Structured Streaming Connector from Qubole. Please visit the following link for detailed information.

https://github.com/qubole/kinesis-sql

Install AWS-CLI
----------

You need to install AWS-CLI. Please visit the following link for more information on installation steps.

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
  
Create Access Key and Secret Key
----------------------------------

You need to create an access key and secret key for the user. Please visit the following link for more information on creation of the keys.

https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey

.. note:: It's important to regularly rotate your access and secret keys. Please visit the following link for more information.     https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console


Configure AWS-CLI
-----------

Please visit the following link to get more information on configuration details of AWS-CLI.

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html ::
  
  aws configure region: us-east-1 aws_access_key_id = accesskeyid aws_secret_access_key = awssecretaccesskey

Create AWS Kinesis Stream
-----------

You need to create AWS Kinesis Stream::

  aws kinesis create-stream --stream-name sparkflows_kinesis_test --shard-count 1

Send message to AWS Kinesis from AWS CLI
------------

You need to send message to Kinesis::

  aws kinesis put-record --stream-name sparkflows_kinesis_test --data file://data.json --partition-key uuidgen

Update EMR_EC2_Default_Role
------------

Update **EMR_EC2_DefaultRole** with **AmazonKinesisFullAccess** Policy so that our EMR Cluster would have full access to Kinesis.

Alternatively Create an IAM policy for accessing Amazon Kinesis
---------------------------------------------------

Alternatively, create an IAM policy that defines what exactly this user has access to in your AWS account.  It's important to grant only restricted access to this user within your account. Please visit the following link for more information. https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html


Create EMR Cluster with the above Role
-----------

When the EMR cluster is created with the above Role, it would have full access to Amazon Kinesis.

Push data to Kinesis
-----------

AWS provides a Kinesis Data Generator. It can be configured to push random data in specified format to Kinesis. Please visit the following link for more information.

https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html

.. figure:: ../../_assets/aws/kinesis-data-generator-1.png
   :alt: Kinesis Data Generator
   :align: center
   
   
.. figure:: ../../_assets/aws/kinesis-data-generator-2.png
   :alt: Kinesis Data Generator
   :align: center
   
   
Kinesis Workflow in Fire
----------

Workflows can be easily built in Fire which reads data from Kinesis, process them and save the results where needed.


REFERENCE : Create Access Key & Secret Key
--------------

1. Firstly, you need to create a user with programmatic access. Please visit the following link for more information. https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html

 

2. Secondly you need to create an IAM policy that defines what exactly this user has access to in your AWS account.  It's important to grant only restricted access to this within your account. Please visit the following link to get more information on how to create IAM Policies.  https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html

 

3. Lastly, you need to create an access key and a secret key for this user. Please visit the following link for more information on creation of the keys. https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey

.. note:: It's important to regularly rotate your access and secret keys. Please visit the following link for more information. https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console


