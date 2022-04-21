String Functions Multiple
=========== 

String Functions Multiple

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeStringFunctionsMultiple

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - description
        - Description
        - Description
      * - inputCols
        - Columns
        - Columns
      * - functions
        - Function
        - String Function to apply
      * - replaceExistingCols
        - Replace Existing Cols
        - Whether to replace the existing columns or create new ones


Details
-------


This node creates a new Dataframe by transforming data of multiple columns using specified string functions.

In the output DataFrame, the input columns can either be replaced with the new value, or new columns created.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT                   
-------------------------------------------------------
E01       |    DAVID       |    HUMAN RESOURCE         
E02       |    JOHN        |    PRODUCT SALES          
E03       |    MARK        |    MARKETING MANAGEMENT   

if StringFunctionsMultiple node is configured to perform following transformations:

COLUMNS        |    FUNCTION          |      REPLACE EXISTING COLS 	
--------------------------------------------------------------------
EMP_NAME       |    lower             |      false
DEPT           |    removewhitespace  |      false

then outgoing Dataframe would be created as below after applying above transformations:

EMP_CD    |    EMP_NAME    |    DEPT                   |    EMP_NAME_lower    |    DEPT_removewhitespace             
-----------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HUMAN RESOURCE         |    david             |    HUMANRESOURCE
E02       |    JOHN        |    PRODUCT SALES          |    john              |    PRODUCTSALES
E03       |    MARK        |    MARKETING MANAGEMENT   |    mark              |    MARKETINGMANAGEMENT

Multiple transformations can be performed on a column; however, only the last transformation can have [REPLACE EXISTING COLS] option set as [true]
