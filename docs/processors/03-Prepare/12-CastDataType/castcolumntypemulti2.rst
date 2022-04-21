Cast To Different Types-2
=========== 

This node creates a new DataFrame by casting the specified columns into new types

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
This node casts the data type of columns as specified

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeMultiCastColumnType2

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputColNames
        - Columns
        - Columns
      * - outputColTypes
        - New Data Type
        - New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)
      * - replaceExistingCols
        - Replace Existing Cols
        - Whether to replace existing Columns or create New Ones
      * - formats
        - Formats
        - Formats like yyy-MM-dd used in input & output


Details
-------


This node creates a new DataFrame by casting the specified columns into new types.

Option to replace existing column or create a new column after conversion can be selected in the node. 

New format for the Date column can be specified.


Examples
-------


Incoming Dataframe has following rows:

INV_NO    |    INV_DATE               |    INV_AMT       
----------------------------------------------------
STRING    |    timestamp              |    STRING       
----------------------------------------------------
INV001    |    2010-12-28 10:11:12.0  |    1000.0        
INV002    |    2020-10-15 09:11:12.0  |    1500.0        
INV003    |    2010-01-01 10:11:12.0  |    100.0         

if MultiCastColumnType2 node is configured to perform conversion as below:

COLUMNS    |    NEW DATA TYPE    |    REPLACE EXISTING COLS    |    FORMATS 	
-----------------------------------------------------------------------------------
INV_DATE   |    STRING           |    false                    |    yyyy/MMM/dd

then new column would be added in outgoing Dataframe as below after conversion:

INV_NO    |    INV_DATE               |    INV_AMT    |    INV_DATE-new       
-------------------------------------------------------------------------------  
STRING    |    timestamp              |    STRING     |    STRING    
-------------------------------------------------------------------------------
INV001    |    2010-12-28 10:11:12.0  |    1000.0     |    2010/Dec/28        
INV002    |    2020-10-15 09:11:12.0  |    1500.0     |    2020/Oct/15        
INV003    |    2010-01-01 10:11:12.0  |    100.0      |    2010/Jan/01        
