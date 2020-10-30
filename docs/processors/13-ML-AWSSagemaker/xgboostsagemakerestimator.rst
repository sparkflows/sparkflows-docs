XGBoostSageMakerEstimator
=========== 



Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.sagemaker.NodeXGBoostSageMakerEstimator

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - roleArn
        - Role Arn
        - Role arn to use sagemaker
      * - trainingInstanceType
        - Training Instance Type
        - InstanceType for training
      * - trainingInstanceCount
        - Training Instance Count
        - Number of Instance for training
      * - endpointInstanceType
        - Endpoint Instance Type
        - InstanceType for Endpoint
      * - endpointInitialInstanceCount
        - Endpoint Initial Instance Count
        - Number of Instance for Endpoint
      * - booster
        - Booster
        - Select the type of model to run at each iteration. It has 2 options: gbtree: tree-based models & gblinear: linear models
      * - silent
        - Silent
        - Silent mode is activated is set to 1, i.e. no running messages will be printed
      * - nthread
        - NThread
        - If you wish to run on all cores, value should not be entered and algorithm will detect automatically
      * - objective
        - Objective
        - This defines the loss function to be minimized
      * - numTrees
        - Num Trees
        - The number of rounds for boosting
      * - numClasses
        - Num Classes
        - For Objective: multi:softmax, you also need to set an additional num_class (number of classes) parameter defining the number of unique classes
      * - seed
        - Seed
        - Can be used for generating reproducible results and also for parameter tuning




