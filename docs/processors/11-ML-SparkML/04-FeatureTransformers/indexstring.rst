Index String
=========== 

Maps a column of indices back to a new column of corresponding string values. The index-string mapping is either from the ML attributes of the input column, or from user-supplied labels

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeIndexString

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
        - Column containing label indices
      * - outputCol
        - Output Column
        - Output column name


Details
-------


Symmetrically to StringIndexer, IndexToString maps a column of label indices back to a column containing the original labels as strings. 
A common use case is to produce indices from labels with StringIndexer, train a model with those indices and retrieve the original labels from the column of predicted indices with IndexToString.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/2.0.0/ml-features.html#indextostring


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/ml-features.html#indextostring
+++++++++++++++

import org.apache.spark.ml.feature.{IndexToString, StringIndexer}

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

val converter = new IndexToString()
  .setInputCol("categoryIndex")
  .setOutputCol("originalCategory")

val converted = converter.transform(indexed)
converted.select("id", "originalCategory").show()
