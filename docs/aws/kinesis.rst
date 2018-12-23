Fire Integration with Kinesis
==============================

This document described Fire integration with Kinesis.

Update EC2 Role
------------

Update EMR_EC2_DefaultRole with AmazonKinesisFullAccess & AmazonSageMakerFullAccess

Install AWS CLI
----------

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
  
Configure AWS Access Key
-----------

  aws configure region: us-east-1 aws_access_key_id = accesskeyid aws_secret_access_key = awssecretaccesskey

Create AWS Kinesis stream
-----------



Send message to AWS Kinesis from AWS CLI
------------

Sending message to Kinesis::

  aws kinesis put-record --stream-name sparkflows_kinesis_test --data file://data.json --partition-key uuidgen

