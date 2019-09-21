ImputingWithMedian
=========== 

Imputing with median

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeReplaceMissingValueWithMedian

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - colNames
        - Input Columns
        - Input column of type - all numeric for median impute

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
     
   * - Input Columns
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
