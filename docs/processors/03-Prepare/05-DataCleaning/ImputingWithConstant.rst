Imputing With Constant
=========== 

It imputes missing value with constant value. It fills missing values (None) in selected columns with given constant value for the corresponding column, in the incoming DataFrame.

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeReplaceMissingValueWithConstant

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
        - Columns to be processed for missing values
      * - constants
        - Constants
        - Missing value will be replaced with constant


Details
-------


This node imputes the missing value with constant value.

It fills missing values (None) in selected columns with given constant value for the corresponding column, in the incoming DataFrame.


Examples
-------


Incoming Dataframe has following rows and [AGE] column has missing values / [NULL] for some rows:

CUST_CD    |    CUST_NAME    |    AGE
-----------------------------------------
CD01       |    DAVID        |    30
CD02       |    MARY         |    40
CD03       |    PAUL         |			
CD04       |    MATT         |			

If imputingwithconstatnt node is configured to Impute [AGE] with 45 then missing values in [AGE] column would be replaced with 45.
Outgoing Dataframe would result as below:

CUST_CD    |    CUST_NAME    |    AGE
-----------------------------------------
CD01       |    DAVID        |    30
CD02       |    MARY         |    40
CD03       |    PAUL         |    45			
CD04       |    MATT         |    45			
