One Hot Encoder
=========== 

Maps a column of label indices to a column of binary vectors, with at most a single one-value

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
The output DataFrame contains a new column which contains the mapping of a column of label indices to a column of binary vectors, with at most a single one-value.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeOneHotEncoder

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCols
        - Input Columns
        - Input columns for encoding
      * - outputCols
        - Output Columns
        - Output columns


Details
-------


One-hot encoding maps a column of label indices to a column of binary vectors, with at most a single one-value. 
This encoding allows algorithms which expect continuous features, such as Logistic Regression, to use categorical features.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/2.0.0/ml-features.html#onehotencoder


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/ml-features.html#onehotencoder
+++++++++++++++

import org.apache.spark.ml.feature.{OneHotEncoder, StringIndexer}

val df = spark.createDataFrame(Seq(
  (0, "a"),
  (1, "b"),
  (2, "c"),
  (3, "a"),
  (4, "a"),
  (5, "c")
)).toDF("id", "category")

val indexer = new StringIndexer()
  .setInputCol("category")
  .setOutputCol("categoryIndex")
  .fit(df)
val indexed = indexer.transform(df)

val encoder = new OneHotEncoder()
  .setInputCol("categoryIndex")
  .setOutputCol("categoryVec")
val encoded = encoder.transform(indexed)
encoded.select("id", "categoryVec").show()
