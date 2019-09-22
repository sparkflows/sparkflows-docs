StringFunctions
=========== 

This node performs specified String function on a row

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeStringFunctions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Column Name
        - input column name
      * - stringFunction
        - String Function
        - String Function Name
      * - replaceExistingCols
        - ReplaceExistingCols
        - replaceExistingCols


Examples
----------

Input
---------

.. list-table:: 
   :widths: 20 20 20
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
     - 10
     - 80
     
   * - James
     - 5
     - 50
     
   * - James
     - 10
     - 60
    
   * - James
     - 7
     - 80
     
     
Parameters
----------

.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column Name
     - name
     
   * - String Function
     - upper
     
   * - ReplaceExistingCols
     - true
        

Output
------

.. list-table:: 
   :widths: 20 10 10 10
   :header-rows: 1

   * - age
     - height
     - name
   
   * - 5
     - 80
     - ALICE
     
   * - 5
     - 80
     - ALICE
     
   * - 10
     - 80
     - ALICE
     
   * - 5
     - 50
     - JAMES
     
   * - 10
     - 60
     - JAMES
    
   * - 7
     - 80
     - JAMES
