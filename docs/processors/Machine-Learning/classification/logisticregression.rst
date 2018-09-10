LogisticRegression
=========== 

Logistic regression. Currently, this class only supports binary classification.

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




