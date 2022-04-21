Cast To Different Types-1
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

fire.nodes.etl.NodeMultiCastColumnType

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


Details
-------


This node creates a new DataFrame by casting the specified columns into new types.

Option to replace existing column or create a new column after conversion can be selected in the node. 


Examples
-------


Incoming Dataframe has following rows:

INV_NO    |    INV_DATE          |    INV_AMT       
----------------------------------------------------
STRING    |    STRING            |    STRING       
----------------------------------------------------
INV001    |    2010-12-28        |    1000.0        
INV002    |    2020-10-15        |    1500.0        
INV003    |    2010-01-01        |    100.0         

if MultiCastColumnType node is configured to perform conversions as below:

COLUMNS    |    NEW DATA TYPE    |    REPLACE EXISTING COLS 	
--------------------------------------------------------------
INV_DATE   |    DATE             |    false
INV_DATE   |    LONG             |    false

then new columns would be added in outgoing Dataframe as below after conversion:

INV_NO    |    INV_DATE          |    INV_AMT       |    INV_DATE-new  |    INV_AMT-new       
------------------------------------------------------------------------------------------
STRING    |    STRING            |    STRING        |    DATE          |    LONG       
------------------------------------------------------------------------------------------
INV001    |    2010-12-28        |    1000.0        |    2010-12-28    |    1000        
INV002    |    2020-10-15        |    1500.0        |    2020-10-15    |    1500        
INV003    |    2010-01-01        |    100.0         |    2010-01-01    |    100        
