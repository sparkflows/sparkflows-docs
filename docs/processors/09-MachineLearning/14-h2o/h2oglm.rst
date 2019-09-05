H2OGLM
=========== 

H2O GLM

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2OGlm

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - response_column
        - Response Column
        - 
      * - isResponseIsCategorical
        - isResponseColIsCategorical
        - Specify a response column type(numeric or categorical). Separates the Classification and Regression
      * - offset_column
        - Offset Column
        - Specify a column to use as the offset; the value cannot be the same as the value for the weights_column
      * - weights_column
        - Weights Column
        - Specify a column to use for the observation weights, which are used for bias correction (The specified weights_column must be included in the specified training_frame)
      * - ignore_const_cols
        - Ignore Const Colst
        - Enable to ignore constant training columns
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be excluded from the model (Optional, Python and Flow only)
      * - nfolds
        - NFolds
        - Specify the number of folds for cross-validation
      * - fold_column
        - Fold Column
        - Specify the column that contains the cross-validation fold index assignment per observation
      * - early_stopping
        - Early Stopping
        - Specify whether to stop early when there is no more relative improvement on the training or validation set
      * - remove_collinear_columns
        - Remove Collinear Columns
        - Specify whether to automatically remove collinear columns during model-building
      * - max_iterations
        - Max Iterations
        - Specify the number of training iterations
      * - interactions
        - Interactions
        - Specify a list of predictor column indices to interact
      * - distribution_family
        - Distribution Family
        - Specify the model type
      * - seed
        - Seed
        - Specify the random number generator (RNG) seed for algorithm components dependent on randomization
      * - advanced
        - Advanced
      * - alpha
        - Alpha
        - Specify the regularization distribution between L1 and L2
      * - compute_p_values
        - Compute P Values
        - Request computation of p-values. Only applicable with no penalty (lambda = 0 and no beta constraints)
      * - custom_metric_func
        - Custom Metric Func
        - specify a custom evaluation function (Optional)
      * - distribution
        - Distribution
        - specifies a probability distribution from an exponential family
      * - hl
        - hl
      * - beta_epsilon
        - Epsilon : Beta Epsilon
        - Specify the beta epsilon value (If the L1 normalization of the current beta change is below this threshold, consider using convergence)
      * - gradient_epsilon
        - Epsilon : Gradient Epsilon
        - Specify a threshold for convergence (For L-BFGS only)
      * - objective_epsilon
        - Epsilon : Objective Epsilon
        - Specify a threshold for convergence. If the objective value is less than this threshold, the model is converged
      * - hl
        - hl
      * - intercept
        - Intercept
        - Specify whether to include a constant term in the model (This option is enabled by default)
      * - hl
        - hl
      * - family default
        - Link
        - it Specify the model type
      * - fold_assignment
        - Fold Assignment
        - Specify the cross-validation fold assignment scheme (Applicable only if a value for nfolds is specified and fold_column is not specified)
      * - keep_cross_validation_fold_assignment
        - Keep CV Fold Assignment
        - Enable to preserve the cross-validation fold assignment
      * - keep_cross_validation_predictions
        - Keep CV Predictions
        - Specify whether to keep the cross-validation predictions
      * - hl
        - hl
      * - lambda
        - Lambda
        - Specify the regularization strength
      * - lambda_min_ratio
        - Lambda Min Ratio
        - Specify the minimum lambda to use for lambda search (specified as a ratio of lambda_max, which is the smallest λ for which the solution is all zeros)
      * - lambda_search
        - Lambda Search
        - Specify whether to enable lambda search, starting with lambda max (the smallest λ that drives all coefficients to zero)
      * - nlambdas
        - Nlambdas
        - Specify the number of lambdas to use in the search (Applicable only if lambda_search is enabled)
      * - hl
        - hl
      * - missing_values_handling
        - Missing Values Handling
        - Specify how to handle missing values (Skip or MeanImputation)
      * - non_negative
        - Non Negative
        - Specify whether to force coefficients to have non-negative values
      * - solver
        - Solver
        - Specify the solver to use (AUTO, IRLSM, L_BFGS, COORDINATE_DESCENT_NAIVE, COORDINATE_DESCENT, GRADIENT_DESCENT_LH, or GRADIENT_DESCENT_SQERR)
      * - standardize
        - Standardize
        - Specify whether to standardize the numeric columns to have a mean of zero and unit variance
      * - theta
        - Theta
        - Theta value (equal to 1/r) for use with the negative binomial family, This value must be > 0 and defaults to 1e-10
      * - hl
        - hl
      * - max_active_predictors
        - Max Active Predictors
        - Specify the maximum number of active predictors during computation
      * - obj_reg
        - Obj Reg
        - Specify the likelihood divider in objective value computation (This defaults to 1/nobs)
      * - prior
        - Prior
        - Specify prior probability for p(y==1), (Use this parameter for logistic regression if the data has been sampled and the mean of response does not reflect reality)
      * - score_each_iteration
        - Score Each Iteration
        - Enable to score during each iteration of the model training (Optional)
      * - hl
        - hl
      * - tweedie_variance_power
        - Tweedie Variance Power
        - Specify the Tweedie variance power (Only applicable if Tweedie is specified for Family)
      * - tweedie_link_power
        - Tweedie Link Power
        - Specify the Tweedie link power (Only applicable if Tweedie is specified for Family)
      * - hl
        - hl


Details
-------


Generalized Linear Models (GLM) estimate regression models for outcomes following exponential distributions. In addition to the Gaussian (i.e. normal) distribution, these include Poisson, binomial, and gamma distributions. Each serves a different purpose, and depending on distribution and link function choice, can be used either for prediction or classification.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/glm.html


