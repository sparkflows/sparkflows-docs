Cast To Single Type
=========== 

This node creates a new DataFrame by casting the specified input columns to a new data type

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
This node casts the data type of selected columns to the specified data type

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeCastColumnType

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Columns
        - Columns to be cast to new data type
      * - outputColType
        - New Data Type
        - New data type for the selected columns (INTEGER, DOUBLE, STRING, LONG, SHORT)
      * - replaceExistingCols
        - Replace Existing Cols?
        - Whether to replace existing columns or create new ones?


Details
-------


This node creates a new DataFrame by casting the specified input columns to a new data type. All the selected columns would be cast to the specified data type.

The boolean field Replace Existing Columns indicates whether the existing column should be replaced or a new column should be created.


Examples
-------


If incoming Dataframe has following columns with below specified datatype:


*  CUST_ID : Integer
*  CUST_NAME : String
*  DOB : Datetime
*  AGE : Integer


and [DOB] and [AGE] are selected for casting to [STRING] datatype then outgoing Dataframe would have below datatypes:


*  CUST_ID : Integer
*  CUST_NAME : String
*  DOB : String
*  AGE : String
