Write To SnowFlake
=========== 



Input
--------------
The Dataframe from the previous node

Output
--------------
The incoming Dataframe is passed to the next node as it is

Type
--------- 

transform

Class
--------- 

fire.nodes.snowflake.NodeWriteToSnowFlake

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - connection
        - Connection
        - The Snowflake connection to connect
      * - sfWarehouse
        - Snowflake Warehouse
        - Warehouse for connecting to the Snowflake
      * - sfDatabase
        - Snowflake Database
        - Database for connecting to the Snowflake
      * - sfSchema
        - Snowflake Schema
        - Schema for connecting to the Snowflake
      * - dbtable
        - Snowflake Table
        - Snowflake Table from which to read the data
      * - saveMode
        - Save Mode
        - Whether to Append, Overwrite or Error if the table Exists


Details
-------


This node saves the rows of the incoming DataFrame into Snowflake.


