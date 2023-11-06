As Registered Models in SageMaker
=================

Sparkflows MLOps allows you to deploy Machine learning models on SageMaker. These models can be either built in Sparkflows or models built outside of Sparkflows can also be onboarded and served.

Admin Guide
-----
Below we go through the admin guide of different options available in Sparkflows MLOps to deploy models.

Configure the below from the MLOps tab in Admin page:

* mlops.region
* mlops.aws_id 
* Mlops.arn

  .. figure:: ../../_assets/mlops/sagemaker/sagemaker-1.png
     :alt: mlops-sagemaker
     :width: 60%

  
  .. figure:: ../../_assets/mlops/sagemaker/sagemaker-2.png
     :alt: mlops-sagemaker
     :width: 60%

Push the MLflow docker image to ECR to be used for deploying the model. To begin with, one can just push the default mlflow docker image.

To Push the docker image to ECR, you would need to perform the following steps:
  
#. Use the get-login-password command that retrieves and displays an authentication token using the GetAuthorizationToken API that we can use to authenticate to an Amazon ECR registry. Use the same region_name that you used while creating a repo. Store the encrypted token somewhere for a moment.

   ::
     
      aws ecr get-login-password --region <region_name>

#. We need two things. The first is the token I just mentioned and second is the repository URI from the previous step.

   ::
  
      aws ecr --region <region> | docker login -u AWS -p <encrypted_token> <repo_uri>

   We are querying the ECR API provided by AWS CLI. Later we are pipelining Docker login.
  
   - -u AWS: Default user provided by AWS.
   - -p <encrypted_token>: Password we retrieved in the last step.
   - repo_uri: URI of our repository.

   If the login is successful, **Login Succeeded** will be displayed in the terminal.

#. Push the docker image:

   ::

      mlflow sagemaker build-and-push-container

