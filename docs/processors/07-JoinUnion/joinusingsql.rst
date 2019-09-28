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
   :header-rows: 1

   * - txid
     - itemid
     - date
     - pyid
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
   :widths: 10 30 30 30
   :header-rows: 1

   * - py_id
     - pay_txid
     - pay_type
     - amount
        
   * - 01
     - 1001
     - credt_card
     - 60
     
   * - 01
     - 1001
     - redme_coupon
     - 20
     
   * - 01
     - 1001
     - redme_emp_offer
     - 20
   
   * - 02
     - 1002
     - credt_card
     - 160
      
   * - 02
     - 1002
     - redme_coupon
     - 40
     

Parameters
------------

.. list-table:: 
   :widths: 20 70
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Temp Table1
     - transaction_temp_table
     
   * - Temp Table2
     - payment_temp_table
     
   * - SQL
     - select a.txid, a.itemid, a.date, a.pyid, a.amount as total_amount, b.pay_type, b.amount from transaction_temp_table a JOIN payment_temp_table b ON(a.txid = b.txid and a.py_id = b.pyid)
 
Refresh the Schema tab.

Output
--------

.. list-table:: 
   :widths: 10 10 20 10 20 10 10
   :header-rows: 1

   * - txid
     - itemid
     - date
     - pyid
     - total_amount
     - pay_type
     - amount

   * - 1001
     - 0001
     - 2019-09-20
     - 01
     - 100
     - credt_card
     - 60
  
   * - 1001
     - 0001
     - 2019-09-20
     - 01
     - 100
     - redme_coupon
     - 20
     
   * - 1001
     - 0001
     - 2019-09-20
     - 01
     - 100
     - redme_emp_offer
     - 20
     
   * - 1002
     - 0001
     - 2019-09-20
     - 02
     - 100
     - credt_card
     - 160
     
   * - 1002
     - 0001
     - 2019-09-20
     - 02
     - 100
     - redme_coupon
     - 40

