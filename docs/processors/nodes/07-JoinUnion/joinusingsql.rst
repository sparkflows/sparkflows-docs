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
      * - tempTable1
        - Temp Table1
        - Temp Table Name to be used
      * - tempTable2
        - Temp Table2
        - Temp Table Name to be used
      * - tempTable3
        - Temp Table3
        - Temp Table Name to be used
      * - tempTable4
        - Temp Table4
        - Temp Table Name to be used
      * - tempTable5
        - Temp Table5
        - Temp Table Name to be used
      * - sql
        - SQL
        - SQL to be run
      * - outputColNames
        - Column Names for the CSV
        - New Output Columns of the SQL
      * - outputColTypes
        - Column Types for the CSV
        - Data Type of the Output Columns
      * - outputColFormats
        - Column Formats for the CSV
        - Format of the Output Columns




