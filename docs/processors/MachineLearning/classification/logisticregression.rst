LogisticRegression
=========== 

Logistic regression. Currently, this class only supports binary classification.

Input
--------------
This takes in a DataFrame and performs Logistic Regression

Output
--------------
The Logistic Regression Model generated is passed along to the next nodes. The input DataFrame is also passed along to the next nodes

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeLogisticRegression

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
      * - probabilityCol
        - Probability Column
        - The column name for predicted class conditional probabilities
      * - predictionCol
        - Prediction Columns
        - The prediction column created during model scoring
      * - rawPredictionCol
        - Raw Prediction Column
        - The raw prediction (a.k.a. confidence) column name
      * - maxIter
        - Maximum Iterations
        - Maximum number of iterations (>= 0)
      * - fitIntercept
        - Fit Intercept
        - Whether to fit an intercept term
      * - regParam
        - Regularization Param
        - The regularization parameter
      * - standardization
        - Standardization
        - Whether to standardize the training features before fitting the model
      * - threshold
        - Threshold
        - The threshold in binary classification prediction
      * - tol
        - Tolerance
        - The convergence tolerance for iterative algorithms
      * - elasticNetParam
        - ElasticNet Param
        - The ElasticNet mixing parameter. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty
      * - weightCol
        - Weight Column
        - If the 'weight column' is not specified, all instances are treated equally with a weight 1.0
      * - gridSearch
        - Grid Search
      * - regParamGrid
        - Regularization Param Grid Search
        - Regularization Parameters for Grid Search
      * - elasticNetGrid
        - ElasticNet Param Grid Search
        - ElasticNet Parameters for Grid Search


Details
======


Logistic regression is a popular method to predict a categorical response. 

It is a special case of Generalized Linear models that predicts the probability of the outcomes. 
In spark.ml logistic regression can be used to predict a binary outcome by using binomial logistic regression, or it can be used to predict a multiclass outcome by using multinomial logistic regression.

More details are available at : https://spark.apache.org/docs/2.3.0/ml-classification-regression.html#logistic-regression


Examples
======


The below example is available at : https://spark.apache.org/docs/2.3.0/ml-classification-regression.html#logistic-regression
+++++++++++++++


import org.apache.spark.ml.classification.LogisticRegression

// Load training data
val training = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

val lr = new LogisticRegression()
  .setMaxIter(10)
  .setRegParam(0.3)
  .setElasticNetParam(0.8)

// Fit the model
val lrModel = lr.fit(training)

// Print the coefficients and intercept for logistic regression
println(s"Coefficients: ${lrModel.coefficients} Intercept: ${lrModel.intercept}")

// We can also use the multinomial family for binary classification
val mlr = new LogisticRegression()
  .setMaxIter(10)
  .setRegParam(0.3)
  .setElasticNetParam(0.8)
  .setFamily("multinomial")

val mlrModel = mlr.fit(training)

// Print the coefficients and intercepts for logistic regression with multinomial family
println(s"Multinomial coefficients: ${mlrModel.coefficientMatrix}")
println(s"Multinomial intercepts: ${mlrModel.interceptVector}")
