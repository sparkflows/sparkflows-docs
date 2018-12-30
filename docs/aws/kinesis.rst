Fire Integration with Kinesis
==============================

This document described Fire integration with Kinesis. Fire uses Apache Spark Structured Streaming Connector from Qubole.

https://github.com/qubole/kinesis-sql

Install AWS CLI
----------

Install AWS CLI::

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
  
Configure AWS CLI
-----------

Configure AWS CLI::

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html
  aws configure region: us-east-1 aws_access_key_id = accesskeyid aws_secret_access_key = awssecretaccesskey

Create AWS Kinesis Stream
-----------

Create AWS Kinesis Stream::

  aws kinesis create-stream --stream-name sparkflows_kinesis_test --shard-count 1

Send message to AWS Kinesis from AWS CLI
------------

Sending message to Kinesis::

  aws kinesis put-record --stream-name sparkflows_kinesis_test --data file://data.json --partition-key uuidgen

Update EMR_EC2_Default_Role
------------

Update **EMR_EC2_DefaultRole** with **AmazonKinesisFullAccess** Policy so that our EMR Cluster would have full access to Kinesis.


Create EMR Cluster with the above Role
-----------

When we create the EMR Cluster with the above Role, it would have full access to Amazon Kinesis.

Pushing data to Kinesis
-----------

AWS provides a Kinesis Data Generator. It can be configured for pushing random data in specified format to Kinesis.

https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html

.. figure:: ../_assets/aws/kinesis-data-generator-1.png
   :alt: Kinesis Data Generator
   :align: center
   
   
.. figure:: ../_assets/aws/kinesis-data-generator-2.png
   :alt: Kinesis Data Generator
   :align: center
   
   
