Find And Replace Using Regex Multiple
=========== 

This node finds and replaces text in a column containing string

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFindAndReplaceUsingRegexMultiple

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Columns
        - Columns on which to apply Regex
      * - searchPatterns
        - Find
        - Enter Search Pattern
      * - replacePatterns
        - Replace
        - Enter replacement Value


Details
-------


This node finds and replaces text in a column containing string with another one.

String can be a single character or a combination of words.

In this node multiple find and replace conditions can be entered for one or multiple columns in one go. 

Outgoing Dataframe would be created after processing of all conditions.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE       |    DATE_OF_JOINING   |    SALARY       |    PERFORMANCE
---------------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25        |    2021-01-01        |    12 000.00    |    GOOD
E02       |    JOHN        |    SALES      |    35        |    2019-05-04        |    11 000.00    |    VERY GOOD
E03       |    MARTIN      |    MARKETING  |    40        |    2018-06-07        |    34 000       |    AVERAGE
E04       |    TONY        |    MARKETING  |    45        |    2017-02-01        |    12 500.00    |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25        |    2020-12-21        |    78 999.00    |    BAD

if FindAndReplaceUsingRegexMultiple node is configured as below:

INPUT COLUMNS    |   FIND    |    REPLACE 	
----------------------------------------------
DATE_OF_JOINING  |   \-      |    \/
SALARY           |   \s      |    ,
PERFORMANCE      |   BAD     |    NOT SO GOOD

then outgoing Dataframe would be created as below
after replacement of occurrence of [-] with [/] in [DATE_OF_JOINING] column
and  replacement of occurrence of [SPACES] with [,] in [SALARY]
and  replacement of occurrence of [BAD] with [NOT SO GOOD] in [PERFORMANCE] column:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE       |    DATE_OF_JOINING   |    SALARY       |    PERFORMANCE
---------------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25        |    2021/01/01        |    12,000.00    |    GOOD
E02       |    JOHN        |    SALES      |    35        |    2019/05/04        |    11,000.00    |    VERY GOOD
E03       |    MARTIN      |    MARKETING  |    40        |    2018/06/07        |    34,000       |    AVERAGE
E04       |    TONY        |    MARKETING  |    45        |    2017/02/01        |    12,500.00    |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25        |    2020/12/21        |    78,999.00    |    NOT SO GOOD
