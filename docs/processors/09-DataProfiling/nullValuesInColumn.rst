Null Values In Column
=========== 

Number of Null Values in Selected Columns.

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeNullValuesInColumn

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
        - Name of columns for Number of Null Values Check


Details
-------


This node identifies number of Null values and its percentage against the total data length in the selected columns.


Examples
-------


A set of columns can be selected to display count of Null values on.

If NullValuesInColumn node is configured to display count of Null values in [EMP_CD], [EMP_NAME], [DEPT] and [AGE] columns from the incoming dataset

then outgoing Dataframe would be created as below displaying count of Null values in each column and it's percentage.
