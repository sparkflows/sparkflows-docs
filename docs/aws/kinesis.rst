Fire Integration with Kinesis
==============================

Sending the message to AWS kinesis from aws cli
------------

Sending message to Kinesis::

  aws kinesis put-record --stream-name sparkflows_kinesis_test --data file://data.json --partition-key uuidgen

