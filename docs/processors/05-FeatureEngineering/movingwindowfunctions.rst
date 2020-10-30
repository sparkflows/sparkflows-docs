MovingWindowFunctions
=========== 

This node calculates the moving values of selected functions for the field(input column).

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new columns is added which contains the results of applying the selected function on the given column of the input DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMovingWindowFunctions

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - windowStart
        - Window Start
        - value to be used to calculate the window from
      * - windowEnd
        - Window End
        - value to be used to calculate the window to
      * - partitionCol
        - Partition Column Name
        - partition column to split the incoming dataframe for the sliding/window operation
      * - orderCol
        - Order Column Name
        - the order of the selected column for the sliding/window operation
      * - inputCols
        - Input Columns
        - input column name for calc
      * - functions
        - Functions
        - 




