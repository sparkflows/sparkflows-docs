Hash
=========== 

This node adds a new Columns which contains the Hash of the specified columns

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new column is added to the incoming DataFrame by creating a Hash of the specified input columns.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeHash

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Columns
        - Columns to be concatenated
      * - hashingAlgorithm
        - Hashing Algorithm
        - Hashing Algorithm
      * - outputCol
        - Output Column Name
        - Column name for Hash
      * - bitLength
        - Bit Length
        - Bit Length
      * - sep
        - Separator
        - Separator to be used when concatenating the columns




