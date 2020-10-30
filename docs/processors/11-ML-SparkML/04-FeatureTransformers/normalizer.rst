Normalizer
=========== 

Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm.

Input
--------------
It  takes in a DataFrame and transforms it to another DataFrame

Output
--------------
It adds a new column containing the normalized value of the input column, to the incoming DataFrame.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeNormalizer

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
        - The input column name
      * - outputCol
        - Output Column
        - The output column name
      * - p
        - P
        - Normalization in L^p space. Must be >= 1. (default: p = 2)


Details
-------


Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm.

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/ml-features.html#normalizer


