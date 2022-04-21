Compare Specific Columns
=========== 

Compares 2 incoming DataFrames on specific columns. Outputs 1 DataFrame (A-B) or (B-A) or (A intersection B) based on user's input

Type
--------- 

join

Class
--------- 

fire.nodes.etl.NodeCompareSpecificColumnsSingleOutput

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - columnsToCompare
        - Columns to Compare
        - Columns to be used in the comparison
      * - compareOption
        - Compare Type
        - Comparision options whether (A-B) or (B-A) or (A intersection B)


Details
-------


This node takes two Dataframe as input, compares them on specific columns and creates one outgoing Dataframes as output 
based on the Compare Type selected to compare two incoming Dataframes.

If Compare Type is selected as LEFTDATAFRAME_EXCEPT_RIGHTDATAFRAME then outgoing Dataframe is created based on (A-B) and it consists of rows of 1st Dataframe 
in which values in the specified columns don't have matching entries in same set of columns in 2nd Dataframe.

If Compare Type is selected as RIGHTDATAFRAME_EXCEPT_LEFTDATAFRAME then outgoing Dataframe is created based on (B-A) and it consists of rows of 2nd Dataframe 
in which values in the specified columns don't have matching entries in same set of columns in 1st Dataframe.

If Compare Type is selected as LEFTDATAFRAME_INTERSECT_RIGHTDATAFRAME then outgoing Dataframe is created based on (A intersection B) and it consists of rows 
common in both incoming Dataframes in which values in the specified columns have matching entries in same set of columns.


Examples
-------


1st Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25     |    2021-01-01        |    12 000.00  |    GOOD
E02       |    JOHN        |    SALES      |    35     |    2019-05-04        |    11 000.00  |    VERY GOOD
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    34 000     |    AVERAGE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    12 500.00  |    VERY VERY GOOD
E05       |    MARK        |    SALES      |    25     |    2020-12-21        |    78 999.00  |    BAD

2nd Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    34 000     |    AVERAGE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    12 500.00  |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25     |    2020-12-21        |    78 999.00  |    BAD
E06       |    ROSS        |    FRONT DESK |    35     |    2010-01-01        |    20 000.00  |    GOOD
E07       |    GAVIN       |    MAINTENANCE|    45     |    2020-05-04        |    10 000.00  |    VERY VERY GOOD
E08       |    LISA        |    FRONT DESK |    40     |    2015-05-04        |    12 000.00  |    VERY GOOD

if CompareSpecificColumnsSingleOutput node is configured to compare incoming Dataframes on [DEPT] column 
then outgoing Dataframes would be created as below based on [Compare Type] selected:

 LEFTDATAFRAME_EXCEPT_RIGHTDATAFRAME (A-B) Outgoing Dataframe with rows of 1st Dataframe in which values in the specified columns 
+++++++++++++++
don't have matching entries in same set of columns in 2nd Dataframe.

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E02       |    JOHN        |    SALES      |    35     |    2019-05-04        |    11 000.00  |    VERY GOOD
E05       |    MARK        |    SALES      |    25     |    2020-12-21        |    78 999.00  |    BAD

 RIGHTDATAFRAME_EXCEPT_LEFTDATAFRAME (B-A) Outgoing Dataframe with rows of 2nd Dataframe in which values in the specified columns 
+++++++++++++++
don't have matching entries in same set of columns in 1st Dataframe.

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E06       |    ROSS        |    FRONT DESK |    35     |    2010-01-01        |    20 000.00  |    GOOD
E07       |    GAVIN       |    MAINTENANCE|    45     |    2020-05-04        |    10 000.00  |    VERY VERY GOOD
E08       |    LISA        |    FRONT DESK |    40     |    2015-05-04        |    12 000.00  |    VERY GOOD

 LEFTDATAFRAME_INTERSECT_RIGHTDATAFRAME (A insection B) Outgoing Dataframe with rows common in both incoming Dataframes in which values in the specified columns 
+++++++++++++++
have matching entries in same set of columns.

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25     |    2021-01-01        |    12 000.00  |    GOOD
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    34 000     |    AVERAGE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    12 500.00  |    VERY VERY GOOD
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    34 000     |    AVERAGE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    12 500.00  |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25     |    2020-12-21        |    78 999.00  |    BAD
