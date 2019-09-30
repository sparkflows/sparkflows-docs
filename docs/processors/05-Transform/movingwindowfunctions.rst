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

Parameters
------------


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
     
   * - price
     - rms
    
    
Output
-------

.. list-table:: 
   :widths: 10 10 10 10 30 20 20 20 20 20 20 20 20 20 20 20
   :header-rows: 1

   * - year 
     - month
     - date
     - symbol
     - temp
     - price
     - mean_price 
     - min_price
     - max_price
     - stddev_price
     - variance_price
     - skewness_price
     - kurtosis_price
     - cv_price
     - range_price
     - rms_price
     
   * - 2015
     - 9
     - 4
     - ADP
     - 305378
     - 76.15
     - 79.08999999999999
     - 77.8
     - 81.55
     - 2.131267228669365
     - 4.542299999999995
     - 0.7045857353865611
     - -1.500000000000001
     - 0.026947366654056965
     - 3.75
     - 45.673684253991745
     
   * - 2015
     - 8
     - 26
     - ADP
     - 591184
     - 77.8 
     - 77.29
     - 76.15
     - 77.92
     - 0.989090491310071
     - 0.9782999999999976
     - -0.6954155301207766
     - -1.4999999999999987
     - 0.012797134057576282
     - 1.769999999999996
     - 44.625838180737105
   
   * - 2015
     - 9
     - 10
     - ADP
     - 467863
     - 77.92
     - 79.08999999999999
     - 77.8
     - 81.55
     - 2.131267228669365
     - 4.542299999999995
     - 0.7045857353865611
     - -1.500000000000001
     - 0.026947366654056965
     - 3.75
     - 45.673684253991745
     
   * - 2015
     - 8
     - 14
     - ADP
     - 194911
     - 82.99 
     - 82.27
     - 81.55
     - 82.99
     - 1.0182337649086268
     - 1.0367999999999968
     - 0.0
     - -2.0000000000000018
     - 0.012376732282832465
     - 1.4399999999999977
     - 58.1759026573718 
     
     

