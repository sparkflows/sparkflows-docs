String Functions Multiple
=========== 

String Functions Multiple

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeStringFunctionsMultiple

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - description
        - Description
        - Description
      * - inputCols
        - Columns
        - Columns
      * - functions
        - Function
        - String Function to apply
      * - replaceExistingCols
        - Replace Existing Cols
        - Whether to replace the existing columns or create new ones


Details
-------


This node performs the specified string function on the selected input columns of the incoming DataFrame.

In the output DataFrame, the input columns can either be replaced with the new value, or new columns created.


