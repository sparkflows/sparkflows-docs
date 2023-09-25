Offline Model Serving
========
Offline model serving can be done in any of the following ways :

As Sparkflows Score Workflow
---------
   * There is no additional administrative configuration needed as the model is served as any other workflow. It just needs a running instance of Sparkflows server.

As Python Scorer in Standalone Docker Image
-------------

    * As an admin you would need to pull the custom scorer docker image of Sparkflows which has all the pre-requisites.
    * This docker image is linked to a specific release of Sparkflows. You need to ensure that the right image is downloaded/pulled.
    * The Machine learning model needs to be downloaded from the Sparkflows model repository.
    * The model is then mounted into the docker and the corresponding docker run command needs to be executed.
    * Then, the test data can be passed into the running image to be scored.

As Registered Models in MLflow
--------------
    * One would need an MLflow server installed and running. The steps to install the same can be found in the official documentation of MLflow here - https://mlflow.org/docs/latest/quickstart.html
    * Once the MLFlow server is up and running, the following configurations needs to be added in the **Administrative tab** in the section **Configuration** and sub-section **MLflow** :
   
       * MLflow server URL (tracking URL).
       * MLflow login username, if any.
       * MLflow login password, if any.

