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
        - Scale to be used when applying the Math Function




