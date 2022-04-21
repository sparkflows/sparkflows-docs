Concat Columns
=========== 

This node creates a new DataFrame by concatenating the specified columns of the input DataFrame

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new column is added to the incoming DataFrame by concatenating the specified columns. The new DataFrame is sent to the output of this Node.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeConcatColumns

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Columns
        - Columns to be concatenated
      * - outputCol
        - Concatenated Column Name
        - Column name for the concatenated columns
      * - sep
        - Separator
        - Separator to be used when concatenating the columns


Details
-------


It creates a new DataFrame by concatenating specified columns of the input DataFrame into a new column.

A new column is added to the incoming DataFrame by concatenating the specified columns. The new DataFrame is sent to the output of this Node.


Examples
-------


If incoming Dataframe has two columns [CUST_CD] and [CUST_NAME] which need to be concatenated to new column [CUST_IDENTIFIER] using separator [-] then output Dataframe would
be created as below:


*  CUST_CD : C001 
*  CUST_NAME : DAVID
*  CUST_IDENTIFIER : C001-DAVID 
