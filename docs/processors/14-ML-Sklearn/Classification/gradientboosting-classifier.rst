Sklearn Gradient Boosting Classifier
=========== 

Gradient Boosting Classifier, builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. In each stage n_classes_ regression trees are fit on the negative gradient of the binomial or multinomial deviance loss function. Binary classification is a special case where only a single regression tree is induced.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.sklearn.NodeSklearnGradientBoostingClassifier

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
      * - loss
        - Loss
        - 
      * - learning_rate
        - LearningRate
        - 
      * - n_estimators
        - NEstimators
        - 
      * - subsample
        - Subsample
        - 
      * - criterion
        - Criterion
        - 
      * - min_samples_split
        - MinSamplesSplit
        - 
      * - min_samples_leaf
        - MinSamplesLeaf
        - 
      * - min_weight_fraction_leaf
        - MinWeightFractionLeaf
        - 
      * - max_depth
        - MaxDepth
        - 
      * - min_impurity_decrease
        - MinImpurityDecrease
        - 
      * - min_impurity_split
        - MinImpuritySplit
        - 
      * - random_state
        - RandomState
        - Default value is None i.e -1
      * - verbose
        - Verbose
        - 
      * - max_leaf_nodes
        - MaxLeafNodes
        - Default value is None i.e -1
      * - warm_start
        - WarmStart
        - 
      * - presort
        - Presort
        - 
      * - validation_fraction
        - ValidationFraction
        - 
      * - n_iter_no_change
        - NIterNoChange
        - Default value is None i.e -1
      * - tol
        - Tol
        - 


Details
-------


More details are available at : https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html


