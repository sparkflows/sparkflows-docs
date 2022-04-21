Standard Scaler
=========== 

StandardScaler transforms a dataset of Vector rows, normalizing each feature to have unit standard deviation and/or zero mean.

Input
--------------
It takes in a DataFrame as input and transforms it to another DataFrame

Output
--------------
It adds a new column containing the transform of the input Vector column to unit standard deviation and/or zero mean features to the incoming DataFrame.

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeStandardScaler

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
      * - withMean
        - With Mean
        - Centers the data with mean before scaling.
      * - withStd
        - With Standard Dev
        - Scales the data to unit standard deviation


Details
-------


StandardScaler transforms a dataset of Vector rows, normalizing each feature to have unit standard deviation and/or zero mean. It takes parameters:


*  withStd: True by default. Scales the data to unit standard deviation.
*  withMean: False by default. Centers the data with mean before scaling. It will build a dense output, so take care when applying to sparse input.


StandardScaler is an Estimator which can be fit on a dataset to produce a StandardScalerModel; this amounts to computing summary statistics. The model can then transform a Vector column in a dataset to have unit standard deviation and/or zero mean features.

Note that if the standard deviation of a feature is zero, it will return default 0.0 value in the Vector for that feature.

More details are available at : http://spark.apache.org/docs/latest/ml-features.html#standardscaler


Examples
-------


The below example is available at : https://spark.apache.org/docs/latest/ml-features.html#standardscaler
+++++++++++++++


import org.apache.spark.ml.feature.StandardScaler

val dataFrame = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

val scaler = new StandardScaler()
  .setInputCol("features")
  .setOutputCol("scaledFeatures")
  .setWithStd(true)
  .setWithMean(false)

// Compute summary statistics by fitting the StandardScaler.
val scalerModel = scaler.fit(dataFrame)

// Normalize each feature to have unit standard deviation.
val scaledData = scalerModel.transform(dataFrame)
scaledData.show()
