
DropColumns
========== 

This node creates a new DataFrame by deleting columns specified as an input

Input
---------- 

It takes in a DataFrame as input

Output
---------- 

The specified columns are dropped from the incoming DataFrame to generate the output DataFrame

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeDropColumns

Fields
---------- 

+----------+---------+------------------------------------------------------+
| Name     | Title   | Description                                          |
+==========+=========+======================================================+
| dropCols | Columns | The columns to be excluded from the output DataFrame |
+----------+---------+------------------------------------------------------+