Workflow Execution REST API
============================

Overview
--------
 
The Workflow Execution REST API's, allow you to execute Workflows, get results etc.

Below are the various Workflow Execution API's available in Fire Insights, They should be executed after you have logged into Fire Insights.



Execute Workflow
------------------

Execute specified Workflow.

An Example request for Executing specified workflow:

::
   
   curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{
  "emailOnFailure": "string",
  "emailOnSuccess": "string",
  "libJars": "string",
  "programParameters": "string",
  "sparkConfig": "string",
  "workflowId": 1
  }' 'http://hostname:port/api/v1/workflow/execute' -b /tmp/cookies.txt
   

An Example response:

::

    162

List all the Executions
------------------------

List all the workflow executions.

An example request for List all the executions:

::

    curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflow-executions?page=0&size=1000' -b /tmp/cookies.txt
    
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
    
    
  
List Executions of a Workflow
------------------------------
 
Return the list of Executions for given workflowId.

workflowId = 131::

An Example request for List executions of a Workflow::

  curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflow-executions/workflows/131' -b /tmp/cookies.txt

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
  
Stop the Execution of workflow
--------------------------------
 
Stops the execution of workflow with specified workflowExecutionId.

Workflow Execution Id = 100::

An Example request for Stopping specified workflow:

::

  curl -X GET --header 'Accept: text/plain' 'http://hostname:port/api/v1/workflow-execution/100/stop'' -b /tmp/cookies.txt
  
An Example response:

::

    {"status":"ok","message":"Stopping Analysis Flow Execution"}
  
Kill the Execution of workflow
------------------------------
 
Kill the execution of workflow with specified workflowExecutionId.

Workflow Execution Id = 100::

An example request for Killing specified workflow::

  curl -X GET --header 'Accept: text/plain' 'http://hostname:port/api/v1/workflow-execution/100/kill' -b /tmp/cookies.txt

An Example response:

::

    Killed YARN application : yarn application -kill application_1560754639341_5930,Exit Value : 0
  
 
  
Delete Workflow Executions by days
----------------------------------
 
Delete Workflow Executions by days
 
"days": "7"::

An example request for deleting workflow executions by days::

  curl -X DELETE --header 'Accept: text/plain' 'http://hostname:port/api/v1/workflow-executions/days/7' -b /tmp/cookies.txt
  

An Example response:

::

    Workflow executions deleted successfully

Get Executed Task Count
-----------------------

Get Executed Task Count:

An example request for Getting Executed Task Count::

  curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflow-executions/tasks/count' -b /tmp/cookies.txt
  

An Example response:

::

    92

Get Latest Executions
---------------------

Get Latest Executions:

An Example request for Getting Latest Executions::

  curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflow-executions/latest' -b /tmp/cookies.txt
   
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

