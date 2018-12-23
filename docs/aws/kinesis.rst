Fire Integration with Kinesis
==============================

Sending the message to AWS kinesis from aws cli
------------

aws kinesis put-record --stream-name sparkflows_kinesis_test --data file://data.json --partition-key uuidgen

