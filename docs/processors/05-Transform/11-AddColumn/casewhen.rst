CaseWhen
=========== 

Sets values based on conditions

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeCaseWhen

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - outputCol
        - Output Column Name
        - output column name
      * - whenConditions
        - When Condition
        - When Condition
      * - values
        - Value
        - Value when this condition is true
      * - finallyElse
        - Else
        - else
    
Examples
----------

Input
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
     

Parameters
------------

.. list-table:: 
   :widths: 60 20
   :header-rows: 1
   
   * - When Condition
     - Value
     
   * - amount >= 100.0 and amount < 200.0
     - "high_value"
     
   * - amount >=200.0
     - "very_high_value"
     
.. list-table:: 
   :widths: 20 30
   :header-rows: 1    
   
   * - Name
     - Value
     
   * - Output Column Name
     - transaction_type
     
   * - Else
     - "low-value"
     
Output
--------------

.. list-table:: 
   :widths: 10 30 30 30 30
   :header-rows: 1

   * - txid
     - itemid
     - date
     - pyid
     - amount
     - transaction_type
   
   * - 1001
     - 0001
     - 2019-09-20
     - 01
     - 100
     - high_value

   * - 1002
     - 0001
     - 2019-09-20
     - 02
     - 100
     - high_value

