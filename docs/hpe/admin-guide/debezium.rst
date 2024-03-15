Debezium
======



Overview
-----

Debezium is used to stream DB changes. These changes are then merged into the Dataset.

Design
----

Below is the design of the overall flow.

.. figure:: ../../_assets/hpe/debezium_design.png
      :width: 60%
      :alt: HPE UA Add framework details

#. Debezium reads database logs, produces json messages that describe the changes and streams them to Kafka
#. Kafka streams the messages and stores them in a S3 folder. 
#. Using Spark with Delta Lake we transform the messages to INSERT, UPDATE and DELETE operations, and run them on the target delta lake table.

.. figure:: ../../_assets/hpe/debezium_setup.png
      :width: 60%
      :alt: HPE UA Add framework details

Useful Command
-----

#. To check the connect

   ::

        curl -H "Accept:application/json" {hostname}:8083/

#. List the connectors

   ::

        curl -H "Accept:application/json" {hostname}:8083/connectors/

#. Register the source with debezium

   ::

        curl -i -X POST -H "Accept:application/json" -H "Content-Type:application/json" {hostname}:8083/connectors/ -d @source.json



