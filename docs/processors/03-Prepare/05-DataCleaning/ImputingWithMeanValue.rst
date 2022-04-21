Imputing With Mean Value
=========== 

Imputing the continuous variables by mean.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeReplaceMissingValueWithMean

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Column Names
        - Columns type should be continuous


Details
-------


This node imputes the missing values in the specified columns by mean of the values in the column.


Examples
-------


Incoming Dataframe has following rows and [AGE] column has missing value / [NULL] for some rows:

CUST_CD    |    CUST_NAME    |    AGE
-----------------------------------------
CD01       |    DAVID        |    30
CD02       |    MARY         |    40
CD03       |    PAUL         |			
CD04       |    MATT         |			

If imputingwithmeanvalue node is configured to Impute [AGE] with mean value then missing values in [AGE] column would be replaced with 35 which is the mean of [AGE] column.
Outgoing Dataframe would result as below:

CUST_CD    |    CUST_NAME    |    AGE
-----------------------------------------
CD01       |    DAVID        |    30
CD02       |    MARY         |    40
CD03       |    PAUL         |    35			
CD04       |    MATT         |    35			
