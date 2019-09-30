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


Examples
---------

Input
--------------

.. list-table:: 
   :widths: 10 10 10 10 30 20
   :header-rows: 1

   * - year 
     - month
     - date
     - symbol
     - temp
     - price
     
   * - 2015
     - 9
     - 4
     - ADP
     - 305378
     - 76.15
     
   * - 2015
     - 8
     - 26
     - ADP
     - 591184
     - 77.8 
      
   * - 2015
     - 9
     - 10
     - ADP
     - 467863
     - 77.92
     
   * - 2015
     - 8
     - 12
     - ADP
     - 209928
     - 81.55
     
   * - 2015
     - 8
     - 14
     - ADP
     - 194911
     - 82.99 

Parameters1
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Window Start
     - -1
     
   * - Window End
     - 1
    
   * - Order Column Name
     - 
    
   * - Partition Column Name
     - symbol  


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Input Columns
     - Functioms
    
   * - price
     - avg
    
   * - price
     - min
    
   * - price
     - max
   
   * - price
     - stddev
    
   * - price
     - variance
    
   * - price
     - skewness
    
   * - price
     - kurtosis
    
   * - price
     - coefficient_of_variation
    
   * - price
     - range
    
    



