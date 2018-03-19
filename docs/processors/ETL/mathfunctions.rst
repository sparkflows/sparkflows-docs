
MathFuntions
========== 

This node performs specified math function on a row

Input
---------- 

It accepts a DataFrame as input from the previous Node

Output
---------- 

A new column is added which contains the results of applying the Math function on the given column of the input DataFrame

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeMathFuntions

Fields
---------- 

+--------------+-------------------+--------------------+
| Name         | Title             | Description        |
+==============+===================+====================+
| inputCol     | Input Column Name | input column name  |
+--------------+-------------------+--------------------+
| mathFunction | Math Function     | Math Function Name |
+--------------+-------------------+--------------------+
| outputCol    | Output Column     | Output Column Name |
+--------------+-------------------+--------------------+