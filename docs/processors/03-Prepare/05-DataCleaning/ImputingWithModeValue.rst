Imputing With Mode Value
=========== 

Imputing with most frequently observed value. It fills missing values (None) in selected columns with most frequently observed value in the corresponding column, in the incoming DataFrame.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeReplaceMissingValueWithMode

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - colNames
        - Columns
        - Columns to be processed for imputing the missing values.


Details
-------


This node imputes the missing values in the specified columns by mode of the values in the column.


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

If imputingwithmodevalue node is configured to Impute [AGE] with mode value then missing values in [AGE] column would be replaced with 30 which is the mode of [AGE] column.
Outgoing Dataframe would result as below:

CUST_CD    |    CUST_NAME    |    AGE
------------------------------------------
C01        |    MATT         |    50
C02        |    LISA         |    45
C03        |    ROBIN        |    30	
C04        |    MARCUS       |    30	
C05        |    MARK         |    30
C06        |    DAVID        |    30
C07        |    ANTHONY      |    90
