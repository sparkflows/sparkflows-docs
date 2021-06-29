Write To SnowFlake
=========== 



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
      * - sfDatabase
        - SF Database
        - Database for connecting to the SnowFlake
      * - sfSchema
        - SF Schema
        - Schema for connecting to the SnowFlake
      * - sfWarehouse
        - SF Warehouse
        - Warehouse for connecting to the SnowFlake
      * - saveMode
        - Save Mode
        - Whether to Append, Overwrite or Error if the table Exists
      * - dbtable
        - SF Table
        - 


Details
-------


This node saves the rows of the incoming DataFrame into Snowflake.


