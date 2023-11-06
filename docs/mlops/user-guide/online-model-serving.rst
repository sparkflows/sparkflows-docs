Online Model Serving
==========

Online serving can be performed in any one of the following ways:

As Sparkflows Score Workflow
-----------
* The workflow can be triggered via REST API to score the data.

  An example request for Executing specified workflow:

  ::
   
       curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{
       "emailOnFailure": "string",
       "emailOnSuccess": "string",
       "libJars": "string",
       "programParameters": "string",
       "sparkConfig": "string",
       "workflowId": 1
       }' 'http://hostname:port/api/v1/workflow/execute' -b /tmp/cookies.txt
   

As REST End Point in Standalone Docker Image
---------------
* Encapsulate the model inside a custom Docker image provided by Sparkflows.
* The model is then loaded and served as a REST end point.
* This docker image can run either on the same machine as Sparkflows or a different machine or in a Kubernetes cluster as a pod.

As Registered Models in MLflow
---------
* The model residing natively in the Sparkflows model registry can be logged and registered in MLflow by click of the **Register** button in the **Actions** menu. 
* Once the model is registered in MLflow, it can be served as a REST end point via click of a **Deploy** model in the **Actions** menu of Sparkflows model registry. The option to **Deploy** gets enabled for a model only if it has been logged and registered in MLflow.
* Once the model is deployed, the REST end point and the python/curl commands to use the end point to score also shows up in the same **Action** menu. The python script can be copied and used to score sample data. Same holds true for the curl sample command. The sample code is generated only for the models which have been deployed.
* If the model is no longer needed to be served, they can be **Undeployed** by click of the **Undeploy** model option in the **Actions** menu. The option to **Undeploy** gets enabled only for models deployed.
* If for some reason, you want to re-register the model, once can click on the **Re-register** option to register the model again.

  .. figure:: ../../_assets/mlops/mlops_mlflow_api_end_point.png
     :alt: MLflow end point
     :width: 60%

As Registered Models in SageMaker
----------

Sparkflows MLOps allows you to deploy Machine learning models on SageMaker. These models can be either built in Sparkflows or models built outside of Sparkflows can also be onboarded and served.

Below we go through the admin guide of different options available in Sparkflows MLOps to deploy models:

* Configure the below from the MLOps tab in Admin page:

  * mlops.region
  * mlops.aws_id 
  * Mlops.arn

    .. figure:: ../../_assets/mlops/sagemaker/sagemaker-1.png
       :alt: mlops-sagemaker
       :width: 60%

  
    .. figure:: ../../_assets/mlops/sagemaker/sagemaker-2.png
       :alt: mlops-sagemaker
       :width: 60%

* Push the MLflow docker image to ECR to be used for deploying the model. To begin with, one can just push the default mlflow docker image.

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

As MLflow Scoring Container in Sagemaker
---------
* The model residing natively in the Sparkflows model registry can be logged and registered in MLflow by click of the **Register** button in the **Actions** menu. 
* Then, it can be deployed to Sagemaker by click of the **Deploy to Sagemaker** button. What happens under the hood is as below:
  
  * Sparkflows pushes/uses a custom Sparkflows container to ECR registry.
  * Then, deploys the model in the same container on Sagemaker.
  * The Sagemaker then creates a REST end point for serving the model.
  * The details of end point and command to score test data shows up in the Sparkflows model registry once the model is deployed on Sagemaker.

* Once deployed, the deployment shows up as below:

  .. figure:: ../../_assets/mlops/mlops-sagemaker-deployment-2.png
     :alt: MLops Sagemaker
     :width: 60%

* The details of the deployment can be seen below:

  .. figure:: ../../_assets/mlops/mlops-sagemaker-deployment-1.png
     :alt: MLops Sagemaker
     :width: 60%

As Registered Models in SageMaker
-----------

Once the configurations are done, we can import external models and deploy it to SageMaker. The steps for the same are below:

#. Import the model: The custom model needs to override a class named **CustomPreprocessor**  in a python filename **custom_preprocess.py**. The skeleton of the same can be found attached. These files along with any other code file and artifacts to be used for deployment needs to be packaged in the directory structure as below:

   ::
     
     model_bundle
          artifacts
                 first_model.pkl
                 second_model.pkl
     code
                 first_code.py
                 second_code.py
     requirements.txt

#. Once, the files are ready in the above structure, zip them up and then they can be imported in Sparkflows in the models page by choosing the Import option.  

   .. figure:: ../../_assets/mlops/sagemaker/sagemaker-1.png
      :alt: MLops Sagemaker
      :width: 60%

#. Once the model is imported into Sparkflows,the Register, Deploy, Undeploy of the model behaves the same way as any other model.


As MLflow Scoring Container in AzureML
-----------

* The model residing natively in the Sparkflows model registry can be logged and registered in MLflow by click of the **Register** button in the **Actions** menu. 
* Then, it can be deployed to Sagemaker by click on the **Deploy to AzureML** button. What happens under the hood is as below:

  * Sparkflows pushes/uses a custom Sparkflows container to Azure registry.
  * Then, deploys the model in the same container on AzureML.
  * The AzureML then creates a REST end point for serving the model.
  * The details of end point and command to score test data shows up in the Sparkflows model registry once the model is deployed on Sagemaker.


