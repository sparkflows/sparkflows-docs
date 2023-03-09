Execute Query In SnowFlake
=========== 

This node executes query in Snowflake.

Output
--------------
DataFrame created from the data read in from Snowflake.

Type
--------- 

Dataset

Class
--------- 

fire.nodes.snowflake.NodeExecuteQueryInSnowFlake

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
        - The Snowflake connection to connect.
      * - sfWarehouse
        - Snowflake Warehouse
        - Warehouse for connecting to the SnowFlake.
      * - sfDatabase
        - Snowflake Database
        - Database for connecting to the Snowflake.
      * - sfSchema
        - Snowflake Schema
        - Schema for connecting to the Snowflake.
      * - query
        - Snowflake Query
        - 
      * - outputColNames
        - Output Column Names
        - Name of the Output Columns.
      * - outputColTypes
        - Output Column Types
        - Data Type of the Output Columns.
      * - outputColFormats
        - Output Column Formats
        - Format of the Output Columns.


Details
-------


This node executes the provided query in Snowflake. It creates a DataFrame from the data read from Snowflake and passes to the next nodes.


Examples
-------


SQL Structure
+++++++++++++++

Below is a sample SQL Structure to be used:

SELECT [COLUMNS] FROM [DATABASE].[SCHEMA].[TABLE]

SQL Example
+++++++++++++++

SELECT ID, price, lotsize, bedrooms from housingdb.housingschema.housing
