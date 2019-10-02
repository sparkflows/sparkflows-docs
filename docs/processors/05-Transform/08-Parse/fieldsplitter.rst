FieldSplitter
=========== 

This node splits the string of the specified input column using the specified delimiter

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
New columns are added to the incoming DataFrame with values from the result of splitting the value in the input column

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFieldSplitter

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column
        - input column name
      * - outputCols
        - Output Columns
        - new column names separed by comma','.(eg: col1,co2,col3)
      * - sep
        - Separator
        - separator to split the input column value(default: space)
      * - onError
        - On Error
        - 

Examples
---------

Input
--------------

.. list-table:: 
   :widths: 50 30
   :header-rows: 2

   * - date_of_payment
     - total_amount
   
   * - StringType
     - DoubleType
     
   * - 12/17/2013
     - 113.48
     
   * - 12/4/2013
     - 119.49
     
   * - 12/16/2013
     - 12.01
  
   * - 10/22/2013 
     - 10.61
   
   
Parameters
----------


.. list-table:: 
   :widths: 10 10
   :header-rows: 1
   
   * - Name
     - Value
     
   * - Input Column
     - date_of_payment
     
   * - Separator
     - /
     
   * - Output Columns
     - month,date,year


Output
----------

.. list-table:: 
   :widths: 50 30 20 20 20
   :header-rows: 2

   * - date_of_payment
     - total_amount
     - month
     - date
     - year
   
   * - StringType
     - DoubleType
     - StringType
     - StringType
     - StringType
     
   * - 12/17/2013
     - 113.48
     - 12
     - 17
     - 2013
     
   * - 12/4/2013
     - 119.49
     - 12
     - 4
     - 2013
     
   * - 12/16/2013
     - 12.01
     - 12
     - 16
     - 2013
  
   * - 10/22/2013 
     - 10.61
     - 10
     - 22
     - 2013
     

