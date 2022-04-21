Read From SnowFlake
=========== 

This node reads a table from Snowflake

Output
--------------
Dataframe created from the data read from Snowflake

Type
--------- 

dataset

Class
--------- 

fire.nodes.snowflake.NodeReadFromSnowFlake

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
        - Warehouse for connecting to the SnowFlake
      * - sfDatabase
        - Snowflake Database
        - Database for connecting to the SnowFlake
      * - sfSchema
        - Snowflake Schema
        - Schema for connecting to the SnowFlake
      * - dbtable
        - Snowflake Table
        - Snowflake Table from which to read the data
      * - schema
        - Schema
      * - outputColNames
        - Output Column Names
        - Name of the Output Columns
      * - outputColTypes
        - Output Column Types
        - Data Type of the Output Columns
      * - outputColFormats
        - Output Column Formats
        - Format of the Output Columns


Details
-------


This node reads a table from Snowflake.


