Text Case Transformer
=========== 

This node converts the text of the selected column to upper or lower case

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeTextCaseTransformer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column Name
        - input column name
      * - mode
        - Text Case Type
        - Whether to convert the selected column to upper or lower case
      * - outputCol
        - Output Column
        - Output Column


Details
-------


This node converts text of the selected column to upper or lower case


Examples
-------



*  Input Column Name - Select required column to change the text type.
*  Text Case Type - Select the type (upper/lower) to change input column text type.
*  Output Column - Type new Column name to view the new result.
