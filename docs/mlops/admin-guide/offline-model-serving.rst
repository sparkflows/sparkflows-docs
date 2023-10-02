Offline Model Serving Admin guide
========
Offline model serving can be done in any of the following ways :

Using Sparkflows Score Workflow
---------
   * There is no additional administrative configuration needed as the model is served as any other workflow. It just needs a running instance of Sparkflows server.

Using Python Scorer in Standalone Docker Image
-------------

    * As an admin you would need to pull the custom scorer docker image of Sparkflows which has all the pre-requisites.
    * This docker image is linked to a specific release of Sparkflows. You need to ensure that the right image is downloaded/pulled.
    * The Machine learning model needs to be downloaded from the Sparkflows model repository.
    * The model is then mounted into the docker and the corresponding docker run command needs to be executed.
    * Then, the test data can be passed into the running image to be scored.

Using Registered Models in MLflow
--------------
    * One would need an MLflow server installed and running. The steps to install the same can be found in the official documentation of MLflow here - https://mlflow.org/docs/latest/quickstart.html
    * Need to add the below installed on the MLflow instance
        * jdk 1.8
        * Python 3.7
        * Sparkling water: pip install h2o-pysparkling-3.2==3.36.1.2.post
        * PySpark: pip install pyspark==3.2.1
        * MLflow: pip install mlflow==1.30.1
        * boto3: pip install --upgrade boto3
        * Flask: pip install Flask==2.2.4
    * Once the MLFlow server is up and running, the following configurations needs to be added in the **Administrative tab** in the section **Configuration** and sub-section **MLflow** :
   
       * MLflow server URL (tracking URL).
       * MLflow login username, if any.
       * MLflow login password, if any.


      .. figure:: ../../_assets/mlops/mlops_mlflow_local.png
       :alt: Load balancers
       :width: 60%
