AFTSurvivalRegression
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


More at Spark MLlib/ML docs page : https://spark.apache.org/docs/latest/ml-classification-regression.html#survival-regression


