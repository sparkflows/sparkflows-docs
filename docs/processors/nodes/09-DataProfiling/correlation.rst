Correlation
=========== 

calculates the correlation between two series of data.

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
The input DataFrame is passed along to the next Processors

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeCorrelation

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
      * - inputCols
        - Input Column for Correlation
        - Column Names to check correlation 


Details
-------


This node calculates the correlation between two series of data in a common operation in Statistics.

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/mllib-statistics.html#correlations


