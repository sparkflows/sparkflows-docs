Fire Integration with Kinesis
==============================

Update EMR_EC2_DefaultRole with AmazonKinesisFullAccess & AmazonSageMakerFullAccess

Install AWS CLI::

  https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html
  
Configure::

  aws configure region: us-east-1 aws_access_key_id = accesskeyid aws_secret_access_key = awssecretaccesskey

Sending the message to AWS kinesis from aws cli
------------

Sending message to Kinesis::

  aws kinesis put-record --stream-name sparkflows_kinesis_test --data file://data.json --partition-key uuidgen

