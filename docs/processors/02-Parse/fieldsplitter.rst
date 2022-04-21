Field Splitter
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
        - Input column name
      * - outputCols
        - Output Columns
        - New column names separated by comma (eg: col1,co2,col3)
      * - sep
        - Separator
        - Separator to split the input column value (default: space)
      * - onError
        - On Error
        - 


Details
-------


Splits the string of the specified input column using the specified delimiter. The new column names are specified by the user.

The new dataframe would have the new columns added to it.


Examples
-------


If a String Column stores values in [PRD_CD]:[PRD_NAME] format and incoming Dataframe has a value as CD01:DrillMachine 
then using : as Separator to split data into two Columns (Col1, Col2) would result in followings:


*  Col1 : CD01
*  Col2 : DrillMachine
