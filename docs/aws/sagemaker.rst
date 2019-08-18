Fire Integration with SageMaker
========================

Fire is fully integrated with AWS SageMaker. Fire provides a number of processors for doing model building with SageMaker.

You can do Data Preparation and Feature Engineering with Sparkflows doing compute with Apache Spark. Sparkflows then seamlessly enables you to do your model training and deployment with SageMaker.

The above forms a very powerful combinations for end to end Machine Learning.

Spark Sagemaker Examples
------------------------

There are a number of SageMaker-Spark examples by AWS here : 

* https://github.com/aws/sagemaker-spark
* https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark-example1.html


Fire SageMaker Processors
------------------

SageMaker Processors include:

* KMeansSageMakerEstimator
* XGBoostSageMakerEstimator 
* LDASageMakerEstimator
* LinearLearnerBinaryClassifier
* LinearLearnerRegressor
* PCASageMakerEstimator
* SaveSageMaker

AWS Provided Policies
-----

AWS provides managed policies for SageMaker. Example : AmazonSageMakerFullAccess

Launching EMR
------------

When launching the EMR Cluster make sure that the Role (eg: **EMR_EC2_DefaultRole**) used has the AmazonSageMakerFullAccess policy. 

Now that the Roles and Policies are in place, start up your EMR cluser with the **EMR_DefaultRole** and  **EMR_EC2_DefaultRole** Roles.

Create New Role
--------------

Create a new Role called **aws-sagmaker-full-access** with the below Policy. It would be used in the Apache Spark job when accessing SageMaker.

* AmazonSageMakerFullAccess

Use ARN of the new Role in the Workflow
----------------

We now use the ARN of the new Role when we use the SageMaker KMeans Estimator Node in the Workflow.

**arn:aws:iam::account_id:role/aws-sagemaker-full-access**


AWS Instance Types
------------------

AWS has various instance types:

* p : GPU Instances
* c : Compute Instances
* r : Memory Optimized Instances
* m : General Instances

Amazon SageMaker Instance Types details are here : https://aws.amazon.com/sagemaker/pricing/instance-types/


Dataset Column Names for Training with Sagemaker
------------------------------------------------

Sagemaker needs the following columns to exist in the Dataset.

* label : label column
* features : features column, this column can also be set


Flow with Sparkflows and AWS
---------------------------

* We do the Data Preparation and Feature Generation in EMR with Sparkflows.
* When Sparkflows invokes the SageMakerEstimator, it calls SageMaker for Training and Deployment.
* Once the model is deployed on SageMaker, the endpoint can be used for realtime predictions.

XGBoost Sagemaker Workflow
---------------------

Below is a workflow which:

* Reads in a libsvm file as input
* Performs XGBoost Modeling
* Reads in another libsvm file
* Performs predictions with the model built in the previous step
* Prints out the result

.. figure:: ../_assets/aws/sagemaker-xgboost-workflow-1.png
   :alt: SageMaker XGBoost 
   :align: center
   
XGBoost Configuration
---------------

Below are the configuration setup details of the XGBoost Processor.

.. figure:: ../_assets/aws/sagemaker-xgboost-configuration-1.png
   :alt: SageMaker XGBoost Configuration
   :align: center

   
Executing the Workflow
------------------

Below are the results of executing the workflow.

.. figure:: ../_assets/aws/sagemaker-xgboost-execute-1.png
   :alt: SageMaker XGBoost Execution
   :align: center
   
   



