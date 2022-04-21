ReadKafkaBatch
=========== 

Dataset Node for processing the batch 

Input
--------------
Create a Dataset/DataFrame for a defined range of offsets.

Output
--------------
It creates a DataFrame from defined range of offsets

Type
--------- 

dataset

Class
--------- 

fire.nodes.dataset.NodeKafkaBatchRead

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - broker
        - Broker
        - broker host:port
      * - topic
        - Topic
        - Kafka Topic Name
      * - maxRecordsPerTrigger
        - MaxRecordsPerTrigger
        - Maximum Number of Records to Process.
      * - path
        - Path
        - Location of the offsets file.




