Invoke Azure Functions
======================

This node invokes Azure Functions and allows triggering Azure Function endpoints using GET or POST methods from the pipeline using Airflow.

Connection Configuration
------------------------

Create an Azure Workspace connection, then sync this connection with Airflow by selecting the Azure Workspace connection under Sparkflows Airflow Connection.

**Azure Workspace Connection**
+++++++++++++++++++++++++++++++

.. figure:: ../../_assets/user-guide/pipeline/azure-functions/azure_workspace_con1.png
      :alt: Pipeline List
      :width: 70%
  
- **Client Id**: The Application (Client) ID from Azure App Registration. Used to identify your Azure application during authentication.
- **Client Secret**: Secret key/password generated for the Azure App Registration. Used with the Client ID for secure authentication.
- **Tenant Id**: Your Azure Directory (Tenant) ID. Identifies which Azure organization/account owns the app.
- **Scope**: Defines what API/resource access token should be requested.
- **Function Key**: Authorization key for Azure Functions. Used when calling secured Azure Function endpoints.

**Airflow Connection**
+++++++++++++++++++++++++++++

.. figure:: ../../_assets/user-guide/pipeline/azure-functions/airflow_azure_sync.png
      :alt: Pipeline List
      :width: 70%

Node Field Descriptions
-----------------------

+----------------+---------------------------------------------------------------+-------------+
| Field          | Description                                                   | Requirement |
+================+===============================================================+=============+
| Task Name      | Provide a unique name for this task to track it in the DAG.   | Required    |
+----------------+---------------------------------------------------------------+-------------+
| Function URL   | Specify the Azure Function URL to be triggered.               | Required    |
+----------------+---------------------------------------------------------------+-------------+
| Method Type    | Choose the HTTP method: GET or POST.                          | Required    |
+----------------+---------------------------------------------------------------+-------------+
| Query Params   | Used only for GET requests. Add key/value query parameters.   | Conditional |
+----------------+---------------------------------------------------------------+-------------+
| Payload        | Used only for POST requests. Add key/value payload entries.   | Conditional |
+----------------+---------------------------------------------------------------+-------------+
| Trigger Rule   | Airflow trigger rule controlling task execution.              | Required    |
+----------------+---------------------------------------------------------------+-------------+

.. figure:: ../../_assets/user-guide/pipeline/azure-functions/invoke_func_pipeline_1.png
      :alt: Pipeline List
      :width: 70%
  
GET Example Configuration
-------------------------

.. code-block:: json

   {
     "Name": "invoke_customer_status",
     "functionUrl": "https://myapp.azurewebsites.net/api/customerStatus",
     "methodType": "GET",
     "queryParams": [
       {"Key":"name","Value":"admin"},
       {"Key":"path","Value":"s3://abc"}
     ],
     "AzureConnectionId": "Azure_Workspace_Connection_18",
     "trigger_rule": "all_success"
   }

.. figure:: ../../_assets/user-guide/pipeline/azure-functions/invoke_func_pipeline_3.png
      :alt: Pipeline List
      :width: 70%

POST Example Configuration
--------------------------

.. code-block:: json

   {
     "Name": "invoke_create_order",
     "functionUrl": "https://myapp.azurewebsites.net/api/createOrder",
     "methodType": "POST",
     "payload": [
       {"Key":"name","Value":"admin"},
       {"Key":"path","Value":"s3://abc"}
     ],
     "AzureConnectionId": "Azure_Workspace_Connection_18",
     "trigger_rule": "all_success"
   }


.. figure:: ../../_assets/user-guide/pipeline/azure-functions/invoke_func_pipeline_2.png
      :alt: Pipeline List
      :width: 70%


.. note::

    - Use Query Params only when Method Type is GET.
    - Use Payload only when Method Type is POST.
    - Ensure the Azure Connection has permission to access the function.
    - Task Name should be unique within the DAG.
