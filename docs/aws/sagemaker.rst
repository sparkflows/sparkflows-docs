Fire Integration with SageMaker
========================

Fire is fully integrated with AWS SageMaker. Fire provides a number of processors for doing model building with SageMaker.

There are a number of SageMaker-Spark examples by AWS here : https://github.com/aws/sagemaker-spark

Fire SageMaker Processors
------------------

SageMaker Processors include:

* KMeansSageMakerEstimator


Setup
-----

AWS provides managed policies for SageMaker. Example : AmazonSageMakerFullAccess

We created a Role with 2 Policies:

* AmazonS3FullAccess
* AmazonSageMakerFullAccess

