H2OIsolationForest
=========== 

H2O IsolationForest

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2OIsolationForest

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
      * - offset_column
        - Offset Column
        - 
      * - weights_column
        - Weights Column
        - 
      * - ignore_const_cols
        - Ignore Const Colst
        - Specify whether to ignore constant training columns
      * - ignored_columns
        - Ignored Columns
        - Specify the column or columns to be excluded from the model
      * - ntrees
        - NTrees
        - Specify the number of trees
      * - max_depth
        - Max Depth
        - Specify the maximum tree depth
      * - seed
        - Seed
        - Specify the random number generator (RNG) seed for algorithm components dependent on randomization
      * - advanced
        - Advanced
      * - build_tree_one_node
        - Build Tree One Node
        - To run on a single node
      * - col_sample_rate_change_per_level
        - Column Sample Rate Change Per Level
        - It specifies to change the column sampling rate as a function of the depth in the tree
      * - col_sample_rate_per_tree
        - Column Sample Rate Per Tree
        - Specify the column sample rate per tree
      * - max_runtime_secs
        - Max Runtime (secs)
        - Allowed runtime in seconds for model training
      * - min_rows
        - Min Rows
        - Specify the minimum number of observations for a leaf (nodesize in R)
      * - mtries
        - MTries
        - Specify the columns to randomly select at each level
      * - hl
        - hl
      * - sample_rate
        - Sample Rate
        - Specify the row sampling rate (x-axis)
      * - sample_size
        - Sample Size
        - Specify number of randomly sampled observations used to train each Isolation Forest tree
      * - hl
        - hl
      * - score_each_iteration
        - Score Each Iteration
        - Enable this option to score during each iteration of the model training
      * - score_tree_interval
        - Score Tree Interval
        - Score the model after every so many trees


Details
-------


Isolation Forest is similar in principle to Random Forest and is built on the basis of decision trees. Isolation Forest, however, identifies anomalies or outliers rather than profiling normal data points. Isolation Forest isolates observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of that selected feature. This split depends on how long it takes to separate the points.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/if.html


