H2O Auto ML
=========== 

H2O AutoML

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2OAutoML

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
      * - max_runtime_secs
        - Max Runtime Secs
        - This argument controls how long the AutoML will run at the most, before training the final Stacked Ensemble models.If neither max_runtime_secs nor max_models are specified by the user, then max_runtime_secs defaults to 3600 seconds (1 hour)
      * - max_models
        - Max Models
        - Specify the maximum number of models to build in an AutoML run, excluding the Stacked Ensemble models.
      * - nfolds
        - Nfolds
        - Number of folds for k-fold cross-validation. Defaults to 5.
      * - max_runtime_secs_per_model
        - Max Models
        - This argument controls the max time the AutoML run will dedicate to each individual model. Defaults to 0
      * - stopping_metric
        - StoppingMetric
        - Specifies the metric to use for early stopping.
      * - stopping_tolerance
        - StoppingTolerance
        - This option specifies the relative tolerance for the metric-based stoppingto stop the AutoML run if the improvement is less than this value. This value defaults to 0.001
      * - stopping_rounds
        - StoppingRounds
        - This argument stops training new models in the AutoML run when the option selected forstopping_metric doesn't improve for the specified number of models, based on a simple moving average.To disable this feature, set it to 0. Defaults to 3 and must be an non-negative integer.
      * - include_algos
        - Include Algos
        - By default all algos will be selected
      * - balance_classes
        - BalanceClasses
        - Specify whether to oversample the minority classes to balance the class distribution.
      * - sort_metric
        - Sort Metric
        - Metric to sort the leaderboard by. Defaults to AUTO
      * - weights_column
        - Weights Column
        - Specify a column to use for the observation weights, which are used for bias correction.
      * - fold_column
        - Fold Column
        - The name or index of the column in training_frame that holds per-row fold assignments.
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be excluded from the model
      * - keep_cross_validation_predictions
        - KeepCrossValidationPredictions
        - Whether to keep the predictions of the cross-validation predictions.
      * - keep_cross_validation_models
        - KeepCrossValidationModels
        - Whether to keep the cross-validated models. Keeping cross-validation models may consume significantly more memory in the H2O cluster.
      * - keep_cross_validation_fold_assignment
        - KeepCrossValidationFoldAssignment
        - Whether to keep fold assignments in the models. Deleting them will save memory in the H2O cluster.
      * - path
        - Path
        - Path for saving the H2O Mojo


Details
-------


H2O AutoML(for Regression and Classification) The H2O AutoML interface is designed to have as few parameters as possible so that all the user needs to do is point to their dataset, identify the response column and optionally specify a time constraint or limit on the number of total models trained.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html#automl-automatic-machine-learning


