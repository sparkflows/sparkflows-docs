MovingAvergae
=========== 

This node calculates the moving average of given field(column).

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new column is added which contains the results of calculation of Moving Average on the given column of the input DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMovingAverage

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
        - input column name for moving average calc
      * - partitionCol
        - Partition Column Name
        - partition column name
      * - orderCol
        - Order Column Name
        - Order column name
      * - windowFrom
        - Window From
        - value to be used to calculate the window from
      * - windowTo
        - Window To
        - value to be used to calculate the window to




