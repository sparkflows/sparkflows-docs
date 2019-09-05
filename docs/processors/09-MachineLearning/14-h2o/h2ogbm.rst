H2OGBM
=========== 

H2O GBM

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2OGbm

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
      * - offset_column
        - Offset Column
        - Specify a column to use as the offset
      * - weights_column
        - Weights Column
        - Specify a column to use for the observation weights, which are used for bias correction
      * - ignore_const_cols
        - Ignore Const Colst
        - Specify whether to ignore constant training columns
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be excluded from the model
      * - hl
        - hl
      * - learn_rate
        - Learn Rate
        - Specify the learning rate (The range is 0.0 to 1.0)
      * - max_depth
        - Max Depth
        - Specify the maximum tree depth (Setting this value to 0 specifies no limit)
      * - nfolds
        - NFolds
        - Specify the number of folds for cross-validation
      * - ntrees
        - NTrees
        - Specify the number of trees to build
      * - hl
        - hl
      * - build_tree_one_node
        - Build tree one node
        - Specify to run on a single node, check this checkbox
      * - max_runtime_secs
        - Max runtime secs
        - Allowed runtime in seconds for model training (Use 0 to disable)
      * - seed
        - Seed
        - Specify the random number generator (RNG)
      * - hl
        - hl
      * - stopping_rounds
        - Stopping Rounds
        - Stops training when the option selected for stopping_metric doesn’t improve for the specified number of training rounds, based on a simple moving average
      * - stopping_metric
        - Stopping metric
        - Specify the metric to use for early stopping
      * - stopping_tolerance
        - Stopping tolerance
        - Specify the relative tolerance for the metric-based stopping to stop training if the improvement is less than this value
      * - advanced
        - Advanced
      * - balance_classes
        - Balance classes
        - Specify whether to oversample the minority classes to balance the class distribution
      * - calibrate_model
        - Calibrate model
        - Use Platt scaling to calculate calibrated class probabilities (Defaults to False)
      * - categorical_encoding
        - Categorical encoding
        - Specify variuos encoding schemes for handling categorical features
      * - check_constant_response
        - Check constant response
        - it Check if the response column is a constant value
      * - class_sampling_factors
        - Class sampling factors
        - Specify the per-class (in lexicographical order) over/under-sampling ratios (By default, these ratios are automatically computed during training to obtain the class balance, Note that this requires balance_classes=true)
      * - hl
        - hl
      * - col_sample_rate
        - Col sample rate
        - Specify the column sampling rate (y-axis) (Note that this method is sampling without replacement)
      * - col_sample_rate_change_per_level
        - Col sample rate change per level
        - Specify to change the column sampling rate as a function of the depth in the tree (This can be a value > 0.0 and <= 2.0 and defaults to 1)
      * - col_sample_rate_per_tree
        - Col sample rate per tree
        - Specify the column sample rate per tree (This can be a value from 0.0 to 1.0 and defaults to 1)
      * - min_split_improvement
        - Col sample rate per tree
        - Specify the minimum relative improvement in squared error reduction in order for a split to happen
      * - hl
        - hl
      * - custom_metric_func
        - Custom metric func
        - Specify a custom evaluation function
      * - distribution
        - Distribution
        - Specify the distribution (i.e., the loss function),The options are AUTO, bernoulli, multinomial, gaussian, poisson, gamma, laplace, quantile, huber, or tweedie
      * - fold_assignment
        - Fold Assignment
        - Specify the cross-validation fold assignment scheme (Applicable only if a value for nfolds is specified and fold_column is not specified)
      * - histogram_type
        - Histogram type
        - Specify to cycle through all histogram types (one per tree)
      * - hl
        - hl
      * - keep_cross_validation_fold_assignment
        - Keep CV Fold Assignment
        - Enable to preserve the cross-validation fold assignment
      * - keep_cross_validation_predictions
        - Keep CV Predictions
        - Enable to keep the cross-validation predictions
      * - hl
        - hl
      * - learn_rate_annealing
        - Learn Rate Anealing
        - Specifies to reduce the learn_rate by this factor after every tree. So for N trees, GBM starts with learn_rate and ends with learn_rate * learn_rate_annealing**^*N*
      * - max_abs_leafnode_pred
        - Max abs leafnode pred
        - Reduces overfitting by limiting the maximum absolute value of a leaf node prediction (Double.MaxValue by default)
      * - max_hit_ratio_k
        - Max hit ratio k
        - Specify the maximum number (top K) of predictions to use for hit ratio computation (Applicable to multi-class only)
      * - max_after_balance_size
        - MAX after balance size
        - Specify the maximum relative size of the training data after balancing class counts (balance_classes must be enabled)
      * - min_rows
        - Min Rows
        - it Specify the minimum number of observations for a leaf (nodesize in R)
      * - hl
        - hl
      * - nbins
        - NBins
        - Specify the number of bins for the histogram to build, then split at the best point (Numerical/real/int only)
      * - nbins_cats
        - NBin Cats
        - Specify the maximum number of bins for the histogram to build, then split at the best point (Categorical/enums only)
      * - nbins_top_level
        - Nbins top level
        - Specify the minimum number of bins at the root level to use to build the histogram (For numerical/real/int columns only)
      * - hl
        - hl
      * - pred_noise_bandwidth
        - Pred noise bandwidth
        - Specify bandwidth (sigma) of Gaussian multiplicative noise ~N(1,sigma) for tree node predictions
      * - score_each_iteration
        - Score Each Iteration
        - Specify whether to score during each iteration of the model training
      * - score_tree_interval
        - Score tree interval
        - Score the model after every so many trees (Disabled if set to 0)
      * - hl
        - hl
      * - huber_alpha
        - Huber alpha
        - Specify the desired quantile for Huber/M-regression (the threshold between quadratic and linear loss)
      * - quantile_alpha
        - Quantile alpha
        - Specify the quantile to be used for Quantile Regression (Only applicable if Quantile is specified for distribution)
      * - tweedie_power
        - Tweedie power
        - Specify the Tweedie power. The range is from 1 to 2 (Only applicable if Tweedie is specified for distribution)
      * - hl
        - hl
      * - sample_rate
        - Sample rate
        - Specify the row sampling rate (x-axis). (Note that this method is sample without replacement)
      * - sample_rate_per_class
        - Sample rate per class
        - Specifies that each tree in the ensemble should sample from the full training dataset using a per-class-specific sampling rate rather than a global sample factor (as with sample_rate)
      * - hl
        - hl


Details
-------


Gradient Boosting Machine (for Regression and Classification) is a forward learning ensemble method. The guiding heuristic is that good predictive results can be obtained through increasingly refined approximations. H2O’s GBM sequentially builds regression trees on all the features of the dataset in a fully distributed way - each tree is built in parallel.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/gbm.html


