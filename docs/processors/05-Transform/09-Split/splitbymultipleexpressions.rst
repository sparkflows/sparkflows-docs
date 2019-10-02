SplitByMultipleExpressions
=========== 

Splits the incoming DataFrame into multiple output DataFrames by applying the conditional logic

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeSplitByMultipleExpressions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - conditionExpr1
        - Conditional Expression 1 to split the Data on
        - Conditional Expression 1 to be used for Splitting the Dataset
      * - conditionExpr2
        - Conditional Expression 2 to split the Data on
        - Conditional Expression 2 to be used for Splitting the Dataset
      * - conditionExpr3
        - Conditional Expression 3 to split the Data on
        - Conditional Expression 3 to be used for Splitting the Dataset
      * - conditionExpr4
        - Conditional Expression 4 to split the Data on
        - Conditional Expression 4 to be used for Splitting the Dataset
      * - conditionExpr5
        - Conditional Expression 5 to split the Data on
        - Conditional Expression 5 to be used for Splitting the Dataset


Examples
---------

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
     - 5.0
     
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
   :widths: 60 30
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Conditional Expression 1 to split the Data on
     - id <= 4
     
   * - Conditional Expression 2 to split the Data on
     - id > 4 AND id <= 5

   * - Conditional Expression 3 to split the Data on
     - id > 5 AND id <= 6
     
   * - Conditional Expression 4 to split the Data on
     - id > 12 AND id <= 30
 

Output1
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
   
   * - 4
     - 0.0
     - 4.1
     - 5.0



Output2
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2
     
   * - 5
     - 0.0
     - 3.1
     - 6.0
      
     
Output3
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
    


Output4
--------

.. list-table:: 
   :widths: 20 20 20 20
   :header-rows: 1

   * - id
     - label
     - f1
     - f2


   EMPTY
