
JoinUsingColumn
========== 

This node joins the incoming dataframes on a joinCol

Input
---------- 

This node takes in 2 DataFrames as input and produces one DataFrame as output

Output
---------- 

The output DataFrame is the result of joining the 2 incoming DataFrames on the join column

Type
---------- 

join

Class
---------- 

fire.nodes.etl.NodeJoinUsingColumn

Fields
---------- 

+---------+-------------+-------------------------+
| Name    | Title       | Description             |
+=========+=============+=========================+
| joinCol | Join Column | column on which to join |
+---------+-------------+-------------------------+