Workflow Execution API
======================

Execute
------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow/execute
     - POST
     
An Example request to Execute specific workflow:   

::

    {
     "emailOnFailure": "string",
     "emailOnSuccess": "string",
     "libJars": "string",
     "programParameters": "string",
     "sparkConfig": "string",
     "workflowId": 1
    },

Request Structure

For Executing specific workflow, we need to add below parameters

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
      
   * - workflowId
     - The canonical identifier of the workflow to Execute. This field is required.
     

An Example response:

::

   200


List all Executions
------------------------

.. list-table:: 
   :widths: 20 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions?page=0&size=1000
     - GET
     
Request Structure

For Listing all the executions, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - page
     - The number of pages can be added.
   
   * - size
     - The different size can be added. 
     
An Example response:

::

   [
   {
    "id": 135,
    "analysisFlowId": 161,
    "userId": 33,
    "projectId": 33,
    "analysisFlowScheduleId": null,
    "status": 2,
    "name": "Test_csv",
    "category": "-",
    "description": "Fired Manually",
    "logs": "/tmp/fire/workflowlogs/workflow-5342148677548385044.log",
    "fireJobId": "02aedbe5-0713-4172-9f7c-c63272f7cbd9",
    "applicationId": "application_1560754639341_5932",
    "uiWebUrl": "http://hostname:4042",
    "metrics": null,
    "startTime": 1566821007783,
    "endTime": 1566821024075,
    "emailOnSuccess": null,
    "emailOnFailure": null
   },
   
List Executions of Workflow
------------------------------

.. list-table:: 
   :widths: 30 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions/workflows/{workflowId}
     - GET
     
Request Structure

For Listing executions of a workflow, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - workflowId
     - The canonical identifier of the List execution of workflow. This field is required.   
     
An Example response:

::

    [
    {
    "id": 99,
    "analysisFlowId": 131,
    "userId": 33,
    "projectId": 33,
    "analysisFlowScheduleId": null,
    "status": 2,
    "name": "Test_workflow",
    "category": "-",
    "description": "Fired Manually",
    "logs": "/tmp/fire/workflowlogs/workflow-4439919411814145818.log",
    "fireJobId": "7b7b7dd5-b27b-419e-b853-794b5f53a5b8",
    "applicationId": "application_1560754639341_5929",
    "uiWebUrl": "http://hostname:4041",
    "metrics": null,
    "startTime": 1566795625424,
    "endTime": 1566795650970,
    "emailOnSuccess": null,
    "emailOnFailure": null
   }
   ],    

Stops workflow Execution
------------------------

.. list-table:: 
   :widths: 40 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-execution/{workflowExecutionId}/stop
     - GET
     
Request Structure

For Stopping execution of a workflow, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - workflowExecutionId
     - The canonical identifier of the Execution of workflow. This field is required.   
     
An Example response:

::

    200

Kill workflow Execution
-----------------------

.. list-table:: 
   :widths: 40 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-execution/{workflowExecutionId}/kill
     - GET
     
Request Structure

For Killing execution of a workflow, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - workflowExecutionId
     - The canonical identifier of the Execution of workflow. This field is required.   
     
An Example response:

::

    200
    
Delete Workflow Executions by days
-----------------------------------

.. list-table:: 
   :widths: 30 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions/days/{days}
     - DELETE
     
Request Structure

For deleting execution of a workflow, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - days
     - The canonical identifier of the Execution of workflow. This field is required.   
     
An Example response:

::

    200

Get Executed Task Count
-----------------------

.. list-table:: 
   :widths: 30 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions/tasks/count
     - GET
     
    
An Example response:

::

    200

Get Latest Executions
---------------------

.. list-table:: 
   :widths: 30 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions/latest
     - GET
     
An Example response:

::

    200     
