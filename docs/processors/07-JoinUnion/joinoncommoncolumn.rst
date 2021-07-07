Join On Common Column
=========== 

This node joins the incoming dataframes on a joinCol

Input
--------------
This node takes in 2 DataFrames as input and produces one DataFrame as output

Output
--------------
The output DataFrame is the result of joining the 2 incoming DataFrames on the join column

Type
--------- 

join

Class
--------- 

fire.nodes.etl.NodeJoinUsingColumn

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - joinCol
        - Common Join Column
        - column on which to join
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




