
CastColumnType
========== 

This node creates a new DataFrame by casting input columns with a new data type

Input
---------- 

This type of node takes in a DataFrame and transforms it to another DataFrame

Output
---------- 

This node casts the data type of columns as specified

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeCastColumnType

Fields
---------- 

+---------------+---------------+-----------------------------------------------------+
| Name          | Title         | Description                                         |
+===============+===============+=====================================================+
| inputCols     | Columns       | Columns to be cast to new data type                 |
+---------------+---------------+-----------------------------------------------------+
| outputColType | New Data Type | New data type(INTEGER, DOUBLE, STRING, LONG, SHORT) |
+---------------+---------------+-----------------------------------------------------+