StringFunctionsMultiple
=========== 

String Functions Multiple

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeStringFunctionsMultiple

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - description
        - Description
        - Description
      * - inputCols
        - Columns
        - columns
      * - functions
        - Function
        - String Function to apply
      * - replaceExistingCols
        - Replace Existing Cols
        - Replace Existing Columns (true or false)


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
-------------

.. list-table:: 
   :widths: 10 25 25 25
   :header-rows: 1

   * - Id
     - Columns
     - Function
     - Replace Existing Cols
   
   * - 1
     - name
     - upper
     - false
     
   * - 2
     - name
     - lower
     - false
     
 Output
---------

.. list-table:: 
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - name
     - age
     - height
     - name_upper
     - name_lower
     
   * - Alice
     - 5
     - 80
     - ALICE
     - alice
     
   * - Alice
     - 5
     - 80
     - ALICE
     - alice
     
   * - Alice
     - 10
     - 80
     - ALICE
     - alice
     
   * - James
     - 5
     - 50
     - JAMES
     - james
     
   * - James
     - 10
     - 60
     - JAMES
     - james
    
   * - James
     - 7
     - 80
     - JAMES
     - james
  
