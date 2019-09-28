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


Input1
--------------

.. list-table:: 
   :widths: 10 30 30 30 30
   :header-rows: 2

   * - txid
     - item_id
     - date
     - py_id
     - amount
   
   * - 1001
     - 0001
     - 2019-09-20
     - 01
     - 100

   * - 1002
     - 0001
     - 2019-09-20
     - 02
     - 100
     

Input2
--------------

.. list-table:: 
   :widths: 10 50 50
   :header-rows: 2

   * - id
     - date_string
     - date_string1
     
   * - IntegerType
     - StringType
     - StringType 
   
   * - 0
     - 2011-1-1 00:00:00.0
     - 05/26/2016 01:01:01
   
   * - 1
     - 2012-1-14 01:00:00.0
     - 06/22/2017 01:00:00
   
   * - 2
     - 2013-12-10 02:00:00.0
     - 01/12/2016 01:01:01
     
Parameters
------------

.. list-table:: 
   :widths: 40 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - date_string
     
   * - Input Column Format
     - yyyy-MM-dd HH:mm:ss
     
   * - Output Column Name
     - unix_time
 

Output
--------

.. list-table:: 
   :widths: 10 50 50 30
   :header-rows: 1

   * - id
     - date_string
     - date_string1
     - unix_time
   
   * - 0
     - 2011-1-1 00:00:00.0
     - 05/26/2016 01:01:01
     - 1293840000
   
   * - 1
     - 2012-1-14 01:00:00.0
     - 06/22/2017 01:00:00
     - 1326502800
   
   * - 2
     - 2013-12-10 02:00:00.0
     - 01/12/2016 01:01:01
     - 1386640800


