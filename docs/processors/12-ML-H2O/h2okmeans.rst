H2OKMeans
=========== 

H2O KMeans

Input
--------------
It takes in a DataFrame as input

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.h2o.NodeH2OKMeans

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - k
        - K
        - Specify the number of clusters (groups of data) in a dataset that are similar to one another
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be exclude from the model
      * - ignore_const_cols
        - Ignore Const Cols
        - Specify whether to ignore constant training columns
      * - nfolds
        - NFolds
        - Specify the number of folds for cross-validation
      * - max_iterations
        - Max Iterations
        - Specify the maximum number of training iterations
      * - max_runtime_secs
        - Max runtime in seconds
        - Specify Maximum allowed runtime in seconds for model training
      * - seed
        - Seed
        - Specify the random number generator (RNG) seed for algorithm components dependent on randomization
      * - others
        - Advanced
      * - categorical_encoding
        - Categorical encoding
        - Specify one of the following encoding schemes for handling categorical features
      * - estimate_k
        - Estimate k
        - it Specify whether to estimate the number of clusters (<=k) iteratively (independent of the seed) and deterministically (beginning with k=1,2,3...)
      * - hl
        - hl
      * - fold_assignment
        - Fold Assignment
        - Specify the cross-validation fold assignment scheme (Applicable only if a value for nfolds is specified and fold_column is not specified)
      * - fold_column
        - Fold Column
        - Specify the column that contains the cross-validation fold index assignment per observation
      * - hl
        - hl
      * - init_placeholder
        - Init placeholder
        - Specify the initialization mode
      * - keep_cross_validation_fold_assignment
        - Keep CV Fold Assignment
        - Enable to preserve the cross-validation fold assignment
      * - keep_cross_validation_predictions
        - Keep CV Predictions
        - Enable to keep the cross-validation predictions
      * - score_each_iteration
        - Score Each Iteration
        - Specify whether to score during each iteration of the model training
      * - standardize
        - Standardize
        - Enable to standardize the numeric columns to have a mean of zero and unit variance


Details
-------


K-Means falls in the general category of clustering algorithms. Clustering is a form of unsupervised learning that tries to find structures in the data without using any labels or target values. Clustering partitions a set of observations into separate groupings such that an observation in a given group is more similar to another observation in the same group than to another observation in a different group.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/k-means.html


