Binary Classification Evaluator
=========== 

Evaluator for binary classification, which expects two input columns: rawPrediction and label.

Output
--------------
It outputs the Probability for each class

Type
--------- 

ml-evaluator

Class
--------- 

fire.nodes.ml.NodeBinaryClassificationEvaluator

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - labelCol
        - Label Column
        - The label column for model fitting.
      * - predictionCol
        - Prediction Column
        - The prediction column.
      * - metricName
        - Metric Name
        - The metric used in evaluation.


Details
-------


Evaluator for binary classification, which expects two input columns: rawPrediction and label.


More at Spark MLlib/ML docs page : http://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#binary-classification


Examples
-------

Below example is available at : https://spark.apache.org/docs/latest/mllib-evaluation-metrics.html#binary-classification
+++++++++++++++

import org.apache.spark.mllib.classification.LogisticRegressionWithLBFGS
import org.apache.spark.mllib.evaluation.BinaryClassificationMetrics
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.util.MLUtils

// Load training data in LIBSVM format
val data = MLUtils.loadLibSVMFile(sc, "data/mllib/sample_binary_classification_data.txt")

// Split data into training (60%) and test (40%)
val Array(training, test) = data.randomSplit(Array(0.6, 0.4), seed = 11L)
training.cache()

// Run training algorithm to build the model
val model = new LogisticRegressionWithLBFGS()
  .setNumClasses(2)
  .run(training)

// Clear the prediction threshold so the model will return probabilities
model.clearThreshold

// Compute raw scores on the test set
val predictionAndLabels = test.map { case LabeledPoint(label, features) =>
  val prediction = model.predict(features)
  (prediction, label)
}

// Instantiate metrics object
val metrics = new BinaryClassificationMetrics(predictionAndLabels)

// Precision by threshold
val precision = metrics.precisionByThreshold
precision.collect.foreach { case (t, p) =>
  println(s"Threshold: $t, Precision: $p")
}

// Recall by threshold
val recall = metrics.recallByThreshold
recall.collect.foreach { case (t, r) =>
  println(s"Threshold: $t, Recall: $r")
}

// Precision-Recall Curve
val PRC = metrics.pr

// F-measure
val f1Score = metrics.fMeasureByThreshold
f1Score.collect.foreach { case (t, f) =>
  println(s"Threshold: $t, F-score: $f, Beta = 1")
}

val beta = 0.5
val fScore = metrics.fMeasureByThreshold(beta)
fScore.collect.foreach { case (t, f) =>
  println(s"Threshold: $t, F-score: $f, Beta = 0.5")
}

// AUPRC
val auPRC = metrics.areaUnderPR
println(s"Area under precision-recall curve = $auPRC")

// Compute thresholds used in ROC and PR curves
val thresholds = precision.map(_._1)

// ROC Curve
val roc = metrics.roc

// AUROC
val auROC = metrics.areaUnderROC
println(s"Area under ROC = $auROC")
