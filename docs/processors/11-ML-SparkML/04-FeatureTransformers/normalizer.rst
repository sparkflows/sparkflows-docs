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


Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm. It takes parameter p, which specifies the p-norm used for normalization. (p=2 by default.)
This normalization can help standardize your input data and improve the behavior of learning algorithms.

More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/ml-features.html#normalizer


Examples
-------


The below example is available at : http://spark.apache.org/docs/latest/ml-features.html#normalizer
+++++++++++++++

import org.apache.spark.ml.feature.Normalizer

val dataFrame = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

// Normalize each Vector using $L^1$ norm.
val normalizer = new Normalizer()
  .setInputCol("features")
  .setOutputCol("normFeatures")
  .setP(1.0)

val l1NormData = normalizer.transform(dataFrame)
l1NormData.show()

// Normalize each Vector using $L^\infty$ norm.
val lInfNormData = normalizer.transform(dataFrame, normalizer.p -> Double.PositiveInfinity)
lInfNormData.show()
