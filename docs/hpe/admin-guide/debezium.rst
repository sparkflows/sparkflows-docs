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
