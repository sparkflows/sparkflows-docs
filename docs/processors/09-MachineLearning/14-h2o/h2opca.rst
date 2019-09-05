H2OPCA
=========== 

H2O PCA

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2OPCA

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
        - Specify the rank of matrix approximation (This can be a value from 1 to 9 and defaults to 1).
      * - ignored_columns
        - Specify the column or columns to be excluded from the model
        - 
      * - ignore_const_cols
        - Specify whether to ignore constant training columns (This option is enabled by default)
        - 
      * - max_iterations
        - max_iterations
        - Specify the number of training iterations (The value must be between 1 and 1e6 and the default is 1000)
      * - advanced
        - Advanced
      * - compute_metrics
        - Compute Metrics
        - Enable metrics computations on the training data
      * - impute_missing
        - Impute Missing
        - Specifies whether to impute missing entries with the column mean value
      * - pca_implementation
        - PCA Implementation
        - it Specify the implementation to use for computing PCA (via SVD or EVD)
      * - pca_method
        - PCA Method
        - Specify the algorithm to use for computing the principal components
      * - transform
        - Transform
        - Specify the transformation method for the training data
      * - use_all_factor_levels
        - Use All Factor Levels
        - Specify whether to use all factor levels in the possible set of predictors


Details
-------


Principal Components Analysis (PCA) is closely related to Principal Components Regression. The algorithm is carried out on a set of possibly collinear features and performs a transformation to produce a new set of uncorrelated features.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/pca.html


