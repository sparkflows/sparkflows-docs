LinearRegression
=========== 



Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeLinearRegression

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
      * - predictionCol
        - Prediction Column
        - The prediction column created during model scoring
      * - fitIntercept
        - Fit Intercept
        - Whether to fit an intercept term
      * - maxIter
        - Maximum Iterations
        - Maximum number of iterations (>= 0)
      * - regParam
        - Regularization Param
        - The regularization parameter
      * - elasticNetParam
        - ElasticNet Param
        - The ElasticNet mixing parameter. For alpha = 0, the penalty is an L2 penalty. For alpha = 1, it is an L1 penalty
      * - solver
        - Solver
        - The solver algorithm for optimization
      * - standardization
        - Standardization
        - Whether to standardize the training features before fitting the model
      * - tol
        - Tolerance
        - The convergence tolerance for iterative algorithms
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
      * - maxIterGrid
        - MaxIter Param Grid Search
        - Maximum iteration Parameters for Grid Search




