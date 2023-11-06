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
    * One would need an MLflow server installed and running. The steps to install the same can be found in the official documentation of MLflow here - `MLflow Quickstart Guide <https://mlflow.org/docs/latest/quickstart.html>`_
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

    * When the MLflow server is run a remote machine, below setup needs to be done:

       * Start the Fire MLOps server alongside the MLflow server
       * Ensure the Saprkflows machine can talk to the configured port of the Fire MLOps server
       * Ensure that the ports where the models will be served are open to be accessed via REST API 
       * Ensure the credentials for the MLflow model registry store is configured in Sparkflows. Eg: If `s3` is used as the MLflow regsitry store, its exposed to the Fire MLOps server.
