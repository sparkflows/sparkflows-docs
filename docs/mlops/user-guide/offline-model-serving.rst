Offline Model Serving
========

Once the training workflow completes, the model is saved into the Sparkflows model repository. The models can be picked up and served using one of the below approaches:

As Sparkflows Score Workflow
---------
* The model can be loaded in a Sparkflows workflow and then it can be used to score new data. 
* The same scoring workflow can be triggered via REST API to score the data.

As Python Scorer in Standalone Docker Image
-----------------
* Encapsulate the model inside a custom Docker image provided by Sparkflows.
* This image takes in the input file or directory of data as input, scores it and writes out the scored file.
* This docker image can run either on the same machine as Sparkflows or a different machine or in a Kubernetes cluster as a pod.

As Registered Models in MLflow
------------
* The model residing natively in the Sparkflows model registry can be logged and registered in MLflow by click of the **Register** button in the **Actions** menu. 
* Once the model is registered in MLflow, python script can be used to score batches of rows.

As MLflow Scoring Container in Sagemaker
-------------
* Please contact us to deploy the model in Sagemaker.

As MLflow Scoring Container in AzureML
--------------
* Please contact us to deploy the model in AzureML.
