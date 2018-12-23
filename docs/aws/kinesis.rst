Fire Integration with Kinesis
==============================

Update EMR_EC2_DefaultRole with AmazonKinesisFullAccess & AmazonSageMakerFullAccess


Sending the message to AWS kinesis from aws cli
------------

Sending message to Kinesis::

  aws kinesis put-record --stream-name sparkflows_kinesis_test --data file://data.json --partition-key uuidgen

