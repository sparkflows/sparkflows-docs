Generate UUID
=========== 

This node Generates a Universally Unique ID

Input
--------------
It accepts a dataframe as input

Output
--------------
It adds a new column for UUID to the input DataFrame. This new DataFrame is sent to the output

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeGenerateUUID

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - outputCol
        - Output Column
        - Output Column Name


Details
-------


This node Generates a Universally Unique ID for each row.

It adds a new column for UUID to the input DataFrame. This new DataFrame is sent to the output.


Examples
-------


Incoming Dataframe has following rows:

DATA_COLS
-------------------------------------------
CUST001INV00120200101PRD0011200
CUST001INV00220200202PRD0022200

after execution of GenerateUUID node a UUID is generated for each row and is added as a column in the outgoing Dataframe as below:

DATA_COLS                           |    UUID_VALUE
------------------------------------------------------------------------------------
CUST001INV00120200101PRD0011200     |    61e55caa-22c6-4648-a26d-98df31f11784
CUST001INV00220200202PRD0022200     |    c70b2c9d-773a-45c2-acd7-bd3d256a4419
