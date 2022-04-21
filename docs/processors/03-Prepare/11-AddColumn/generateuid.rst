Generate UID
=========== 

This node Generates a new column with unique Index/Value for each row in the Dataset for each partition. Each Partition starts a new range.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeGenerateUID

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - outputCol
        - UID Column Name
        - UID column name


Details
-------


This node Generates a new column with unique Index/Value for each row in the incoming Dataframe.


Examples
-------


Incoming Dataframe has following rows:

PRD_CD    |    PRD_NAME          |    LIST_PRICE    |    TAX_AMT    |    DISCOUNT
--------------------------------------------------------------------------------------
P01       |    DRILL MACHINE     |    1000.0        |    100.0      |    50.0
P02       |    WEIGHING MACHINE  |    1500.0        |    200.0      |    150.0
P03       |    HAMMER            |    100.0         |    10.0       |    5.0

if GenerateUID node is configured to generate UID for each row and add it as a new column [UID_VAL] 
then outgoing Dataframe would be created as below:

PRD_CD    |    PRD_NAME          |    LIST_PRICE    |    TAX_AMT    |    DISCOUNT    |    UID_VAL
------------------------------------------------------------------------------------------------------
P01       |    DRILL MACHINE     |    1000.0        |    100.0      |    50.0        |    0
P02       |    WEIGHING MACHINE  |    1500.0        |    200.0      |    150.0       |    1
P03       |    HAMMER            |    100.0         |    10.0       |    5.0         |    2
