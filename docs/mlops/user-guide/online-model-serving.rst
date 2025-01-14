Online Model Serving
==========
**Online model serving** is the process of deploying machine learning models in a way that allows them to handle real-time predictions or inference requests. These models are hosted on servers or cloud platforms and respond to incoming requests (e.g., via APIs) with predictions instantly or within milliseconds.

Online model serving can be performed using one of the ways listed below:

* As Registered Models in Kubeflow
* As Registered Models in Sagemaker
* As Registered Models in MLflow
* As MLflow Scoring Container in Sagemaker
* As MLflow Scoring Container in AzureML
* As Sparkflows Score Workflow
* As REST end point in a Standalone Docker Image


As Registered Models in Kubeflow
-----------
Sparkflows MLOps enables you to deploy machine learning models to Kubeflow, which we recommend as the preferred approach. These models can be trained directly within Sparkflows or imported from an external system and served.

Once the required configurations are completed by an Admin, one can deploy the models and the entire pipeline to Kubeflow with just a few clicks. The steps for the same are as follows:

#. **Train/Import the Model:** Train the model using Sparkflows workflows, or import an external model into Sparkflows.
#. **Model Registration:** Once the model is trained/imported, it is automatically registered in the Sparkflows Model Registry. 
#. **Deploy to Kubeflow:** To deploy the model, follow the steps below:

   * Navigate to the **Models page** and select **Deploy Model** from the **Actions menu**.

   * A dialog box will appear for user inputs, as shown below. Once you provide the required information, click the **OK** to deploy the model to Kubeflow.

     .. figure:: ../../_assets/mlops/kubeflow/kubeflow-deployment-details.png
        :alt: MLOps Kubeflow
        :width: 60%

   If you want to use an existing Docker image, provide the **Docker Image Tag**.
   Alternatively, to have Sparkflows build the Docker image, specify the **Docker Context Path** along with the necessary files. Sparkflows will use a base image to build the Docker image, embed the model into it, and deploy it to Kubeflow automatically.

#. Upon deployment, you will receive a live endpoint that can be used to score with the deployed model in Kubeflow. There are several ways to use this live endpoint for scoring, with examples provided below::


    # To score using the mlops-monitoring end point
    import json
    import requests
    import pandas as pd
    
    test_data = pd.read_csv('/home/user/ubuntu/test.csv')
    model_id = 361 # This is the id of the model which you want to use to score
    token = 'xxxxxxxxx' # Retrieve/Create it from Sparkflows user profile page
    
    http_data = test_data.to_json(orient='split')
    scoring_api_url = 'http://XX.15.YYY.171:8080/api/v1/score-models?modelId='+ str(model_id)
    api_call_headers = {'token': token}
    response = requests.post(scoring_api_url, data=http_data, headers=api_call_headers)
    print(response.text)
    
    # Score via Python
    import json
    import requests
    import pandas as pd
    test_data = pd.read_csv('/home/ubuntu/test.csv')
    http_data = test_data.to_json(orient='split')
    json_data = json.loads(http_data)
    response = requests.post('http://172.174.173.7:5078/predict', json=json_data)
    print(response.json())
    
    # Score via curl
    curl -X POST -H 'Content-Type: application/json' -d '{'feature1': 1.0,'feature2': 'this is spam','feature3': 2.0}' http://172.174.173.7:5078/predict

As Registered Models in Sagemaker
-----------
Sparkflows MLOps enables the deployment of machine learning models on SageMaker. These models can either be built within Sparkflows or imported from external sources for serving.

Once the configurations are complete, external models can be imported and deployed to SageMaker. The steps for the same are as follows:

#. **Import the model:** The custom model should override a class named **CustomPreprocessor** in a Python file named **custom_preprocess.py**. A skeleton for this file is provided. Along with this file, include any other necessary code files and artifacts required for deployment. These files should be packaged in the directory structure given below:

   ::
     
     model_bundle
          artifacts
                 first_model.pkl
                 second_model.pkl
     code
                 first_code.py
                 second_code.py
     requirements.txt

#. **Prepare and Zip the Files for Import:** Once the files are organized in the above structure, zip them and import them into Sparkflows from the **Models page** by clicking the **Import** button.

   .. figure:: ../../_assets/mlops/sagemaker/sagemaker-1.png
      :alt: MLOps Sagemaker
      :width: 60%

#. **Manage the Model (Register, Deploy, Undeploy):** Once the model is imported into Sparkflows, the processes for Registering, Deploying, and Undeploying the model follow the same procedure as any other model.

As Registered Models in MLflow
---------
To deploy the models to MLflow, follow the steps given below:

#. **Register the Model in MLflow:** The model stored in the Sparkflows Model Registry can be logged and registered in MLflow by clicking the Register button in the Actions menu.

#. **Deploy the Model as a REST Endpoint:** Once the model is registered in MLflow, it can be deployed as a REST endpoint by selecting **Deploy Model** in the Actions menu of the Sparkflows Model Registry. The **Deploy** option will only be available for models that have been logged and registered in MLflow.

#. **Access Scoring Information:** Follow the steps below:
  
   * After deployment, the REST endpoint, along with Python/cURL commands to score the model, will appear in the same Actions menu.
   * You can copy the Python script or cURL sample command to use for scoring sample data.
   * Sample code is generated only for models that have been deployed.

#. **Undeploy the Model:** If the model is no longer needed for serving, it can be undeployed by clicking the **Undeploy** button in the Actions menu. The **Undeploy** option will only be enabled for models that are deployed.

#. **Re-register the Model:** If needed, you can Re-register the model by clicking the **Re-register** button to register the model again.

   .. figure:: ../../_assets/mlops/mlops_mlflow_api_end_point.png
      :alt: MLflow end point
      :width: 60%

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

As MLflow Scoring Container in AzureML
-----------

* The model residing natively in the Sparkflows model registry can be logged and registered in MLflow by click of the **Register** button in the **Actions** menu. 
* Then, it can be deployed to Azure by click on the **Deploy to AzureML** button. What happens under the hood is as below:

  * Sparkflows pushes/uses a custom Sparkflows container to Azure registry.
  * Then, deploys the model in the same container on AzureML.
  * The AzureML then creates a REST end point for serving the model.
  * The details of end point and command to score test data shows up in the Sparkflows model registry once the model is deployed on AzureML.

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
   

As REST end point in a standalone Docker image
---------------
* Encapsulate the model inside a custom Docker image provided by Sparkflows.
* The model is then loaded and served as a REST end point.
* This docker image can run either on the same machine as Sparkflows or a different machine or in a Kubernetes cluster as a pod.
