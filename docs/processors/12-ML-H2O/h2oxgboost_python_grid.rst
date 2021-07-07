H2O XGBoost With Grid Search
=========== 

H2O XGBoost

Input
--------------
It takes in a DataFrame as input

Type
--------- 

join

Class
--------- 

fire.nodes.h2o.node_h2oxgboost_gridsearch

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - responseCol
        - Response Column
        - 
      * - featureCols
        - Feature Columns
        - Specify the column or columns to be included for feature.
      * - max_leaves
        - Max Leaves
        - Specify the maximum number of leaves to include each tree
      * - ntrees
        - NTrees
        - Specify the number of trees to build
      * - tree_method
        - Tree Method
        - Specify the construction tree method to use.
      * - grow_policy
        - Grow Policy
        - 
      * - stopping_rounds
        - Stopping Rounds
        - 
      * - stopping_metric
        - Stopping Metric
        - Specify the construction tree method to use.
      * - seed
        - Seed
        - 
      * - gridSearch
        - GridSearch
      * - max_depth
        - Max Depth
        - Specify the maximum tree depth (Setting this value to 0 specifies no limit)
      * - learn_rate
        - Learn Rate
        - Specify the learning rate (The range is 0.0 to 1.0)
      * - sample_rate
        - Sample rate
        - Specify the row sampling rate (x-axis). (Note that this method is sample without replacement)
      * - col_sample_rate
        - Col Sample Rate
        - 




