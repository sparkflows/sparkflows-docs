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


Details
-------


This node adds a new Column which contains the Hash of the specified columns in the incoming Dataframe.

Hash value is computed by applying the selected algorithm on selected columns. 


Examples
-------


Incoming Dataframe has following rows:

PRD_CD    |    PRD_NAME          |    LIST_PRICE    |    TAX_AMT    |    DISCOUNT
--------------------------------------------------------------------------------------
P01       |    DRILL MACHINE     |    1000.0        |    100.0      |    50.0
P02       |    WEIGHING MACHINE  |    1500.0        |    200.0      |    150.0
P03       |    HAMMER            |    100.0         |    10.0       |    5.0

if Hash node is configured to add a new hash value column [HASH_VALUE] using [PRD_CD] column by applying [MD5] algorithm
then outgoing Dataframe would be created as below:

PRD_CD    |    PRD_NAME          |    LIST_PRICE    |    TAX_AMT    |    DISCOUNT    |    HASH_VALUE
-----------------------------------------------------------------------------------------------------------------------------
P01       |    DRILL MACHINE     |    1000.0        |    100.0      |    50.0        |    8c45d49a19ecb0a312bcb3b071baeade
P02       |    WEIGHING MACHINE  |    1500.0        |    200.0      |    150.0       |    eefd2b4a1e11d3a7c8565d42920ca84b
P03       |    HAMMER            |    100.0         |    10.0       |    5.0         |    ba7e005bf556bb35e37bccddc6ce485b
