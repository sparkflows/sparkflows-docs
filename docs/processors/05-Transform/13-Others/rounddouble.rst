RoundValue
=========== 



Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeRoundDouble

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Column
        - The columns containing double or float values to round.
      * - precision
        - Precision
        - The scale of the double values to round to.

Examples
---------

Input
--------

.. list-table:: 
   :widths: 50 50 50
   :header-rows: 1

   * - V1
     - V2
     - V3
     
   * - 1.1032154353
     - -0.040296215
     - 1.2673320886
   
   * - -0.41428881
     - 0.9054373226
     - 1.7274529442
     
   * - 1.1140085954
     - 0.0855460897
     - 0.4937024874
      
   * - -0.291540245
     - 0.4455753137
     - 1.2497521162



Parameters
------------

.. list-table:: 
   :widths: 20 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column
     - V1 V2
     
   * - Precision
     - 2


Output
--------

.. list-table:: 
   :widths: 50 50 50
   :header-rows: 1

   * - V3
     - V1
     - V2
     
   * - 1.2673320886
     - 1.1 
     - -0.04
   
   * - 1.7274529442
     - -0.41
     - 0.91
     
   * - 0.4937024874
     - 1.11
     - 0.09
      
   * - 1.2497521162
     - -0.29 
     - 0.45
     
     
