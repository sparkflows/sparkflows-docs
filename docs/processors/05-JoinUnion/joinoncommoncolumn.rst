Join On Common Column
=========== 

This node joins the incoming dataframes using one common column between them.

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
      * - joinType
        - JoinType
        - type of join
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


This node joins the incoming dataframes using one common column between the two dataframes. 

Select the Common Join Column to be used in the Join.


