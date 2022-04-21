Compare All Columns Single Output
=========== 

Compares 2 incoming DataFrames. Outputs 1 DataFrame (A-B) or (B-A) or (A intersection B) based on user's input

Type
--------- 

join

Class
--------- 

fire.nodes.etl.NodeCompareAllColumnsSingleOutput

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - compareOption
        - Compare Type
        - Comparision options whether (A-B) or (B-A) or (A intersection B)


Details
-------


This node takes two Dataframes as input and creates one outgoing Dataframes as an output based on the Compare Type selected to compare two incoming Dataframes.

If Compare Type is selected as LEFTDATAFRAME_EXCEPT_RIGHTDATAFRAME then outgoing Dataframe is created based on (A-B) 
and it consists of rows that are part of 1st incoming Dataframe but not present in 2nd Dataframe.

If Compare Type is selected as RIGHTDATAFRAME_EXCEPT_LEFTDATAFRAME then outgoing Dataframe is created based on (B-A) 
and it consists of rows that are part of 2nd incoming Dataframe but not present in 1st Dataframe.

If Compare Type is selected as LEFTDATAFRAME_INTERSECT_RIGHTDATAFRAME then outgoing Dataframe is created based on (A intersection B) 
and it consists of rows that are part of both incoming Dataframes.


Examples
-------


1st Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25     |    2021-01-01        |    12 000.00  |    GOOD
E02       |    JOHN        |    SALES      |    35     |    2019-05-04        |    11 000.00  |    VERY GOOD
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    34 000     |    AVERAGE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    12 500.00  |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25     |    2020-12-21        |    78 999.00  |    BAD

2nd Incoming Dataframe has following rows:

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    34 000     |    AVERAGE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    12 500.00  |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25     |    2020-12-21        |    78 999.00  |    BAD
E06       |    ROSS        |    SALES      |    35     |    2010-01-01        |    20 000.00  |    GOOD
E07       |    GAVIN       |    SALES      |    45     |    2020-05-04        |    10 000.00  |    VERY VERY GOOD

after execution of CompareAllColumnsSingleOutput node one of the below outgoing Dataframes would be created based on [Compare Type] selected:

 LEFTDATAFRAME_EXCEPT_RIGHTDATAFRAME (A-B) Outgoing Dataframe with rows that are part of 1st incoming Dataframe but not present in 2nd Dataframe
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25     |    2021-01-01        |    12 000.00  |    GOOD
E02       |    JOHN        |    SALES      |    35     |    2019-05-04        |    11 000.00  |    VERY GOOD

 RIGHTDATAFRAME_EXCEPT_LEFTDATAFRAME (B-A) Outgoing Dataframe with rows that are part of 2nd incoming Dataframe but not present in 1st Dataframe
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E06       |    ROSS        |    SALES      |    35     |    2010-01-01        |    20 000.00  |    GOOD
E07       |    GAVIN       |    SALES      |    45     |    2020-05-04        |    10 000.00  |    VERY VERY GOOD

 LEFTDATAFRAME_INTERSECT_RIGHTDATAFRAME (A insection B) Outgoing Dataframe with rows that are part of both incoming Dataframes
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    34 000     |    AVERAGE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    12 500.00  |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25     |    2020-12-21        |    78 999.00  |    BAD
