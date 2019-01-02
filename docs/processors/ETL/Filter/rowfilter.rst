RowFilter
=========== 

This node creates a new DataFrame containing only rows satisfying given condition

Input
--------------
It accepts DataFrame as input from the previous Node

Output
--------------
This node filters the rows based on the conditional expression to generate the output DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeRowFilter

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - conditionExpr
        - Conditional Expression
        - The filtering condition. Rows not satisfying given condition will be excluded from output DataFrame


Details
======


This node creates a new DataFrame containing only rows satisfying the given condition.

Examples of Conditional Expression
+++++++++++++++

col1 > 5 AND col2 > 3

name is not NULL

name is NULL

datetime > '2011-01-01 00:00:00.0'     (datetime column is of type timestamp)

datetime > '2011-01-01 00:00:00.0' and datetime < '2016-01-01 00:00:00.0'


