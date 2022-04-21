Read Databricks Table
=========== 

This node reads a table from Databricks

Input
--------------
It reads data from Databricks Table

Output
--------------
It creates a DataFrame from the data read and sends it to its output

Type
--------- 

dataset

Class
--------- 

fire.nodes.databricks.NodeReadDatabricksTable

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - db
        - Databricks Database
        - Databricks Database
      * - table
        - Databricks Table
        - Databricks Table from which to read the data
      * - query
        - Databricks Query (Optional)
        - If a separate Databricks query needs to be used for reading from the Databricks table. This field is optional.
      * - schema
        - Schema
      * - outputColNames
        - Column Names of the Table
        - Output Columns Names of the Table
      * - outputColTypes
        - Column Types of the Table
        - Output Column Types of the Table
      * - outputColFormats
        - Column Formats
        - Output Column Formats


Details
-------


This node reads a table from Databricks.


