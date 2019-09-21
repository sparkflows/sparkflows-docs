MathFunctions
=========== 

This node performs specified math function on a row

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new column is added which contains the results of applying the Math function on the given column of the input DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMathFuntions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column Name
        - input column name
      * - mathFunction
        - Math Function
        - Math Function Name
      * - outputCol
        - Output Column
        - Output Column Name
      * - scale
        - Scale
        - Scale to be used when applying the Math Functions pow & round function.


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
     - age
     
   * - Math Function
     - pow
     
   * - Output Column
     - pow_age
     
   * - Scale
     - 2


Output
------

.. list-table:: 
   :widths: 20 10 10 10
   :header-rows: 1

   * - name
     - age
     - height
     - pow_age
   
   * - Alice
     - 5
     - 80
     - 25.0
     
   * - Alice
     - 5
     - 80
     - 25.0
     
   * - Alice
     - 10
     - 80
     - 100.0
     
   * - James
     - 5
     - 50
     - 25.0
     
   * - James
     - 10
     - 60
     - 100.0
    
   * - James
     - 7
     - 80
     - 49.0
