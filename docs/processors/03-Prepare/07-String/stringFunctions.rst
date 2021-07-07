String Functions
=========== 

This node performs the specified string function on the selected input columns of the incoming DataFrame

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeStringFunctions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Column Name
        - input column name
      * - stringFunction
        - String Function
        - String Function Name to be applied to the selected columns
      * - replaceExistingCols
        - ReplaceExistingCols
        - Whether to replace the existing columns or create new ones


Details
-------


This node performs the specified string function on the selected input columns of the incoming DataFrame.

In the output DataFrame, the input columns can either be replaced with the new value, or new columns created.


