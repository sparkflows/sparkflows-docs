Polynominal Expansion
=========== 

Perform feature expansion in a polynomial space

Input
--------------
It takes in a DataFrame and transforms it to another DataFrame

Output
--------------
The output DataFrame contains a new column of type vector, Expanding your features into a polynomial space, which is formulated by an n-degree combination of original dimensions.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodePolynominalExpansion

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
      * - degree
        - Degree
        - The polynomial degree to expand, which should be >= 1. A value of 1 means no expansion.


Details
-------


Polynomial expansion is the process of expanding your features into a polynomial space, which is formulated by an n-degree combination of original dimensions.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/2.0.0/ml-features.html#polynomialexpansion


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/ml-features.html#polynomialexpansion
+++++++++++++++

A PolynomialExpansion class provides this functionality. The example below shows how to expand your features into a 3-degree polynomial space.

import org.apache.spark.ml.feature.PolynomialExpansion
import org.apache.spark.ml.linalg.Vectors

val data = Array(
  Vectors.dense(-2.0, 2.3),
  Vectors.dense(0.0, 0.0),
  Vectors.dense(0.6, -1.1)
)
val df = spark.createDataFrame(data.map(Tuple1.apply)).toDF("features")
val polynomialExpansion = new PolynomialExpansion()
  .setInputCol("features")
  .setOutputCol("polyFeatures")
  .setDegree(3)
val polyDF = polynomialExpansion.transform(df)

polyDF.select("polyFeatures").take(3).foreach(println)
