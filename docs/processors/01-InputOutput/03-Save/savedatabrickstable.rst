Save Databricks Table
=========== 

This node saves a input data as table in Databricks

Input
--------------
It take dataframe as input data.

Output
--------------
It creates a Table in Databricks from the dataframe(input data).

Type
--------- 

transform

Class
--------- 

fire.nodes.databricks.NodeSaveDatabricksTable

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - database
        - Databricks Database
        - Name of the Database
      * - table
        - Databricks Table
        - Name of the table
      * - format
        - Format
        - File format when saving to Table
      * - saveMode
        - Save Mode
        - Whether to Append, Overwrite or Error if the path Exists
      * - advanced
        - Advanced
      * - partitionBy
        - Partition By
        - List of columns to partition by - separated by ,


Details
-------


This node saves a input data as table in Databricks.


