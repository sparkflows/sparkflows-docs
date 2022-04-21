Compare All Columns
=========== 

Compares 2 incoming DataFrames. Outputs 3 DataFrames (A-B), (B-A), (A intersection B)

Type
--------- 

join

Class
--------- 

fire.nodes.etl.NodeCompareAllColumns

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description


Details
-------


This node takes two Dataframes as input and creates three Dataframes as output.

First Dataframe (A-B) is created with rows that are part of 1st incoming Dataframe but not present in 2nd Dataframe.

Second Dataframe (B-A) is created with rows that are part of 2nd incoming Dataframe but not present in 1st Dataframe.

Third Dataframe (A intersection B) is created with rows that are part of both incoming Dataframes.


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

after execution of CompareAllColumns node following three outgoing Dataframes would be created:

 (A-B) Outgoing Dataframe with rows that are part of 1st incoming Dataframe but not present in 2nd Dataframe
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E01       |    DAVID       |    HR         |    25     |    2021-01-01        |    12 000.00  |    GOOD
E02       |    JOHN        |    SALES      |    35     |    2019-05-04        |    11 000.00  |    VERY GOOD

 (B-A) Outgoing Dataframe with rows that are part of 2nd incoming Dataframe but not present in 1st Dataframe
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E06       |    ROSS        |    SALES      |    35     |    2010-01-01        |    20 000.00  |    GOOD
E07       |    GAVIN       |    SALES      |    45     |    2020-05-04        |    10 000.00  |    VERY VERY GOOD

 (A insection B) Outgoing Dataframe with rows that are part of both incoming Dataframes
+++++++++++++++

EMP_CD    |    EMP_NAME    |    DEPT       |    AGE    |    DATE_OF_JOINING   |    SALARY     |    PERFORMANCE
--------------------------------------------------------------------------------------------------------------------
E03       |    MARTIN      |    MARKETING  |    40     |    2018-06-07        |    34 000     |    AVERAGE
E04       |    TONY        |    MARKETING  |    45     |    2017-02-01        |    12 500.00  |    VERY VERY GOOD
E05       |    MARK        |    HR         |    25     |    2020-12-21        |    78 999.00  |    BAD
