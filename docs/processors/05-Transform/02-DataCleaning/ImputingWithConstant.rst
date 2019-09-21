ImputingWithConstant
=========== 

It imputes missing value with constant value. It fills missing values (None) in selected columns with given constant value for the corresponding column, in the incoming DataFrame.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeReplaceMissingValueWithConstant

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
        - Columns to be processed for missing values
      * - constants
        - Constants
        - Missing value will be replaced with constant


Examples
---------

Input
--------------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - name
     - age
     - height
   
   * - Alice
     - 5
     - 80
     
   * - Alice
     - 5
     - 80
     
   * - Alice
     - 
     - 80
     
   * - James
     - 5
     - 50
     
   * - James
     - 
     - 60
    
   * - James
     - 
     - 80

Parameters1
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Columns
     - Constants
     
   * - name
     - 
     
   * - age
     - 20
   
   * - height
     - 


Output1
--------------

.. list-table:: 
   :widths: 10 20 10
   :header-rows: 1

   * - name
     - age
     - height
   
   * - Alice
     - 5
     - 80
     
   * - Alice
     - 5
     - 80
     
   * - Alice
     - 20
     - 80
     
   * - James
     - 5
     - 50
     
   * - James
     - 20
     - 60
    
   * - James
     - 20
     - 80
