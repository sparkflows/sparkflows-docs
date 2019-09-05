H2ODRF
=========== 

H2O DRF

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2ODrf

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
        - it Specify a response column type(numeric or categorical). Separates the Classification and Regression
      * - ignore_const_cols
        - Ignore Const Cols
        - Specify whether to ignore constant training columns, since no information can be gained from them
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be excluded from the model (Optional, Python and Flow only)
      * - fold_column
        - Fold Column
        - Specify the column that contains the cross-validation fold index assignment per observation
      * - weights_column
        - Weights Column
        - Specify whether to ignore constant training columns, since no information can be gained from them (enabled by default)
      * - hl
        - hl
      * - max_depth
        - Max Depth
        - Specify the maximum tree depth (defaults values to 20)
      * - min_rows
        - Min Rows
        - Specify the minimum number of observations for a leaf (nodesize in R)
      * - hl
        - hl
      * - distribution
        - Distribution
        - Specify the distribution (i.e., the loss function),The options are AUTO, bernoulli, multinomial, gaussian, poisson, gamma, laplace, quantile, huber, or tweedie
      * - nfolds
        - NFolds
        - Specify the number of folds for cross-validation
      * - ntrees
        - NTrees
        - Specify the number of trees
      * - nbins
        - NBins
        - Specify the number of bins for the histogram to build, then split at the best point (Numerical/real/int only)
      * - nbins_top_level
        - Nbins top level
        - Specify the minimum number of bins at the root level to use to build the histogram (For numerical/real/int columns only)
      * - nbins_cats
        - NBin Cats
        - Specify the maximum number of bins for the histogram to build, then split at the best point (Categorical/enums only)
      * - seed
        - Seed
        - Specify the random number generator (RNG) seed for algorithm components dependent on randomization
      * - advanced
        - Advanced
      * - balance_classes
        - Balance classes
        - balance the class distribution (only applicable for classification)
      * - binomial_double_trees
        - Binomial double trees
        - Build twice as many trees (one per class), (Binary classification only) 
      * - build_tree_one_node
        - Build tree one node
        - Enables to run on a single node
      * - calibrate_model
        - Calibrate model
        - Use Platt scaling to calculate calibrated class probabilities (Defaults to False)
      * - categorical_encoding
        - Categorical encoding
        - Specify one of the various encoding schemes for handling categorical features
      * - check_constant_response
        - Check constant response
        - Check if the response column is a constant value (enabled (default))
      * - class_sampling_factors
        - Class sampling factors
        - Specify the per-class (in lexicographical order) over/under-sampling ratios (Note that this requires balance_classes=true)
      * - col_sample_rate_change_per_level
        - Col sample rate change per level
        - Specify to change the column sampling rate as a function of the depth in the tree
      * - col_sample_rate_per_tree
        - Col sample rate per tree
        - Specify the column sample rate per tree (value can be from 0.0 to 1.0 and defaults to 1)
      * - min_split_improvement
        - Col sample rate per tree
        - Specifies the minimum relative improvement in squared error reduction in order for a split to happen (Optimal values would be in the 1e-10…1e-3 range
      * - custom_metric_func
        - Custom metric func
        - it specify a custom evaluation function (Optional)
      * - fold_assignment
        - Fold Assignment
        - Specify the cross-validation fold assignment scheme (Applicable only if a value for nfolds is specified and fold_column is not specified)
      * - histogram_type
        - Histogram type
        - Specify the type of histogram to use for finding optimal split points (By default (AUTO) DRF bins from min…max in steps of (max-min)/N)
      * - hl
        - hl
      * - keep_cross_validation_predictions
        - Keep CV Predictions
        - Enable to keep the cross-validation prediction
      * - keep_cross_validation_fold_assignment
        - Keep CV Fold Assignment
        - Enable to preserve the cross-validation fold assignment
      * - max_after_balance_size
        - MAx after balance size
        - Specify the maximum relative size of the training data after balancing class counts (balance_classes must be enabled, value can be less than 1.0)
      * - max_hit_ratio_k
        - Max hit ratio k
        - Specify the maximum number (top K) of predictions to use for hit ratio computation ( Applicable to multi-class only)
      * - max_runtime_secs
        - Max runtime secs
        - Maximum allowed runtime in seconds for model training (Use 0 to disable) 
      * - mtries
        - Mtries
        - Specify the columns to randomly select at each level 
      * - hl
        - hl
      * - sample_rate
        - Sample rate
        - Specify the row sampling rate (x-axis), (Note that this method is sample without replacement)
      * - sample_rate_per_class
        - Sample rate per class
        - Specifies that each tree in the ensemble should sample from the full training dataset using a per-class-specific sampling rate rather than a global sample factor (as with sample_rate)
      * - hl
        - hl
      * - score_each_iteration
        - Score Each Iteration
        - it Enable to score during each iteration of the model training (Optional)
      * - score_tree_interval
        - Score tree interval
        - Score the model after every so many trees (Disabled if set to 0)
      * - hl
        - hl
      * - hl
        - hl
      * - stopping_rounds
        - Stopping Rounds
        - Stops training when the option selected for stopping_metric
      * - stopping_metric
        - Stopping metric
        - Specify the metric to use for early stopping
      * - stopping_tolerance
        - Stopping tolerance
        - Specify the relative tolerance for the metric-based stopping to stop training if the improvement is less than this value
      * - hl
        - hl


Details
-------


Distributed Random Forest (DRF) is a powerful classification and regression tool. When given a set of data, DRF generates a forest of classification or regression trees, rather than a single classification or regression tree. Each of these trees is a weak learner built on a subset of rows and columns. More trees will reduce the variance. Both classification and regression take the average prediction over all of their trees to make a final prediction, whether predicting for a class or numeric value.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/drf.html


