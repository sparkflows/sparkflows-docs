Online Model Serving
=======
Online model serving can be done in any of the following ways :

As Sparkflows Score Workflow
---------
  * There is no additional administrative configuration needed as the model is served as any other workflow. It just needs a running instance of Sparkflows server.

As REST End Point in Standalone Docker Image
------------
  * As an admin you would need to pull the custom scorer docker image of Sparkflows which has all the pre-requisites.
  * This docker image is linked to a specific release of Sparkflows. You need to ensure that the right image is downloaded/pulled.
  * The Machine learning model needs to be downloaded from the Sparkflows model repository.
  * The docker run command when executed, loads the model and exposed a REST end point which can be used from outside the container to score data.

As Registered Models in MLflow
------------
  * One would need an MLflow server installed and running. The steps to install the same can be found in the official documentation of MLflow here - `MLflow Quickstart Guide <https://mlflow.org/docs/latest/quickstart.html>`_
  * Ensure that the port 5000 onwards on the MLflow machine is free to be exposed as end point to deploy models
  * Ensure the port 8086 (or the port where the MLOps server is started) is open on the machine.
  * Prerequisites on the MLflow instance
       * JDK 1.8
       * Python 3.7
       * Sparkling water: pip install h2o-pysparkling-3.2==3.36.1.2.post
       * PySpark: pip install pyspark==3.2.1
       * MLflow: pip install mlflow==1.30.1
       * boto3: pip install boto3==1.28.50
       * Flask: pip install Flask==2.2.4
       * Click: pip install click==8.1.3
       * Tornado: pip install tornado==6.2
       * Pylint: pip install pylint==2.5.3
       * NumPy: pip install numpy==1.21.6

  * Once the MLFlow server is up and running, the following configurations needs to be added in the **Administrative tab** in the section **Configuration** and sub-section **MLflow** :
   
       * MLflow server URL (tracking URL).
       * MLflow login username, if any.
       * MLflow login password, if any.
       * MLflow deploy mode: In production, it should be set to `fire_mlops_server`wherein Sparkflows and MLflow run on seperate machines. The other options are `local` when Sparkflows and MLflow are hosted on same machine, and `remote` if Sparkflows and MLflow server have ssh access to each other and hosted on different machines.
       * Fire MLOps Host and Port: When the MLflow is hosted on remote server, the host and port of Sparkflows MLOps server needs to be configured here.

         .. figure:: ../../_assets/mlops/mlops_mlflow_local.png
            :alt: Load balancers
            :width: 60%

  * If the MLflow server is local to the Sparkflows instance, the above configurations are sufficient. But, if the MLflow server is running remotely, say on AWS or on cloud, then additional configuration listed below would need to be configured.
   
      * The Sparkflows machine would need SSH access to the MLflow server.
      * The path of SSH key of the MLflow server needs to be available to Sparkflows which can reside on disk , secure storage on a key vault to be pulled from.

        .. figure:: ../../_assets/mlops/mlops_mlflow_remote.png
           :alt: Load balancers
           :width: 60%

  * When the MLflow server is run a remote machine, below setup needs to be taken care of:

       * Start the Fire MLOps server alongside the MLflow server
       * Ensure the port 8086 (or the port where the MLOps server is started) is open on the machine.
       * Ensure the Sparkflows machine can talk to the configured port of the Fire MLOps server
       * Ensure that the ports where the models will be served are open to be accessed via REST API 
       * Ensure the credentials for the MLflow model registry store is configured in Sparkflows. Eg: If `s3` is used as the MLflow regsitry store, its exposed to the Fire MLOps server.

         .. figure:: ../../_assets/mlops/mlops-mlflow-remote-server.png
            :alt: Load balancers
            :width: 60%
As Registered Models in SageMaker
----------

Sparkflows MLOps allows you to deploy Machine learning models on SageMaker. These models can be either built in Sparkflows or models built outside of Sparkflows can also be onboarded and served.

Below we go through the admin guide of different options available in Sparkflows MLOps to deploy models:

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
