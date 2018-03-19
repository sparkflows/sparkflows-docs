
RemoveUnwantedCharacters
========== 

This node removes unwanted characters

Input
---------- 

It accepts a DataFrame as input from the previous Node

Type
---------- 

transform

Class
---------- 

fire.nodes.etl.NodeRemoveUnwantedCharacters

Fields
---------- 

+-------------------+--------------------+---------------------+
| Name              | Title              | Description         |
+===================+====================+=====================+
| inputCols         | Input Columns      | Input columns       |
+-------------------+--------------------+---------------------+
| removeWhitespaces | Remove whitespaces | Removes white space |
+-------------------+--------------------+---------------------+
| removeLetters     | Remove letters     | Removes letters     |
+-------------------+--------------------+---------------------+
| removeDigits      | Remove digits      | Removes digits      |
+-------------------+--------------------+---------------------+
| removeSigns       | Remove signs       | Removes signs       |
+-------------------+--------------------+---------------------+
| removeCommas      | Remove commas      | Removes commas      |
+-------------------+--------------------+---------------------+