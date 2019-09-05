H2ONeuralNetwork
=========== 

H2O Deep Learning/Neural Network

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2ONeuralNetwork

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
      * - activation
        - Activation
        - Specify the activation function (Tanh, Tanh with dropout, Rectifier, Rectifier with dropout, Maxout, Maxout with dropout), (Maxout is not supported when autoencoder is enabled)
      * - average_activation
        - Average activation
        - Specify the average activation for the sparse autoencoder ( average_activation value must be positive)
      * - reconstructionMSE
        - Reconstruction MSE
        - Only for AutoEncoder Deep Learning model to get MSE
      * - hl
        - hl
      * - offset_column
        - Offset Column
        - Specify a column to use as the offset (Applicable for regression only)
      * - weights_column
        - Weights Column
        - Specify a column to use for the observation weights, which are used for bias correction (The specified weights_column must be included in the specified training_frame)
      * - ignore_const_cols
        - Ignore Const Columns
        - Specify whether to ignore constant training columns
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be excluded from the model (Optional, Python and Flow only)
      * - hl
        - hl
      * - autoencoder
        - Autoencoder
        - Specify whether to enable the Deep Learning autoencoder (Cross-validation is not supported when autoencoder is enabled)
      * - hidden
        - Hidden
        - Specify the hidden layer sizes (value must be positive)
      * - hidden_dropout_ratios
        - Hidden dropout ratios
        - Specify the hidden layer dropout ratio to improve generalization (Applicable only if the activation type is TanhWithDropout, RectifierWithDropout, or MaxoutWithDropout)
      * - hl
        - hl
      * - hl
        - hl
      * - nfolds
        - NFolds
        - Specify the number of folds for cross-validation (Cross-validation is not supported when autoencoder is enabled)
      * - fold_assignment
        - Fold Assignment
        - Specify the cross-validation fold assignment scheme (Applicable only if a value for nfolds is specified and fold_column is not specified)
      * - fold_column
        - Fold Column
        - Specify the column that contains the cross-validation fold index assignment per observation
      * - hl
        - hl
      * - l1
        - L1
        - Specify the L1 regularization to add stability and improve generalization (sets the value of many weights to 0)
      * - l2
        - L2
        - Specify the L2 regularization to add stability and improve generalization (sets the value of many weights to smaller values)
      * - seed
        - Seed
        - Specify the random number generator (RNG) seed for algorithm components dependent on randomization
      * - advanced1
        - Advanced 1
      * - adaptive_rate
        - Adaptive rate
        - Specify whether to enable the adaptive learning rate (ADADELTA), (enabled by default)
      * - hl
        - hl
      * - huber_alpha
        - Huber alpha
        - Specify the desired quantile for Huber/M-regression (the threshold between quadratic and linear loss)
      * - quantile_alpha
        - Quantile alpha
        - Specify the quantile to be used for Quantile Regression (Only applicable if distribution=quantile)
      * - tweedie_power
        - Tweedie power
        - Specify the Tweedie power (Only applicable if distribution=tweedie)
      * - hl
        - hl
      * - balance_classes
        - Balance classes
        - Specify whether to oversample the minority classes to balance the class distribution (Applicable for classification only)
      * - categorical_encoding
        - Categorical encoding
        - Specify one of the various encoding schemes for handling categorical features
      * - class_sampling_factors
        - Class sampling factors
        - Specify the per-class (in lexicographical order) over/under-sampling ratios (Applicable only for classification and when balance_classes is enabled)
      * - col_major
        - Col major
        - Specify whether to use a column major weight matrix for the input layer
      * - diagnostics
        - Diagnostics
        - Specify whether to compute the variable importances for input features (using the Gedeon method)
      * - distribution
        - Distribution
        - Specify the distribution (i.e., the loss function)
      * - epochs
        - Epochs
        - Specify the number of times to iterate (stream) the dataset ( value can be a fraction)
      * - hl
        - hl
      * - elastic_averaging
        - Elastic averaging
        - Specify whether to enable elastic averaging between computing nodes, which can improve distributed model convergence
      * - elastic_averaging_moving_rate
        - Elastic averaging moving rate
        - Specify the moving rate for elastic averaging (option is only available if elastic_averaging=True)
      * - elastic_averaging_regularization
        - Elastic averaging regularization
        - Specify the elastic averaging regularization strength (option is only available if elastic_averaging=True)
      * - epsilon
        - Epsilon
        - Specify the adaptive learning rate time smoothing factor to avoid dividing by zero (Applicable only if adaptive_rate is enabled)
      * - export_weights_and_biases
        - Export weights and biases
        - Specify whether to export the neural network weights and biases as H2O frames
      * - hl
        - hl
      * - force_load_balance
        - Force load balance
        - Specify whether to force extra load balancing to increase training speed for small datasets and use all cores (option is enabled by default)
      * - input_drop_ratio
        - Input drop ratio
        - Specify the input layer dropout ratio to improve generalization (Suggested values are 0.1 or 0.2)
      * - initial_weight_distribution
        - Initial weight distribution
        - Specify the initial weight distribution (Uniform Adaptive, Uniform, or Normal)
      * - initial_weight_scale
        - Initial weight scale
        - Specify the scale of the distribution function (Applicable only if initial_weight_distribution is Uniform or Normal)
      * - hl
        - hl
      * - keep_cross_validation_predictions
        - Keep CV Predictions
        - Enable to keep the cross-validation predictions
      * - keep_cross_validation_fold_assignment
        - Keep CV Fold Assignment
        - Enable to preserve the cross-validation fold assignment
      * - hl
        - hl
      * - loss
        - Loss
        - Specify the loss function (Use Absolute, Quadratic, or Huber for regression, Use Absolute, Quadratic, Huber, or CrossEntropy for classification)
      * - max_after_balance_size
        - MAx after balance size
        - Specify the maximum relative size of the training data after balancing class counts (balance_classes must be enabled)
      * - max_runtime_secs
        - Max runtime secs
        - Allowed runtime in seconds for model training
      * - max_w2
        - Max w2
        - Specify the constraint for the squared sum of the incoming weights per unit
      * - mini_batch_size
        - Mini batch size
        - Specify a value for the mini-batch size. (Smaller values lead to a better fit; larger values can speed up and generalize better)
      * - missing_values_handling
        - Missing values handling
        - Specify how to handle missing values (Skip or MeanImputation)
      * - momentum_start
        - Momentum Start
        - Specify the initial momentum at the beginning of training; we suggest 0.5 (Applicable only if adaptive_rate is disabled)
      * - momentum_stable
        - Momentum Stable
        - Specify the final momentum after the ramp is over; we suggest 0.99 (Applicable only if adaptive_rate is disabled)
      * - max_categorical_features
        - NFolds
        - Specify the maximum number of categorical features enforced via hashing (value must be at least one)
      * - hl
        - hl
      * - fast_mode
        - Fast mode
        - Specify whether to enable fast mode, a minor approximation in back-propagation (option is enabled by default)
      * - quiet_mode
        - Quiet mode
        - Specify whether to display less output in the standard output ( not enabled by default)
      * - single_node_mode
        - Single node mode
        - Specify whether to run on a single node for fine-tuning of model parameters
      * - hl
        - hl
      * - nesterov_accelerated_gradient
        - Nesterov Accelerated Gradient
        - Enables the Nesterov Accelerated Gradient (Applicable only if adaptive_rate is disabled)
      * - overwrite_with_best_model
        - Overwrite with best model
        - Specify whether to overwrite the final model with the best model found during training, based on the option specified for stopping_metric
      * - hl
        - hl
      * - rate
        - Rate
        - Specify the learning rate (Applicable only if adaptive_rate is disabled)
      * - rate_annealing
        - Rate Annealing
        - Specify the rate annealing value (Applicable only if adaptive_rate is disabled)
      * - rate_decay
        - Rate Decay
        - 
      * - hl
        - hl
      * - advanced2
        - Advanced 2
      * - hl
        - hl
      * - reproducible
        - Reproducible
        - Specify whether to force reproducibility on small data
      * - rho
        - Rho
        - Specify the adaptive learning rate time decay factor (Applicable only if adaptive_rate is enabled)
      * - standardize
        - Standardize
        - If enabled, automatically standardize the data (mean 0, variance 1)
      * - hl
        - hl
      * - stopping_metric
        - Stopping metric
        - Specify the metric to use for early stopping
      * - stopping_rounds
        - Stopping Rounds
        - Stops training when the option selected for stopping_metric doesn’t improve for the specified number of training rounds, based on a simple moving average
      * - stopping_tolerance
        - Stopping tolerance
        - Specify the relative tolerance for the metric-based stopping to stop training if the improvement is less than this value
      * - hl
        - hl
      * - advanced3
        - Advanced 3
      * - hl
        - hl
      * - score_duty_cycle
        - Score duty cycle
        - Specify the maximum duty cycle fraction forscoring
      * - score_each_iteration
        - Score Each Iteration
        - Specify whether to score during each iteration of the model training (Optional)
      * - score_interval
        - Score interval
        - Specify the shortest time interval (in seconds) to wait between model scoring
      * - score_training_samples
        - Score training samples
        - Specify the number of training set samples for scoring. The value must be >= 0
      * - score_validation_samples
        - Score validation samples
        - Specify the number of validation set samples for scoring (Applicable only if a validation_frame is specified)
      * - score_validation_sampling
        - Score validation sampling
        - Specify the method used to sample validation dataset for scoring
      * - hl
        - hl
      * - classification_stop
        - Classification stop
        - Specify the stopping criteria in terms of classification error (1-accuracy) on the training data scoring dataset
      * - regression_stop
        - Regression stop
        - Specify the stopping criterion for regression error (MSE) on the training data (Regression models only)
      * - hl
        - hl
      * - sparse
        - Sparse
        - Specify whether to enable sparse data handling, which is more efficient for data with many zero values
      * - sparsity_beta
        - Sparsity beta
        - Specify the sparsity-based regularization optimization (Applicable only if autoencoder is enabled)
      * - hl
        - hl
      * - replicate_training_data
        - Replicate training data
        - Specify whether to replicate the entire training dataset onto every node for faster training on small datasets
      * - shuffle_training_data
        - Shuffle training data
        - Specify whether to shuffle the training data
      * - target_ratio_comm_to_comp
        - Target ratio comm to comp
        - Specify the target ratio of communication overhead to computation
      * - train_samples_per_iteration
        - Train samples per iteration
        - Specify the number of global training samples per MapReduce iteration
      * - hl
        - hl
      * - use_all_factor_levels
        - Use all factor levels
        - Specify whether to use all factor levels in the possible set of predictors
      * - variable_importances
        - Variable importances
        - Specify whether to compute variable importance


Details
-------


H2O’s Deep Learning is based on a multi-layer feedforward artificial neural network that is trained with stochastic gradient descent using back-propagation. The network can contain a large number of hidden layers consisting of neurons with tanh, rectifier, and maxout activation functions.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/deep-learning.html


