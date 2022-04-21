Sklearn Random Forest Classifier
=========== 

Random Forest Classifier, fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.sklearn.NodeSklearnRandomForestClassifier

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
      * - n_estimators
        - NEstimators
        - 
      * - criterion
        - Criterion
        - 
      * - max_depth
        - MaxDepth
        - Default value is None
      * - min_samples_split
        - MinSamplesSplit
        - 
      * - min_samples_leaf
        - MinSamplesLeaf
        - 
      * - min_weight_fraction_leaf
        - MinWeightFractionLeaf
        - 
      * - max_features
        - MaxFeatures
        - 
      * - max_leaf_nodes
        - MaxLeafNodes
        - Default value is None
      * - min_impurity_decrease
        - MinImpurityDecrease
        - 
      * - min_impurity_split
        - MinImpuritySplit
        - 
      * - bootstrap
        - Bootstrap
        - 
      * - oob_score
        - OobScore
        - 
      * - random_state
        - RandomState
        - Default value is None 
      * - warm_start
        - WarmStart
        - 


Details
-------


More details are available at : https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html


