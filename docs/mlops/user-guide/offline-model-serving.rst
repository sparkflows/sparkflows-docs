Offline Model Serving
========

Once the training workflow completes, the model is saved into the Sparkflows model repository. The models can be picked up and served using one of the below approaches:

As Sparkflows Score Workflow
---------
  * The model can be loaded in a Sparkflows workflow and then it can be used to score new data. 
  * The scoring workflow can also be triggered via REST API to score the data.

    .. figure:: ../../_assets/mlops/mlops_workflow_score.png
       :alt: Load balancers
       :width: 60%

As Python Scorer in Standalone Docker Image
-----------------
  * Encapsulate the model inside a custom Docker image provided by Sparkflows.
  * This image takes in the input file or directory of data as input, scores it and writes out the scored file.
  * This docker image can run either on the same machine as Sparkflows or a different machine or in a Kubernetes cluster as a pod.

As Registered Models in MLflow
------------
  * The model residing natively in the Sparkflows model registry can be logged and registered in MLflow by click of the **Register** button in the **Actions** menu. 
  * Once the model is registered in MLflow, python script can be used to score batches of rows.

    .. figure:: ../../_assets/mlops/mlops_mlflow_score.png
       :alt: Load balancers
       :width: 60%

As MLflow Scoring Container on Sagemaker in batch mode
-------------
  * Please contact us to deploy the model in Sagemaker. The model can be deployed to Sagemaker by click of a button from Sparkflows.


As MLflow Scoring Container on AzureML in batch mode
--------------
  * Please contact us to deploy the model in AzureML. The model can be deployed to AzureML by click of a button from Sparkflows.
