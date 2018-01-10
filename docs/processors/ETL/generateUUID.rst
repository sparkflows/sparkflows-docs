
GenerateUUID
========== 

This node Generates a universally unique ID

Input
---------- 

It accepts a DataFrame as input

Output
---------- 

It adds a new column for UUID to the input DataFrame. This new DataFrame is sent to the output.

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeGenerateUUID

Fields
---------- 

+-----------+---------------+------------------------+
| Name      | Title         | Description            |
+===========+===============+========================+
| prefix    | Prefix        | Prefix to add in UUID  |
+-----------+---------------+------------------------+
| postfix   | Postfix       | Postfix to add in UUID |
+-----------+---------------+------------------------+
| outputCol | Output Column | Output Column Name     |
+-----------+---------------+------------------------+