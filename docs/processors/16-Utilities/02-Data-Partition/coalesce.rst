Coalesce
=========== 

This node coalesces the DataFrame into specified number of Partitions

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame.

Output
--------------
The output DataFrame has the specified number of partitions

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeCoalesce

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - numPartitions
        - Number of Partitions
        - input for number of partitions


Details
-------


This node coalesces the DataFrame into specified number of Partitions.

It is specially helpful for the case when too many small files are being created. In such a scenario, the Coalesce node can be used to limit the number of output files produced.


