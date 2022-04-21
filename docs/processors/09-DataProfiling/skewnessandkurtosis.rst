Skewness And Kurtosis
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeSkewnessAndKurtosis

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
        - Name of columns to get the skewness and kurtosis.


Details
-------


This node identifies Skewness (measure of symmetry) and Kurtosis (measure of whether the data are heavy-tailed or light-tailed relative to a normal distribution) in the selected columns.

More than one numeric column can be selected.


Examples
-------


A set of columns from incoming dataset can be selected.

If SkewnessAndKurtosis node is configured to compute values for [Salary]

then outgoing Dataframe would contain Skewness and Kurtosis values for the selected column:


*  Skewness : 2.112
*  Kurtosis : 2.802
