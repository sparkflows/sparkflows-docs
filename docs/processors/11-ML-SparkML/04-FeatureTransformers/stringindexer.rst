String Indexer
=========== 

StringIndexer encodes a string column of labels to a column of label indices

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
It adds a new column containing the encoding of the string column of labels to a column of label indices, to the incoming DataFrame.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeStringIndexer

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - handleInvalid
        - Handle Invalid
        - Invalid entries to be skipped or thrown error
      * - inputCols
        - Input Columns
        - Input columns for encoding
      * - outputCols
        - Output Columns
        - Output columns


Details
-------


StringIndexer encodes a string column of labels to a column of label indices. The indices are in [0, numLabels), ordered by label frequencies, so the most frequent label gets index 0.
If the input column is numeric, we cast it to string and index the string values.
                                                                                                  
More at Spark MLlib/ML docs page : https://spark.apache.org/docs/2.0.0/ml-features.html#stringindexer


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/ml-features.html#stringindexer
+++++++++++++++

import org.apache.spark.ml.feature.StringIndexer

val df = spark.createDataFrame(
  Seq((0, "a"), (1, "b"), (2, "c"), (3, "a"), (4, "a"), (5, "c"))
).toDF("id", "category")

val indexer = new StringIndexer()
  .setInputCol("category")
  .setOutputCol("categoryIndex")

val indexed = indexer.fit(df).transform(df)
indexed.show()
