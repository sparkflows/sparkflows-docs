
Split
========== 

This node splits the incoming DataFrame into 2. It takes in the fraction to use in splitting the data. For example, if the fraction is .7, it would split the data into 2 DataFrames, one containing 70% of the rows and the other containing the remaining 30%.

Type
---------- 

transform

Class
---------- 

fire.nodes.ml.NodeSplit

Fields
---------- 

+-----------+------------+-------------+
| Name      | Title      | Description |
+===========+============+=============+
| fraction1 | Fraction 1 | None        |
+-----------+------------+-------------+