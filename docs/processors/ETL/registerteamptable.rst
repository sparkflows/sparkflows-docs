
RegisterTempTable
========== 

This node registers the incoming DataFrame as a temporary table in Spark

Input
---------- 

It accepts a DataFrame as input from the previous Node

Output
---------- 

The incoming DataFrame is output without any changes

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeRegisterTempTable

Fields
---------- 

+-----------+-----------------+-------------------------------------------+
| Name      | Title           | Description                               |
+===========+=================+===========================================+
| tempTable | Temporary Table | Name of the temporary table to be created |
+-----------+-----------------+-------------------------------------------+