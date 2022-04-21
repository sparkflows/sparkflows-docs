Filter By String Length
=========== 

This node filters the Rows within the given string length. The column to be used for determining the string length is specified

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFilterByStringLength

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column Name
        - input column name
      * - minLength
        - Minimum length
        - Minimum length of String
      * - maxLength
        - Maximum length
        - Maximum length of String


Details
-------


This node filters the Rows within the given string length range. 

The column to be used for determining the string length is specified.

New outgoing Dataframe is created based on filtered rows and it is passed to next node.


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

If FilterByStringLength node is configured as below:

INPUT COLUMN NAME    :    EMP_NAME
MINIMUM LENGTH       :    3
MAXIMUM LENGTH       :    5

then outgoing Dataframe would be created as below with the rows falling in the given string length range:

EMP_CD    |    EMP_NAME    |    DEPT    |    SALARY    |    AGE    
------------------------------------------------------------------------
E02       |    LISA        |    HR      |    50000     |    35
E04       |    DAVID       |    SALES   |    55000     |    40
E05       |    MARK        |    SALES   |    60000     |    45
E06       |    JOE         |    SALES   |    40000     |    25
E07       |    BELLA       |    HR      |    60000     |    24
