MathFunctionsMultiple
=========== 

Math Functions Multiple

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMathFunctionsMultiple

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
        - Columns
      * - functions
        - Function
        - Math Function to apply
      * - replaceExistingCols
        - Replace Existing Cols
        - Replace Existing Columns (true, false)
      * - scales
        - Scale
        - Scale to be used when applying the Math Function


Examples
----------

Input
---------

.. list-table:: 
   :widths: 20 20 20
   :header-rows: 2

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
   :widths: 10 25 25 25 25
   :header-rows: 1

   * - Id
     - Columns
     - Function
     - Replace Existing Cols
     - Scale
   
   * - 1
     - age
     - pow
     - true
     - 2
     
  *  - 2
     - height
     - sqrt
     - false
     - 
   
   
Output
---------

.. list-table:: 
   :widths: 20 20 20 40
   :header-rows: 1

   * - name
     - height
     - age
     - height_sqrt
     
   * - Alice
     - 80
     - 25.0
     - 8.94427190999916
     
   * - Alice
     - 80
     - 25.0
     - 8.94427190999916
     
   * - Alice
     - 80
     - 100.0
     - 8.94427190999916
     
   * - James
     - 50
     - 25.0
     - 7.0710678118654755
     
   * - James
     - 60
     - 100.0
     - 7.745966692414834
    
   * - James
     - 80
     - 49.0
     - 8.94427190999916
