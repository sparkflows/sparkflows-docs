Min Max Scaler
=========== 

MinMaxScaler transforms a dataset of Vector rows, rescaling each feature to a specific range (often [0, 1])

Input
--------------
It takes in a DataFrame as input and transforms it to another DataFrame

Output
--------------
A new column containing the scaled features is added to the incoming DataFrame

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeMinMaxScaler

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
      * - max
        - Max
        - The upper bound after transformation, shared by all features
      * - min
        - Min
        - The lower bound after transformation, shared by all features


Details
-------


MinMaxScaler transforms a dataset of Vector rows, rescaling each feature to a specific range (often [0, 1]). It takes parameters:


*  min: 0.0 by default. Lower bound after transformation, shared by all features.
*  max: 1.0 by default. Upper bound after transformation, shared by all features.


MinMaxScaler computes summary statistics on a data set and produces a MinMaxScalerModel. The model can then transform each feature individually such that it is in the given range.

More details are available at : http://spark.apache.org/docs/latest/ml-features.html#minmaxscaler


Examples
-------


The below example is available at : https://spark.apache.org/docs/latest/ml-features.html#minmaxscaler
+++++++++++++++


import org.apache.spark.ml.feature.MinMaxScaler
import org.apache.spark.ml.linalg.Vectors

val dataFrame = spark.createDataFrame(Seq(
  (0, Vectors.dense(1.0, 0.1, -1.0)),
  (1, Vectors.dense(2.0, 1.1, 1.0)),
  (2, Vectors.dense(3.0, 10.1, 3.0))
)).toDF("id", "features")

val scaler = new MinMaxScaler()
  .setInputCol("features")
  .setOutputCol("scaledFeatures")

// Compute summary statistics and generate MinMaxScalerModel
val scalerModel = scaler.fit(dataFrame)

// rescale each feature to range [min, max].
val scaledData = scalerModel.transform(dataFrame)
println(s"Features scaled to range: [${scaler.getMin}, ${scaler.getMax}]")
scaledData.select("features", "scaledFeatures").show()
