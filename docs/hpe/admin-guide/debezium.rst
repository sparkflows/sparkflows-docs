Debezium
======

Debezium is used to stream database changes, which are then merged into a dataset. For detailed information on setting up the Debezium server, refer to the `Debezium Server Setup Documentation <https://debezium.io/documentation/reference/stable/operations/debezium-server.html>`_.




Design
----

Below is the design of the overall flow.

.. figure:: ../../_assets/hpe/debezium_design.png
      :width: 60%
      :alt: HPE UA Add framework details

* Debezium reads database logs and generates JSON messages that describe the changes.
* These messages are streamed to Kafka.
* Kafka stores the messages in an S3 folder.
* Using Spark with Delta Lake, the messages can be transformed into INSERT, UPDATE, and DELETE operations and applied to the target Delta Lake table.

.. figure:: ../../_assets/hpe/debezium_setup.png
   :width: 60%
   :alt: HPE UA Add framework details

Useful Commands
-----

Check the Connect Status
+++++++++++++++++++++++++

Use the following command to check if Debezium is connected:

   ::

        curl -H "Accept:application/json" {hostname}:8083/

List the Connectors
++++++++++++++++++++

To list all the connectors registered with Debezium, use:
   
   ::

        curl -H "Accept:application/json" {hostname}:8083/connectors/



Register the Source Connector
+++++++++++++++++++++++++++++++++

To register the source connector with Debezium, execute the following command:

   ::

        curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" {hostname}:8083/connectors/ -d @source.json


Here is an example of a **source.json** file:

   ::

        {"name": "inventory-connector",  
        "config": {  
        "connector.class": "io.debezium.connector.mysql.MySqlConnector",
        "tasks.max": "1",  
        "database.hostname": "mysql",  
        "database.port": "3306",
        "database.user": "debezium",
        "database.password": "dbz",
        "database.server.id": "184054",  
        "topic.prefix": "dbserver1",  
        "table.include.list": "inventory.customers",
        "snapshot.mode":"when_needed",
        "decimal.handling.mode": "double",
        "include.schema.changes": "true",  
        "schema.history.internal.kafka.bootstrap.servers": "kafka:9092",  
        "schema.history.internal.kafka.topic": "schema-changes.inventory",
        "key.converter.schemas.enabled": "false",
        "value.converter.schemas.enabled": "false", 
        "transforms": "unwrap",
        "transforms.unwrap.add.fields": "name,op,db,table,source.ts_ms",
        "transforms.unwrap.delete.handling.mode": "rewrite",
        "transforms.unwrap.drop.tombstones": "true",
        "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState"  
        }}

Register the Sink Connector
+++++++++++++++++++++++++

To register the sink connector, use the following command:
   
   ::

        curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" {hostname}:8083/connectors/ -d @sink.json

Here is an example of a **sink.json** file:

   ::

        {
        "name": "sink_connector_kafka_s3_avro_tickit",
        "config": {
        "behavior.on.null.values": "ignore",
        "connector.class": "io.confluent.connect.s3.S3SinkConnector",
        "flush.size": 10000,
        "locale": "en-US",
        "format.class":"io.confluent.connect.s3.format.json.JsonFormat",
        "partitioner.class": "io.confluent.connect.storage.partitioner.DailyPartitioner",
        "rotate.schedule.interval.ms": 60000,
        "s3.bucket.name": "assume-role-bucket1",
        "s3.part.size": 5242880,
        "s3.region": "us-east-1",
        "aws.access.key.id":"XXXXXXX",
        "aws.secret.access.key":"XXXXXXXXXXXXXXXXXXXXXX",
        "schema.compatibility": "NONE",
        "schema.generator.class":                 
        "io.confluent.connect.storage.hive.schema.DefaultSchemaGenerator",
        "storage.class": "io.confluent.connect.s3.storage.S3Storage",
        "tasks.max": 1,
        "table.name.format": "${topic}",
        "timestamp.extractor": "Wallclock",
        "timezone": "UTC",
        "store.url": "",
        "topics.dir": "cdc_data_lake/bronze",
        "topics.regex": "dbserver1.inventory.(.*)",
        "key.converter.schemas.enabled": "false",
        "value.converter.schemas.enabled": "false"
        } 
        }

   .. note:: Ensure you update the aws.secret.access.key and aws.access.key.id with the actual values.



Useful Configuration Fields
--------------------------------
Some useful fields to include in your configuration are:

::

      "database.whitelist": "myDb"
      "table.whitelist": "myDb.table1,myDb.table2"
      "store.url": "http://kafkasgd.rtpppe.netapp.com:10444/"  

Debezium Monitoring
-----------

For monitoring Debezium, refer to the `Debezium Monitoring Documentation <https://debezium.io/documentation/reference/stable/configuration/avro.html>`_.

