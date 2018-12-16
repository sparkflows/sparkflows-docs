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

Update EMR_EC2_DefaultRole
+++++++++++++++++++++++++++

We updated the **EMR_EC2_DefaultRole** role to also have the AmazonSageMakerFullAccess Policy:

* AmazonElasticMapReduceforEC2Role
* AmazonSageMakerFullAccess


Create New Role
+++++++++++++++

We created a new Role called **aws-sagmaker-full-access** with 2 Policies:

* AmazonS3FullAccess
* AmazonSageMakerFullAccess

Use ARN of the new Role
+++++++++++++++++++++++

We now use the ARN of the new Role when we use the SageMaker KMeans Estimator.

arn:aws:iam::account_id:role/aws-segmaker-full-access

