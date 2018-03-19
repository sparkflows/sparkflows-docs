
RemoveDuplicateRows
========== 

This node take an array of fields, compare rows on those fields. If they full match then its a match. From the matches it would randomly take one row and drop the rest.

Input
---------- 

It accepts a DataFrame as input from the previous Node

Output
---------- 

The output Dataframe is the same as the input Dataframe with the duplicate rows removed

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeRemoveDuplicateRows

Fields
---------- 

+-----------+---------+--------------------------------------+
| Name      | Title   | Description                          |
+===========+=========+======================================+
| inputCols | Columns | The columns to be selected for match |
+-----------+---------+--------------------------------------+