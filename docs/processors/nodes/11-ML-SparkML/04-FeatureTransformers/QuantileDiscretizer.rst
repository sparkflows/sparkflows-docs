QuantileDiscretizer
=========== 

QuantileDiscretizer takes a column with continuous features and outputs a column with binned categorical features.

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
The output DataFrame contains a new column of binned categorical features.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeQuantileDiscretizer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column
        - The Input column name
      * - outputCol
        - Output Column
        - Output column name
      * - numBuckets
        - NumBuckets
        - Maximum number of buckets (quantiles or categories) into which the data points are grouped. Must be >= 2.


Details
-------


QuantileDiscretizer takes a column with continuous features and outputs a column with binned categorical features.


More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/ml-features.html#quantilediscretizer


