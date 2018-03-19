
FilterByStringLength
========== 

This node filters the Rows within the given string length

Input
---------- 

It accepts a DataFrame as input from the previous Node

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeFilterByStringLength

Fields
---------- 

+-----------+-------------------+--------------------------+
| Name      | Title             | Description              |
+===========+===================+==========================+
| inputCol  | Input Column Name | input column name        |
+-----------+-------------------+--------------------------+
| minLength | Minimum length    | Minimum length of String |
+-----------+-------------------+--------------------------+
| maxLength | Maximum length    | Maximum length of String |
+-----------+-------------------+--------------------------+