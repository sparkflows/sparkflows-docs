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
  * The details of end point and command to score test data shows up in the Sparkflows model registry once the model is deployed on Sagemaker.

As Registered Models in SageMaker
-----------
Sparkflows MLOps allows you to deploy Machine learning models on Sagemaker. These models can be either built in Sparkflows or models built outside of Sparkflows can also be onboarded and served.

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
      :alt: MLOps Sagemaker
      :width: 60%

#. Once the model is imported into Sparkflows,the Register, Deploy, Undeploy of the model behaves the same way as any other model.

As Registered Models in Kubeflow
-----------
Sparkflows MLOps allows you to deploy Machine learning models in Kubeflow. These models can be either built in Sparkflows or models built outside of Sparkflows can also be onboarded and served.

Once the configurations are done, we can import external models and deploy it to Kubeflow. The steps for the same are below:

#. Import the model into Sparkflows if its an external model.
#. Register the model by clicking on Register model in the models page
#. Deploy the model to Kubeflow by click on Deploy model in the models page Actions menu. This will open up a dialog box as seen below which expects users inputs. Once inputs are provided, click on `Ok` and it would deploy the model to Kubeflow. Here if you want to use an existing docker image, then provide the docker image tag. But, if you want Sparkflows to build the docker image, just provide the `Docker context path` with the required files and the docker image will be built using a base image and the model will be embedded into it and deployed to kubeflow automatically.

   .. figure:: ../../_assets/mlops/kubeflow/kubeflow-deployment-details.png
      :alt: MLOps Kubeflow
      :width: 60%

#. On deployment, you will get a live end point which can be used to score using the deployed model in Kubeflow. There are multiple ways by which the live end point can be used to score. The same with examples of how to do it is below::


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
    
