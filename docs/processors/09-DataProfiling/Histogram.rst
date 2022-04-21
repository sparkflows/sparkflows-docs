HistoGram
=========== 

Computes a histogram of the data using number of bins evenly spaced between the minimum and maximum of the specific columns.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeHistoGramCal

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - title
        - Title
        - Title
      * - inputCols
        - Column Name
        - Name of column
      * - bins
        - Number of Bins
        - Number of Bins


Details
-------


This node creates a histogram of the data using specified number of bins evenly spaced between the minimum and maximum of the specific columns.

It outputs a chart displaying histogram and bin details in tabular format.

Chart can be viewed in Column, Bar and Line format.


Examples
-------


Incoming Dataframe has following rows:

EMP_CD       |    EMP_NAME       |    DEPT       |    SALARY       |    AGE       |    DATE_OF_JOINING       |    EMAIL
------------------------------------------------------------------------------------------------------------------------------------
E01          |    ANTHONY        |    HR         |    50000        |    40        |    2019-12-12            |    anthony@hrdept.com
E02          |    LISA           |    HR         |    35000        |    35        |    2019-02-28            |    lisa@hrdept.com
E03          |    MARTIN         |    HR         |    20000        |    25        |    2020-01-01            |    martin@nodept.com
E04          |    DAVID          |    SALES      |    55000        |    40        |    2021-12-13            |    david@salesdept.com
E05          |    MARK           |    SALES      |    60000        |    27        |    2020-01-01            |    mark@salesdept.com
E06          |    JOE            |    SALES      |    40000        |    31        |    2010-01-01            |    joe@salesdept.com
E07          |    BELLA          |    HR         |    60000        |    24        |    2001-12-12            |    bella@hrdept.com
E08          |    ROSE           |    SALES      |    60000        |    27        |    2002-12-12            |    rose@hrdept.com
E09          |    MICHAEL        |    SALES      |    61000        |    31        |    2003-09-12            |    michael@hrdept.com
E10          |    PATRICK        |    HR         |    60000        |    24        |    2004-10-12            |    patrik@hrdept.com

if HistogramCal node is configured as below:

COLUMN NAME     :     SALARY
NUMBER OF BINS  :     10

then following equally spaced 10 bins would be created using MIN and MAX values of [SALARY] and same would be presented in Chart as well:

index    |   range                |    count
----------------------------------------------------------
1        |   20000.0 - 24100.0    |    1
2        |   24100.0 - 28200.0    |    0
3        |   28200.0 - 32300.0    |    0
4        |   32300.0 - 36400.0    |    1
5        |   36400.0 - 40500.0    |    1
6        |   40500.0 - 44600.0    |    0
7        |   44600.0 - 48700.0    |    0
8        |   48700.0 - 52800.0    |    1
9        |   52800.0 - 56900.0    |    1
10       |   56900.0 - 61000.0    |    5
