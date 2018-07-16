
Split By Expression
========== 

This node splits the incoming DataFrame into two output DataFrames by applying the conditional logic

Input
---------- 

It accepts a DataFrame as input from the previous Node

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeSplitByExpression

Fields
---------- 

+---------------+---------------------------------------------+------------------------------------------------------------------------+
| Name          | Title                                       | Description                                                            |
+===============+=============================================+========================================================================+
| conditionExpr | Conditional Expression to split the Data on | Conditional Expression to be used for Splitting the DataFrame into two |
+---------------+---------------------------------------------+------------------------------------------------------------------------+