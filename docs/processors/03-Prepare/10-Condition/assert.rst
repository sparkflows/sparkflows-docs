Assert
=========== 

This Node takes in an expression. It evaluates the expression and based on the results sends the execution to the first or the second output Node

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
The incoming DataFrame is sent to the output. Only one of the output Nodes receives the DataFrame based on the results of the expression

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeAssert

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - expression
        - Expression
        - Expression to be evaluated. It can use variables computed in the previous Nodes




