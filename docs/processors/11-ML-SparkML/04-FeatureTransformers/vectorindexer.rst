Vector Indexer
=========== 

Vector Indexer indexes categorical features inside of a Vector. It decides which features are categorical and converts them to category indices. The decision is based on the number of distinct values of a feature.

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
It indexes categorical features in datasets of Vectors and stores the result into a new column of the DataFrame.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeVectorIndexer

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
      * - maxCategories
        - Maximum Categories
        - Threshold for the number of values a categorical feature can take. If a feature is found to have > maxCategories values, then it is declared continuous. Must be >= 2


Details
-------


VectorIndexer helps index categorical features in datasets of Vectors. It can both automatically decide which features are categorical and convert original values to category indices.
More details are available at: https://spark.apache.org/docs/2.0.0/ml-features.html#vectorindexer


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/ml-features.html#vectorindexer
+++++++++++++++

import org.apache.spark.ml.feature.VectorIndexer

val data = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

val indexer = new VectorIndexer()
  .setInputCol("features")
  .setOutputCol("indexed")
  .setMaxCategories(10)

val indexerModel = indexer.fit(data)

val categoricalFeatures: Set[Int] = indexerModel.categoryMaps.keys.toSet
println(s"Chose ${categoricalFeatures.size} categorical features: " +
  categoricalFeatures.mkString(", "))

// Create new column "indexed" with categorical values transformed to indices
val indexedData = indexerModel.transform(data)
indexedData.show()
