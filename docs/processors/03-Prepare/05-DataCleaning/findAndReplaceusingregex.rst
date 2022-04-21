Find And Replace Using Regex
=========== 

This node finds and replaces text in a column with another

Input
--------------
It accepts a DataFrame as input from the previous Node

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeFindAndReplaceUsingRegex

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
      * - searchPattern
        - Find
        - Enter Search Pattern
      * - replacePattern
        - Replace
        - Enter replacement Value


Details
-------


This node finds and replaces a string in a column with another one.

String can be a single character or a combination of words.


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

 if FindAndReplaceUsingRegex node is configured to find and replace [-] character in [DATE_OF_JOINING] column with [/]
+++++++++++++++
then outgoing Dataframe would be created as below after replacement of character:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE       |    DATE_OF_JOINING   |    SALARY       |    PERFORMANCE
---------------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25        |    2021/01/01        |    12 000.00    |    GOOD
E02       |    JOHN        |    SALES      |    35        |    2019/05/04        |    11 000.00    |    VERY GOOD
E03       |    MARTIN      |    MARKETING  |    40        |    2018/06/07        |    34 000       |    AVERAGE
E04       |    TONY        |    MARKETING  |    45        |    2017/02/01        |    12 500.00    |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25        |    2020/12/21        |    78 999.00    |    BAD

 if FindAndReplaceUsingRegex node is configured to find and replace [^VERY GOOD$] string in [PERFORMANCE] column with [EXCELLENT]
+++++++++++++++
where [^] denotes start of string and [$] denotes end of string
then outgoing Dataframe would be created as below after replacement of exact entry of [VERY GOOD] with [EXCELLENT] and not other entries:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE       |    DATE_OF_JOINING   |    SALARY       |    PERFORMANCE
---------------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25        |    2021-01-01        |    12 000.00    |    GOOD
E02       |    JOHN        |    SALES      |    35        |    2019-05-04        |    11 000.00    |    EXCELLENT
E03       |    MARTIN      |    MARKETING  |    40        |    2018-06-07        |    34 000       |    AVERAGE
E04       |    TONY        |    MARKETING  |    45        |    2017-02-01        |    12 500.00    |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25        |    2020-12-21        |    78 999.00    |    BAD

note that [VERY VERY GOOD] is not replaced as it is not an exact match.
