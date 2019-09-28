JoinUsingColumns
=========== 

This node joins the incoming dataframes on 1 or more columns

Input
--------------
It takes in 2 DataFrames as input and produces one DataFrame as output by joining on the specified columns

Output
--------------
The output DataFrame produced as a result of joining the incoming DataFrames on the specified columns

Type
--------- 

join

Class
--------- 

fire.nodes.etl.NodeJoinUsingColumns

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - joinCols
        - Join Columns
        - Space separated list of columns on which to join
      * - joinType
        - Join Type
        - Type of Join
      * - outputColNames
        - Output Column Names
        - Name of the Output Columns
      * - outputColTypes
        - Output Column Types
        - Data Type of the Output Columns
      * - outputColFormats
        - Output Column Formats
        - Format of the Output Columns
      * - whereClause
        - Where Clause
        - where condition after join function

Input1
--------------

.. list-table:: 
   :widths: 10 30 30 30 30
   :header-rows: 1

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
   :widths: 10 30 30 30
   :header-rows: 1

   * - py_id
     - txid
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
   :widths: 20 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Join Column
     - txid
     
Refresh the Schema tab.

Output
--------

.. list-table:: 
   :widths: 10 10 20 10 10 20 10
   :header-rows: 1

   * - txid
     - py_id
     - item_id
     - date
     - amount
     - pay_type
     - amount

   * - 1001
     - 01
     - 0001
     - 2019-09-20
     - 100
     - credt_card
     - 60
  
   * - 1001
     - 01
     - 0001
     - 2019-09-20
     - 100
     - redme_coupon
     - 20
     
   * - 1001
     - 01
     - 0001
     - 2019-09-20
     - 100
     - redme_emp_offer
     - 20
     
   * - 1002
     - 02
     - 0001
     - 2019-09-20
     - 100
     - credt_card
     - 160
     
   * - 1002
     - 02
     - 0001
     - 2019-09-20
     - 100
     - redme_coupon
     - 40


