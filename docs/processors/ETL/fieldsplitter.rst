
FieldSplitter
========== 

This node splits the string at specified delimiter

Input
---------- 

It accepts a DataFrame as input from the previous Node

Output
---------- 

New columns are added to the incoming DataFrame with values from the result of splitting the value in the input column

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeFieldSplitter

Fields
---------- 

+------------+----------------+-----------------------------------------------------------+
| Name       | Title          | Description                                               |
+============+================+===========================================================+
| inputCol   | Input Column   | input column name                                         |
+------------+----------------+-----------------------------------------------------------+
| outputCols | Output Columns | new column names separed by comma','.(eg: col1,co2,col3)  |
+------------+----------------+-----------------------------------------------------------+
| sep        | Separator      | separator to split the input column value(default: space) |
+------------+----------------+-----------------------------------------------------------+
| onError    | On Error       |                                                           |
+------------+----------------+-----------------------------------------------------------+