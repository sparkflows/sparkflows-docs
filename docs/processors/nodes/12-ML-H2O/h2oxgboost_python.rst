H2O XGBoost
=========== 

H2O XGBoost

Input
--------------
It takes in a two DataFrame as input, one is for train and other one is for validation.

Type
--------- 

join

Class
--------- 

fire.nodes.h2o.node_h2oxgboost

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
      * - ntrees
        - NTrees
        - Specify the number of trees to build
      * - tree_method
        - Tree Method
        - Specify the construction tree method to use.
      * - grow_policy
        - Grow Policy
        - 
      * - max_depth
        - Max Depth
        - Specify the maximum tree depth (Setting this value to 0 specifies no limit)
      * - max_leaves
        - Max Leaves
        - Specify the maximum number of leaves to include each tree
      * - col_sample_rate_per_tree
        - Col Sample Rate Per Tree
        - 
      * - sample_rate
        - Sample rate
        - Specify the row sampling rate (x-axis). (Note that this method is sample without replacement)
      * - learn_rate
        - Learn Rate
        - Specify the learning rate (The range is 0.0 to 1.0)
      * - stopping_rounds
        - Stopping Rounds
        - 
      * - stopping_metric
        - Stopping Metric
        - Specify the construction tree method to use.
      * - seed
        - Seed
        - 




