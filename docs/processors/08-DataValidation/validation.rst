Validate Fields Simple
=========== 

Validation Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeValidation

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
        - Validations being Performed
      * - inputCols
        - Columns
        - Columns
      * - functions
        - Function
        - Validation Function to apply
      * - values
        - Values
        - Values


Details
-------


This node creates two outgoing Dataframes based on the result of Validation Rules on the incoming Dataframe. 
First outgoing Dataframe consists of rows that succeeds the Validation Rules and second one consists of failed rows.   

This node facilitates checking of one condition in each rule.

Multiple validation rules can be defined for multiple columns. Succeeded and Failed Dataframes are created by applying all the validation rules on the incoming Dataframes.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD       |    EMP_NAME       |    DEPT       |    SALARY       |    AGE       |    DATE_OF_JOINING       |    EMAIL
------------------------------------------------------------------------------------------------------------------------------------
E01          |    ANTHONY        |    HR         |    50000        |    40        |    2020-12-12            |    anthony@hrdept.com
E02          |    LISA           |    HR         |    35000        |    35        |    2021-02-30            |    lisa@hrdept.com
E03          |    MARTIN         |    HR         |    20000        |    25        |    2020-01-01            |    martin@nodept.com
E04          |    DAVID          |    SALES      |    55000        |    40        |    2021-13-13            |    david@salesdept.com
E05          |    MARK           |    SALES      |    60000        |    27        |    2020-01-01            |    mark@salesdept.com
E06          |    JOE            |    SALES      |    40000        |    31        |    2010-01-01            |    joe@salesdept.com
E07          |    BELLA          |    HR         |    60000        |    24        |    2001-12-12            |    bella@hrdept.com

if following Validation Rules are defined in Validation node:

COLUMNS           |    FUNCTION                 |    VALUES 	
--------------------------------------------------------------------------
DATE_OF_JOINING   |    IS_VALID_DATE_FORMAT     |    yyyy-MM-dd
AGE               |    VALUE_LESS_THAN          |    36

then outgoing Dataframes would be created as below:

 Succeeded Dataframe consisting of rows that succeeded Validation Rules:
+++++++++++++++

EMP_CD       |    EMP_NAME       |    DEPT       |    SALARY       |    AGE       |    DATE_OF_JOINING       |    EMAIL
------------------------------------------------------------------------------------------------------------------------------------
E03          |    MARTIN         |    HR         |    20000        |    25        |    2020-01-01            |    martin@nodept.com
E05          |    MARK           |    SALES      |    60000        |    27        |    2020-01-01            |    mark@salesdept.com
E06          |    JOE            |    SALES      |    40000        |    31        |    2010-01-01            |    joe@salesdept.com
E07          |    BELLA          |    HR         |    60000        |    24        |    2001-12-12            |    bella@hrdept.com

 Failed Dataframe consisting of rows that failed Validation Rules:
+++++++++++++++

EMP_CD       |    EMP_NAME       |    DEPT       |    SALARY       |    AGE       |    DATE_OF_JOINING       |    EMAIL
------------------------------------------------------------------------------------------------------------------------------------
E01          |    ANTHONY        |    HR         |    50000        |    40        |    2020-12-12            |    anthony@hrdept.com
E02          |    LISA           |    HR         |    35000        |    35        |    2021-02-30            |    lisa@hrdept.com
E04          |    DAVID          |    SALES      |    55000        |    40        |    2021-13-13            |    david@salesdept.com
