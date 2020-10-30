H2OGLRM
=========== 

H2O GLRM

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2OGlrm

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
        - Specify the rank of matrix approximation
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be exclude from the model
      * - ignore_const_cols
        - Ignore Const Cols
        - Specify whether to ignore constant training columns
      * - others
        - Advanced
      * - score_each_iteration
        - Score Each Iteration
        - Specify whether to score during each iteration of the model training
      * - transform
        - Transform
        - Specify the transformation method for the training data: None, Standardize, Normalize, Demean, or Descale. The default is None.
      * - loss
        - Loss
        - Specify the numeric loss function: Quadratic, Absolute, Huber, Poisson, Hinge, or Periodic.
      * - multi_loss
        - Multi Loss
        - Specify either Categorical or Ordinal for the categorical loss function.
      * - period
        - Period
        - When loss=periodic, specify the length of the period
      * - hl
        - hl
      * - regularization_x
        - Regularization X
        - Specify the regularization function for the X matrix: None, Quadratic, L2, L1, NonNegative, OneSparse, UnitOneSparse, or Simplex.
      * - regularization_y
        - Regularization Y
        - Specify the regularization function for the Y matrix: None, Quadratic, L2, L1, NonNegative, OneSparse, UnitOneSparse, or Simplex.
      * - hl
        - hl
      * - gamma_x
        - Gamma X
        - Specify the regularization weight on the X matrix.
      * - gamma_y
        - Gamma Y
        - Specify the regularization weight on the Y matrix.
      * - max_iterations
        - Max Iterations
        - Specify the maximum number of training iterations. The range is 0 to 1e6.
      * - max_updates
        - Max Updates
        - Specify the maximum number of updates.
      * - init_step_size
        - Init Step Size
        - Specify the initial step size.
      * - min_step_size
        - Min Step Size
        - Specify the minimum step size.
      * - seed
        - Seed
        - Specify the random number generator (RNG) seed for algorithm components dependent on randomization. 
      * - init_placeholder
        - Init Placeholder
        - Specify the initialization mode: Random, SVD, PlusPlus, or User.
      * - svd_method
        - SVD Method
        - Specify the method for computing SVD during initialization: GramSVD, Power, Randomized.
      * - expand_user_y
        - Expand User Y
        - Specify whether to expand categorical columns in the user-specified initial Y value.
      * - impute_original
        - Impute Original
        - Specify whether to reconstruct the original training data by reversing the data transform after projecting archetypes.
      * - recover_svd
        - Recover SVD
        - Specify whether to recover singular values and eigenvectors of XY.
      * - max_runtime_secs
        - Max Runtimesecs
        - Specify the maximum allowed runtime in seconds for model training. Use 0 to disable.


Details
-------


Generalized Low Rank Models (GLRM) is an algorithm for dimensionality reduction of a dataset. It is a general, parallelized optimization algorithm that applies to a variety of loss and regularization functions. Categorical columns are handled by expansion into 0/1 indicator columns for each level. With this approach, GLRM is useful for reconstructing missing values and identifying important features in heterogeneous data.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/glrm.html


