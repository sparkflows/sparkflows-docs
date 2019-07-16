ConcatColumns
=========== 

This node creates a new DataFrame by concatenating the specified columns of the input DataFrame

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new column is added to the incoming DataFrame by concatenating the specified columns. The new DataFrame is sent to the output of this Node.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeConcatColumns

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Columns
        - Columns to be concatenated
      * - outputCol
        - Concatenated Column Name
        - Column name for the concatenated columns
      * - sep
        - Separator
        - Separator to be used when concatenating the columns




