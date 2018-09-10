GBTClassifier
=========== 

Gradient-Boosted Trees (GBTs) is a learning algorithm for classification. It supports binary labels, as well as both continuous and categorical features. Note: Multiclass labels are not currently supported.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeGBTClassifier

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      * - Name
        - Title
        - Description
      * - featuresCol
        - Features Column
        - Features column of type vectorUDT for model fitting
      * - labelCol
        - Label Column
        - The label column for model fitting
      * - predictionCol
        - Prediction Columns
        - The prediction column created during model scoring.
      * - impurity
        - Impurity
        - The Criterion used for information gain calculation
      * - lossType
        - Loss Function
        - The Loss function which GBT tries to minimize
      * - maxBins
        - Max Bins
        - The maximum number of bins used for discretizing continuous features.Must be >= 2 and >= number of categories in any categorical feature.
      * - maxDepth
        - Max Depth
        - The Maximum depth of a tree
      * - maxIter
        - Max Iterations
        - The maximum number of iterations(>=0)(a.k.a numtrees)
      * - minInfoGain
        - Min Information Gain
        - The Minimum information gain for a split to be considered at a tree node
      * - minInstancesPerNode
        - Min Instances Per Node
        - The Minimum number of instances each child must have after split
      * - subsamplingRate
        - Subsampling Rate
        - The fraction of the training data used for learning each decision tree.
      * - seed
        - Seed
        - The random seed
      * - stepSize
        - Step Size
        - Step size (a.k.a. learning rate), The step size to be used for each iteration of optimization.
      * - cacheNodeIds
        - Cache Node Ids
        - The caching nodes IDs. Can speed up training of deeper trees.
      * - checkpointInterval
        - Checkpoint Interval
        - The checkpoint interval. E.g. 10 means that the cache will get checkpointed every 10 iterations.Set checkpoint interval (>= 1) or disable checkpoint (-1)
      * - maxMemoryInMB
        - Max memory
        - Maximum memory in MB allocated to histogram aggregation.
      * - gridSearch
        - Grid Search
      * - minInfoGainGrid
        - Min Information Gain Param Grid Search
        - Min Information Gain Parameters for Grid Search
      * - maxBinsGrid
        - Max Bins Param Grid Search
        - Max Bins Parameters for Grid Search
      * - maxDepthGrid
        - Max Depth Param Grid Search
        - Max Depth Parameters for Grid Search
      * - maxIterGrid
        - Max Iteration Param Grid Search
        - Max Iteration Parameters for Grid Search




