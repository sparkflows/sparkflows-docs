Drop Columns
=========== 

This node creates a new DataFrame by deleting columns specified as an input

Input
--------------
It takes in a DataFrame as input

Output
--------------
The specified columns are dropped from the incoming DataFrame to generate the output DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDropColumns

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - dropCols
        - Columns
        - The columns to be excluded from the output DataFrame


Details
-------


This node creates a new DataFrame by deleting columns specified as an input.

The specified columns are dropped from the incoming DataFrame to generate the output DataFrame.


Examples
-------


If incoming Dataframe has following columns


*  CUST_CD
*  CUST_NAME
*  DOB
*  ADDRESS


and [DOB] and [ADDRESS] need to be dropped from outgoing Dataframe then add following to the Drop list in the Drop Column node:


*  DOB
*  ADDRESS
