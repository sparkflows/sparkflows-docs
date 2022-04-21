Binarizer
=========== 

Binarize a column of continuous features given a threshold.

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
A new column containing the binarized values is added to the incoming DataFrame

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeBinarizer

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
      * - threshold
        - Threshold
        - The features greater than the threshold, will be binarized to 1.0.The features equal to or less than the threshold, will be binarized to 0.0.


Details
-------


Binarization is the process of thresholding numerical features to binary (0/1) features.

Binarizer takes the common parameters inputCol and outputCol, as well as the threshold for binarization. 
Feature values greater than the threshold are binarized to 1.0; values equal to or less than the threshold are binarized to 0.0. 
Both Vector and Double types are supported for inputCol.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/latest/ml-features.html#binarizer


Examples
-------


Below example is available at : https://spark.apache.org/docs/latest/ml-features.html#binarizer

import org.apache.spark.ml.feature.Binarizer

val data = Array((0, 0.1), (1, 0.8), (2, 0.2))
val dataFrame = spark.createDataFrame(data).toDF("id", "feature")

val binarizer: Binarizer = new Binarizer()
  .setInputCol("feature")
  .setOutputCol("binarized_feature")
  .setThreshold(0.5)

val binarizedDataFrame = binarizer.transform(dataFrame)

println(s"Binarizer output with Threshold = ${binarizer.getThreshold}")
binarizedDataFrame.show()
