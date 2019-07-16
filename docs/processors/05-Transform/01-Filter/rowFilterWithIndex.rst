NodeRowFilterByIndex
=========== 

This node creates a new DataFrame containing only rows satisfying given condition

Input
--------------
It accepts DataFrame as input from the previous Node

Output
--------------
This node filters the rows based on the conditional expression to generate the output DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeRowFilterByIndex

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - indexes
        - Indexes
        - Comma separated index values starts from 0. ex: 0, 1, 2, 5
      * - indexesRange
        - IndexesRange
        - Index ranges example like 10-14 i.e 10, 11, 12, 13, 14.




