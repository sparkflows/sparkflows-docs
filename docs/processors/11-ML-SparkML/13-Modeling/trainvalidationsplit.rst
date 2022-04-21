Train Validation Split
=========== 

This node represents Train Validation Split from Spark ML

Input
--------------
TrainValidationSplit takes an Estimator, a set of ParamMaps provided in the estimatorParamMaps parameter, and anEvaluator.

Output
--------------
The incoming DataFrame is passed to the output.

Type
--------- 

ml-trainvalidationsplit

Class
--------- 

fire.nodes.ml.NodeTrainValidationSplit

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - trainRatio
        - Train Ratio
        - Training Ratio


Details
-------


This node represents Train Validation Split from Spark ML.

In addition to CrossValidator Spark also offers TrainValidationSplit for hyper-parameter tuning. 
TrainValidationSplit only evaluates each combination of parameters once, as opposed to k times in the case of CrossValidator. 
It is, therefore, less expensive, but will not produce as reliable results when the training dataset is not sufficiently large.

Unlike CrossValidator, TrainValidationSplit creates a single (training, test) dataset pair. It splits the dataset into these two parts using the trainRatio parameter. 
For example with trainRatio=0.75, TrainValidationSplit will generate a training and test dataset pair where 75% of the data is used for training and 25% for validation.

Like CrossValidator, TrainValidationSplit finally fits the Estimator using the best ParamMap and the entire dataset.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/latest/ml-tuning.html#train-validation-split


Examples
-------

Below example is available at : https://spark.apache.org/docs/latest/ml-tuning.html#train-validation-split
+++++++++++++++

import org.apache.spark.ml.evaluation.RegressionEvaluator
import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.tuning.{ParamGridBuilder, TrainValidationSplit}

// Prepare training and test data.
val data = spark.read.format("libsvm").load("data/mllib/sample_linear_regression_data.txt")
val Array(training, test) = data.randomSplit(Array(0.9, 0.1), seed = 12345)

val lr = new LinearRegression()
    .setMaxIter(10)

// We use a ParamGridBuilder to construct a grid of parameters to search over.
// TrainValidationSplit will try all combinations of values and determine best model using
// the evaluator.
val paramGrid = new ParamGridBuilder()
  .addGrid(lr.regParam, Array(0.1, 0.01))
  .addGrid(lr.fitIntercept)
  .addGrid(lr.elasticNetParam, Array(0.0, 0.5, 1.0))
  .build()

// In this case the estimator is simply the linear regression.
// A TrainValidationSplit requires an Estimator, a set of Estimator ParamMaps, and an Evaluator.
val trainValidationSplit = new TrainValidationSplit()
  .setEstimator(lr)
  .setEvaluator(new RegressionEvaluator)
  .setEstimatorParamMaps(paramGrid)
  // 80% of the data will be used for training and the remaining 20% for validation.
  .setTrainRatio(0.8)
  // Evaluate up to 2 parameter settings in parallel
  .setParallelism(2)

// Run train validation split, and choose the best set of parameters.
val model = trainValidationSplit.fit(training)

// Make predictions on test data. model is the model with combination of parameters
// that performed best.
model.transform(test)
  .select("features", "label", "prediction")
  .show()
