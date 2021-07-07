Remove Duplicate Rows
=========== 

This node take an array of fields and compare the rows on those fields. From the matches it would randomly take one row and drop the rest.

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
The output Dataframe is the same as the input Dataframe with the duplicate rows removed

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeRemoveDuplicateRows

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - order
        - Order
        - Whether to take the first or last matching record when removing duplicates
      * - inputCols
        - Columns
        - The columns to be selected for match


Details
-------


This node take an array of fields and compares the rows on those fields.

From the matches it would randomly take one row and drop the rest


