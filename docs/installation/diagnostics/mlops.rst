Mlops
======
The MLOps section in Diagnostics allows users to validate the configured connection and ensure that all deployed models have unique endpoints, helping maintain seamless integration and deployment.  

To validate MLOps Connection and Deployed Models' Endpoints, follow these steps:

Step 1 : Testing MLOps Connection
+++++

#. Login to **Sparkflows** and navigate to **Administration -> Diagnostics -> MLOps**.

#. To test the MLOps connection configured in the application's settings, click on **Test MLOps Connection** button. The system will check the connection and display the result as shown below.

 .. figure:: ../../_assets/diagnositcs/diagnostics-mlops/mlops-test-connection-error.png
    :alt: mlops test connection
    :width: 60%

Step 2 : Verifying Deployed Models' Endpoint Uniqueness
+++++

#. To verify that all deployed models have unique endpoints, click on **Check Deployed Models Endpoints Unique** button. The system will verify whether all deployed models have unique endpoints and display the results as shown below. 

 .. figure:: ../../_assets/diagnositcs/diagnostics-mlops/diagnostics-mlops-check-deployed-models.png
    :alt: mlops test deployed models end point
    :width: 60%

 .. figure:: ../../_assets/diagnositcs/diagnostics-mlops/diagnostics-mlops-no-same-endpoints.png
    :alt: mlops test deployed models end point
    :width: 60%

