Workflow Execution API
======================

List all Executions
------------------------

.. list-table:: 
   :widths: 40 40
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

    {"status":"ok","message":"Stopping Analysis Flow Execution"}

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

    Killed YARN application : yarn application -kill application_1560754639341_5930,Exit Value : 0
    
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

    Workflow executions deleted successfully

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

    [
    {
    "id": 193,
    "userId": 33,
    "uuid": "9213211a-c0ae-40e0-be80-824800e06d82",
    "name": "string",
    "category": "string",
    "content": "{\"name\":\"string\",\"uuid\":\"9213211a-c0ae-40e0-be80-824800e06d82\",\"category\":\"string\",\"description\":\"string\",\"parameters\":\"string\",\"nodes\":[{\"id\":\"string\",\"path\":\"string\",\"name\":\"string\",\"iconImage\":\"string\",\"description\":\"string\",\"details\":\"\",\"examples\":\"\",\"type\":\"string\",\"nodeClass\":\"string\",\"x\":\"string\",\"y\":\"string\",\"fields\":[{\"name\":\"string\",\"value\":\"string\",\"widget\":\"string\",\"title\":\"string\",\"description\":\"string\",\"optionsMap\":{},\"datatypes\":[\"string\"],\"optionsArray\":[\"string\"],\"required\":true,\"display\":true,\"editable\":true,\"disableRefresh\":true}],\"engine\":\"string\"}],\"edges\":[{\"source\":\"string\",\"target\":\"string\",\"id\":0}],\"dataSetDetails\":[],\"engine\":\"string\"}",
    "description": "string",
    "version": 0,
    "dateCreated": 1566831921251,
    "dateLastUpdated": 1566831921251,
    "lockedByUserId": null,
    "permission": null,
    "workflow": {
      "name": "string",
      "uuid": "9213211a-c0ae-40e0-be80-824800e06d82",
      "category": "string",
      "description": "string",
      "parameters": "string",
      "nodes": [
        {
          "id": "string",
          "path": "string",
          "name": "string",
          "iconImage": "string",
          "description": "string",
          "details": "",
          "examples": "",
          "type": "string",
          "nodeClass": "string",
          "x": "string",
          "y": "string",
          "fields": [
            {
              "name": "string",
              "value": "string",
              "widget": "string",
              "title": "string",
              "description": "string",
              "optionsMap": {},
              "datatypes": [
                "string"
              ],
              "optionsArray": [
                "string"
              ],
              "required": true,
              "display": true,
              "editable": true,
              "disableRefresh": true
            }
          ],
          "engine": "string"
        }
      ],
      "edges": [
        {
          "source": "string",
          "target": "string",
          "id": 0
        }
      ],
      "dataSetDetails": [],
      "engine": "string",
      "h2OWorkflow": false
    },
    "projectId": 33,
    "engine": "string"
    },   
