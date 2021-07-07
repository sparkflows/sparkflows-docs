H2O XGBoost
=========== 

XGBoost is a supervised learning algorithm that implements a process called boosting to yield accurate models.

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2OXGBoost

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
        - is Response Col Categorical
        - It Specifies a response column type(numeric or categorical). Separates the Classification and Regression
      * - featuresCols
        - Feature Columns
        - Specify the column or columns to be included for feature.
      * - fold_column
        - Fold Column
        - Specify a column to use as the fold
      * - weights_column
        - Weights Column
        - Specify a column to use for the observation weights, which are used for bias correction
      * - hl
        - hl
      * - learn_rate
        - Learn Rate
        - Specify the learning rate (The range is 0.0 to 1.0)
      * - max_depth
        - Max Depth
        - Specify the maximum tree depth (Setting this value to 0 specifies no limit)
      * - ntrees
        - NTrees
        - Specify the number of trees to build
      * - maxBins
        - Max Bins
        - Specify the maximum number of bins for binning continuous features. This value defaults to 256.
      * - maxLeaves
        - Max Leaves
        - Specify the maximum number of leaves to include each tree
      * - sample_rate
        - Sample rate
        - Specify the row sampling rate (x-axis). (Note that this method is sample without replacement)
      * - hl
        - hl
      * - distributionFamily
        - Distribution
        - Specify the distribution (i.e., the loss function),The options are AUTO, bernoulli, multinomial, gaussian, poisson, gamma, laplace, quantile, huber, or tweedie.
      * - booster
        - Booster
        - Specify the booster type. This can be one of the following: gbtree, gblinear, or dart. Note that gbtree and dart use a tree-based model while gblinear uses linear function
      * - treeMethod
        - Tree Method
        - Specify the construction tree method to use.
      * - missingValuesHandling
        - Missing Values Handling
        - Specify the construction tree method to use.
      * - backend
        - Backend
        - Specify the backend type. This can be done of the following: auto, gpu, or cpu. By default (auto), a GPU is used if available.
      * - dMatrixType
        - DMatrixType
        - Specify the type of DMatrix.
      * - sampleType
        - SampleType
        - Specify whether the sampling type should be one of the following: uniform or weighted.


Details
-------


XGBoost is a supervised learning algorithm that implements a process called boosting to yield accurate models. Boosting refers to the ensemble learning technique of building many models sequentially, with each new model attempting to correct for the deficiencies in the previous model.

More details are available at : https://h2o-release.s3.amazonaws.com/h2o/rel-weierstrass/2/docs-website/h2o-docs/data-science/xgboost.html


