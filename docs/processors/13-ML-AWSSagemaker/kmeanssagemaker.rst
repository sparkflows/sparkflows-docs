K-Means SageMaker Estimator
=========== 

Node runs the SageMaker-provided k-means algorithm. The SageMakerEstimator is an org.apache.spark.ml.Estimator that trains a model on Amazon SageMaker.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.sagemaker.NodeKMeansSageMakerEstimator

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
      * - k
        - K
        - The number of clusters to create.
      * - featureDim
        - Feature Dim
        - The number of dimensions in dataset




