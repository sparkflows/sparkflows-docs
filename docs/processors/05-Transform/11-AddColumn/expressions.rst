Expressions
=========== 

Expressions

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeExpressions

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
      * - outputCols
        - New Columns Name
        - New Columns Name
      * - expressions
        - Expressions
        - Expressions

Functions Used in Expression: abs, acros, asin, atan, atan2, bin, cbrt, ceil, conv, cos, sosh, exp, expm1, factorial, floor, hex, hypot, log, log10, log1p, log2, pmod, pow, rint, round, shiftLeft, shiftRight, shiftRightUnsigned, signum, sin, sinh, sqrt, tan, tanh, toDegrees, toRadians, unhex


Input
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
   
   * - 4
     - 0.0
     - 4.1
     - -5.0
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
      
   * - 66
     - 1.0
     - 2.1
     - 2.0


Parameters
------------

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1
   
   * - id
     - New Columns Name
     - Expressions
     
   * - 1
     - sqrt_f1
     - sqrt(f1)

   * - 2
     - abs_f2
     - abs(f2)
     
     
output
--------

.. list-table:: 
   :widths: 20 20 20 20 40 10
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     - sqrt_f1
     - abs_f2
     
   * - 6
     - 1.0
     - 2.1
     - 2.0
     - 1.449137674618944
     - 2.0
   
   * - 4
     - 0.0
     - 4.1
     - -5.0
     - 2.0248456731316584
     - 5.0
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
     - 760681686165901 
     - 6.0
      
   * - 66
     - 1.0
     - 2.1
     - 2.0
     - 1.449137674618944 
     - 2.0
     
     
     
