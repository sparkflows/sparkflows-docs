Distinct Values In Column
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeDistinctValues

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - distinctCols
        - Column Names
        - Name of columns to get the distinct combination of values.


Details
-------


This node displays distinct combination of values in the selected columns. 

If only one column is selected then it displays Distinct values present in that column. 
If more than one column is selected then it displays distinct combination of values present in the selected columns.


Examples
-------


If DistinctValuesInColumn node is configured to display distinct values in [Location] and [Dept] columns from incoming dataset
then outgoing Dataframe would be created in tabular format displaying unique combination of data between the selected columns.
