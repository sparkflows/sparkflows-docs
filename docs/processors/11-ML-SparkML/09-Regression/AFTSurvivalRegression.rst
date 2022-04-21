AFT Survival Regression
=========== 

Accelerated failure time (AFT) model which is a parametric survival regression model for censored data.

Output
--------------
It generates the LAFTSurvivalRegressionModel and passes it to the next Predict and ModelSave Nodes. The input DataFrame is also passed along to the next nodes.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeAFTSurvivalRegression

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - featuresCol
        - Features Column
        - Features column of type vectorUDT for model fitting
      * - labelCol
        - Label Column
        - The label column for model fitting
      * - censorCol
        - Censor Column
        - Indicator of the event has occurred or not. If the value is 1.O, it means the event has occurred i.e. uncensored; otherwise censored
      * - fitIntercept
        - Fit Intercept
        - Whether to fit an intercept term
      * - maxIter
        - Maximum Iterations
        - Maximum number of iterations (>= 0)
      * - tol
        - Tolerance
        - The convergence tolerance for iterative algorithms
      * - quantileProbabilities
        - QuantileProbabilities
        - Values of the quantile probabilities array should be in the range (0, 1)
      * - quantilesCol
        - Quantiles Column
        - The quantiles column created during model scoring
      * - predictionCol
        - Prediction Column
        - The prediction column created during model scoring


Details
-------


Apache Spark ML implements the Accelerated failure time (AFT) model which is a parametric survival regression model for censored data. It describes a model for the log of survival time, so it’s often called a log-linear model for survival analysis. Different from a Proportional hazards model designed for the same purpose, the AFT model is easier to parallelize because each instance contributes to the objective function independently.

More details can be found at Spark MLlib/ML docs page : https://spark.apache.org/docs/latest/ml-classification-regression.html#survival-regression


Examples
-------


Below example is available at : https://spark.apache.org/docs/latest/ml-classification-regression.html#survival-regression

import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.regression.AFTSurvivalRegression

val training = spark.createDataFrame(Seq(
  (1.218, 1.0, Vectors.dense(1.560, -0.605)),
  (2.949, 0.0, Vectors.dense(0.346, 2.158)),
  (3.627, 0.0, Vectors.dense(1.380, 0.231)),
  (0.273, 1.0, Vectors.dense(0.520, 1.151)),
  (4.199, 0.0, Vectors.dense(0.795, -0.226))
)).toDF("label", "censor", "features")
val quantileProbabilities = Array(0.3, 0.6)
val aft = new AFTSurvivalRegression()
  .setQuantileProbabilities(quantileProbabilities)
  .setQuantilesCol("quantiles")

val model = aft.fit(training)

// Print the coefficients, intercept and scale parameter for AFT survival regression
println(s"Coefficients: ${model.coefficients}")
println(s"Intercept: ${model.intercept}")
println(s"Scale: ${model.scale}")
model.transform(training).show(false)
