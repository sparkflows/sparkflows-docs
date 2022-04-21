Join Using SQL
=========== 

This node registers the incoming DataFrames as temporary tables and executes the SQL provided

Input
--------------
It takes in 2 DataFrames as input and produces one DataFrame as output by executing the provided SQL.

Output
--------------
The DataFrame created as a result of executing the join SQL

Type
--------- 

join

Class
--------- 

fire.nodes.etl.NodeJoinUsingSQL

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - tempTables
        - Temp Table Names
        - Temp Table Name to be used
      * - sql
        - SQL
        - SQL to be run
      * - schema
        - Schema
      * - outputColNames
        - Column Names for the CSV
        - New Output Columns of the SQL
      * - outputColTypes
        - Column Types for the CSV
        - Data Type of the Output Columns
      * - outputColFormats
        - Column Formats for the CSV
        - Format of the Output Columns


Details
-------



*  This node receives two input data frames, creates two temporary tables on top of that data frames.
*  Allows the user to write a SQL query to join these two temporary tables.
*  The resulting data frame of running the SQL is passed on to the next node.


Examples
-------


Examples
+++++++++++++++


*  select col1, col2, col3, col4, col5, col6 from tempTable1 a LEFT JOIN tempTable2 b ON(a.col1 = b.col5)
*  select col1, col2, col3 from tempTable1 a JOIN  tempTable2 b ON(a.col2 = b.col3)
