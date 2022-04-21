Moving Window Functions
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


Details
-------


This node Generates a new Dataframe with Moving Window Function based computed Column appended to the incoming Dataframe.

New Column is populated with value based on selected Moving Window Function applied on the selected column.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    
------------------------------------------------------------------------
E01       |    ANTHONY     |    HR      |    50000     |    40
E02       |    LISA        |    HR      |    50000     |    35
E03       |    MARTIN      |    HR      |    20000     |    25
E04       |    DAVID       |    SALES   |    55000     |    40
E05       |    MARK        |    SALES   |    60000     |    45
E06       |    JOE         |    SALES   |    40000     |    25
E07       |    BELLA       |    HR      |    60000     |    24

If MovingWindowFunctions node is configured as below:

WINDOW START           :     -1
WINDOW END             :     1
PARTITION COLUMN NAME  :     DEPT
ORDER COLUMN NAME      :     SALARY
INPUT COLUMNS          :     SALARY
FUNCTIONS              :     AVG

Where window for each row is created from 1 row preceeding it upto 1 row succeeding it. 
The current incoming Dataframe is partition by [DEPT] and data is sorted by [SALARY].
New column created would be populated with [AVG] of [SALARY] for rows present in a window within a partition.
Outgoing Dataframe would be created as below :

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    |    mean_SALARY
---------------------------------------------------------------------------------------
E03       |    MARTIN      |    HR      |    20000     |    25     |    35000.0
E01       |    ANTHONY     |    HR      |    50000     |    40     |    40000.0
E02       |    LISA        |    HR      |    50000     |    35     |    53333.333
E07       |    BELLA       |    HR      |    60000     |    24     |    55000.0
E06       |    JOE         |    SALES   |    40000     |    25     |    47500.0
E04       |    DAVID       |    SALES   |    55000     |    40     |    51666.667
E05       |    MARK        |    SALES   |    60000     |    45     |    57500.0
