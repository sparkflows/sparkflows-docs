XGBoost Classifier
=========== 



Input
--------------
It takes in a DataFrame as input and performs XGBoost Classification

Output
--------------
The XGBoost Model generated is passed along to the next nodes. The input DataFrame is also passed along to the next nodes

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeXGBoostClassifier

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
        - Prediction Column
        - The prediction column created during model scoring.
      * - numClass
        - Num Class
        - 
      * - maxDepth
        - Max Depth
        - The Maximum depth of a tree
      * - maxBins
        - Max Bins
        - The maximum number of bins used for discretizing continuous features.Must be >= 2 and >= number of categories in any categorical feature.
      * - maxLeaves
        - Max Leaves
        - 
      * - numRound
        - Num Round
        - 
      * - numWorkers
        - Num Workers
        - 
      * - objective
        - Objective
        - 
      * - eta
        - Eta
        - 
      * - regLambda
        - Reg Lambda
        - 
      * - regAlpha
        - Reg Alpha
        - 
      * - subsample
        - Subsample
        - 
      * - sampleType
        - SampleType
        - 
      * - treeMethod
        - TreeMethod
        - 
      * - useExternalMemory
        - UseExternalMemory
        - 
      * - seed
        - Seed
        - 
      * - baseScore
        - Base Score
        - 
      * - minChildWeight
        - Min Child Weight
        - 
      * - colsampleBylevel
        - ColSampleByLevel
        - 
      * - colsampleBytree
        - ColSampleByTree
        - 
      * - minSplitLoss
        - MinSplitLoss
        - 
      * - maxDeltaStep
        - MaxDeltaStep
        - 
      * - sketchEps
        - SketchEps
        - 
      * - scalePosWeight
        - ScalePosWeight
        - 
      * - growPlicy
        - GrowPlicy
        - 
      * - normalizeType
        - NormalizeType
        - 
      * - skipDrop
        - SkipDrop
        - 
      * - rateDrop
        - RateDrop
        - 


Details
-------


Deatils: https://xgboost.readthedocs.io/en/latest/jvm/xgboost4j_spark_tutorial.html#xgboost4j-spark-tutorial-version-0-9


