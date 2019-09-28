JoinUsingColumn
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
        - Join Column
        - column on which to join


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
   :widths: 10 10 20 10 10 10 20 10
   :header-rows: 1

   * - txid
     - item_id
     - date
     - py_id
     - amount
     - py_id
     - pay_type
     - amount

   * - 1001
     - 0001
     - 2019-09-20
     - 01
     - 100
     - 01
     - credt_card
     - 60
  
   * - 1001
     - 0001
     - 2019-09-20
     - 01
     - 100
     - 01
     - redme_coupon
     - 20
     
   * - 1001
     - 0001
     - 2019-09-20
     - 01
     - 100
     - 01
     - redme_emp_offer
     - 20
     
   * - 1002
     - 0001
     - 2019-09-20
     - 02
     - 100
     - 02
     - credt_card
     - 160
     
   * - 1002
     - 0001
     - 2019-09-20
     - 02
     - 100
     - 02
     - redme_coupon
     - 40
     
