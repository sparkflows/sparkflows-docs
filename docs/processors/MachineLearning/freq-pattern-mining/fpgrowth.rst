FPGrowth
=========== 

Does Pattern Mining using FPGrowth Algorithm

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeFPGrowth

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - transactionCol
        - Transaction Column
        - Input data set, each element contains a transaction
      * - minSupport
        - Min Support
        - The minimum support for an itemset to be identified as frequent
      * - numPartitions
        - Number of Partitions
        - The number of partitions used to distribute the work


Details
======


This node does Pattern Mining using FPGrowth Algorithm.

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/mllib-frequent-pattern-mining.html


