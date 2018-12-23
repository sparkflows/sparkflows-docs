Fire Integration with Kinesis
==============================

This document described Fire integration with Kinesis.

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

Update EC2 Role
------------

Update EMR_EC2_DefaultRole with AmazonKinesisFullAccess

Create EMR Cluster with the above Role
-----------

