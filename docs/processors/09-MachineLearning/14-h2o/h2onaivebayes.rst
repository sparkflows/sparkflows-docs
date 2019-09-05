H2ONaiveBayes
=========== 

H2O Naive Bayes

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2ONaiveBayes

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
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be excluded from the model
      * - ignore_const_cols
        - Ignore Const Colst
        - Specify whether to ignore constant training columns, since no information can be gained from them. This option is enabled by default.
      * - nfolds
        - NFolds
        - Specify the number of folds for cross-validation
      * - seed
        - Seed
        - Specify the random number generator (RNG) seed for algorithm components dependent on randomization
      * - advanced
        - Advanced
      * - balance_classes
        - Balance classes
        - Specify whether to oversample the minority classes to balance the class distribution.
      * - max_after_balance_size
        - Max after balance size
        - Specify the maximum relative size of the training data after balancing class counts (balance_classes must be enabled)
      * - hl
        - hl
      * - hl
        - hl
      * - compute_metrics
        - Compute metrics
        - Enable to compute metrics on training data
      * - hl
        - hl
      * - eps_prob
        - eEps probability
        - Specify Cutoff below which probability is replaced with min_prob
      * - eps_sdev
        - Eps sdev
        - Specify the threshold for standard deviation (The value must be positive)
      * - hl
        - hl
      * - fold_assignment
        - Fold Assignment
        - Specify the cross-validation fold assignment scheme (Applicable only if a value for nfold is specified and fold_column is not specified)
      * - fold_column
        - Fold Column
        - Specify the column that contains the cross-validation fold index assignment per observation
      * - hl
        - hl
      * - keep_cross_validation_fold_assignment
        - Keep CV Fold Assignment
        - it Enable to preserve the cross-validation fold assignment.
      * - keep_cross_validation_predictions
        - Keep CV Predictions
        - it Enable to keep the cross-validation predictions.
      * - hl
        - hl
      * - laplace
        - Laplace
        - Specify the Laplace smoothing parameter (The value must be an integer >= 0)
      * - min_prob
        - Min probability
        - Specify the minimum probability to use for observations without enough data
      * - min_sdev
        - Min SDEV
        - Specify the minimum standard deviation to use for observations without enough data
      * - hl
        - hl
      * - score_each_iteration
        - Score Each Iteration
        - (Optional) Specify whether to score during each iteration of the model training.
      * - hl
        - hl


Details
-------


Naïve Bayes is a classification algorithm that relies on strong assumptions of the independence of covariates in applying Bayes Theorem. The Naïve Bayes classifier assumes independence between predictor variables conditional on the response, and a Gaussian distribution of numeric predictors with mean and standard deviation computed from the training dataset.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/naive-bayes.html


