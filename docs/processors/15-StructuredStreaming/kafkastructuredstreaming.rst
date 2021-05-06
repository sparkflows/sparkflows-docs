StructuredStreamingKafka
=========== 

Reads in streaming text from topics in Apache Kafka

Input
--------------
It does not take any DataFrame as input

Output
--------------
It reads events from Kafka and creates DataFrame from the resulting rows. This DataFrame is passed to the output Nodes.

Type
--------- 

sparkstreaming

Class
--------- 

fire.nodes.structuredstreaming.NodeStructuredStreamingKafka

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - batchDuration
        - Batch Duration in Seconds
        - Batch Duration in Seconds
      * - brokers
        - Kafka Brokers
        - Kafka Brokers
      * - group
        - Consumer Group
        - Consumer Group
      * - topics
        - Kafka Topics
        - List of Topics separated by , (comma)
      * - autoOffsetReset
        - auto.offset.reset
        - Auto Offset Reset
      * - enableAutoCommit
        - enable.auto.commit
        - Enable Auto Commit
      * - kafkaParamsKeys
        - Params Key/Value Pairs
        - More Config Values
      * - kafkaParamsValues
        - Parms Key/Value Pairs
        - More Config Values




