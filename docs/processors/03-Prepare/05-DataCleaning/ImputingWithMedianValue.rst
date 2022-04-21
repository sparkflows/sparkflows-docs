Imputing With Median
=========== 

Imputing with median

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeReplaceMissingValueWithMedian

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - colNames
        - Input Columns
        - Input column of type - all numeric for median impute


Details
-------


This node imputes the missing values in the specified columns by median of the values in the column.


Examples
-------


Incoming Dataframe has following rows and [AGE] column has missing value / [NULL] for some rows:

CUST_CD    |    CUST_NAME    |    AGE
------------------------------------------
C01        |    MATT         |    50
C02        |    LISA         |    45
C03        |    ROBIN        |	
C04        |    MARCUS       |	
C05        |    MARK         |    30
C06        |    DAVID        |    30
C07        |    ANTHONY      |    90

If imputingwithmedianvalue node is configured to Impute [AGE] with median value then missing values in [AGE] column would be replaced with 45 which is the median of [AGE] column.
Outgoing Dataframe would result as below:

CUST_CD    |    CUST_NAME    |    AGE
------------------------------------------
C01        |    MATT         |    50
C02        |    LISA         |    45
C03        |    ROBIN        |    45	
C04        |    MARCUS       |    45	
C05        |    MARK         |    30
C06        |    DAVID        |    30
C07        |    ANTHONY      |    90
