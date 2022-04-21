Sklearn Bayesian Ridge Regression
=========== 

Bayesian regression allows a natural mechanism to survive insufficient data or poorly distributed data by formulating linear regression using probability distributors rather than point estimates. The output or response ‘y’ is assumed to drawn from a probability distribution rather than estimated as a single value.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.sklearn.NodeSklearnBayesianRidgeRegression

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - targetCol
        - Target Column
        - The label column for model fitting
      * - featureCols
        - Feature Columns
        - Feature columns of type - all numeric, boolean and vector
      * - niter
        - N Iter
        - Maximum number of iterations. Should be greater than or equal to 1.
      * - alpha1
        - Alpha1
        - Hyper-parameter : shape parameter for the Gamma distribution prior over the alpha parameter.
      * - alpha2
        - Alpha2
        - Hyper-parameter : inverse scale parameter (rate parameter) for the Gamma distribution prior over the alpha parameter.
      * - lambda1
        - Lambda1
        - Hyper-parameter : shape parameter for the Gamma distribution prior over the lambda parameter.
      * - lambda2
        - Lambda2
        - Hyper-parameter : inverse scale parameter (rate parameter) for the Gamma distribution prior over the lambda parameter.
      * - tol
        - Tol
        -  Stop the algorithm if w has converged
      * - fitintercept
        - Fitintercept
        - Whether to calculate the intercept for this model. The intercept is not treated as a probabilistic parameter and thus has no associated variance. If set to False, no intercept will be used in calculations
      * - normalize
        - Normalize
        - This parameter is ignored when ``fit_intercept`` is set to False. If True, the regressors X will be normalized before regression by subtracting the mean and dividing by the l2-norm.
      * - compute_score
        - Compute Score
        - If True, compute the log marginal likelihood at each iteration of the optimization.


Details
-------


More details are available at : https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.BayesianRidge.html


