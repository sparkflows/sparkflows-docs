ImputingWithModeValue
=========== 

Imputing with most frequently observed value. It fills missing values (None) in selected columns with most frequently observed value in the corresponding column, in the incoming DataFrame.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeReplaceMissingValueWithMode

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - colNames
        - Columns
        - Columns to be processed for imputing the missing values.


Examples
---------

Input
---------

.. list-table:: 
   :widths: 10 10
   :header-rows: 1

   * - id
     - amount
   
   * - 1
     - 100
  
   * - 2
     - 200
   
   * - 3
     - 
   
   * - 4
     - 400
     
   * - 5
     - 400
     
   * - 6
     - 400
    
   * - 7
     - 600
     
   * - 8
     - 700
    
Parameters
-------------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Columns
     - amount


Output
---------

.. list-table:: 
   :widths: 10 10
   :header-rows: 1

   * - id
     - amount
   
   * - 1
     - 100
  
   * - 2
     - 200
   
   * - 3
     - 400
   
   * - 4
     - 400
     
   * - 5
     - 400
     
   * - 6
     - 400
    
   * - 7
     - 600
     
   * - 8
     - 700

