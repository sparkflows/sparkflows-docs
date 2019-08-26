Workflow Execution REST API
============================

Overview
--------
 
The Workflow Execution REST API's, allow you to execute Workflows, get results etc.

Below are the various Workflow Execution API's available in Fire Insights, They should be executed after you have logged into Fire Insights.



Execute a Workflow
------------------

Execute specified Workflow.

An example request for Executing specified workflow:

::
   
   curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{
  "emailOnFailure": "string",
  "emailOnSuccess": "string",
  "libJars": "string",
  "programParameters": "string",
  "sparkConfig": "string",
  "workflowId": 0
  }' 'http://hostname:port/api/v1/workflow/execute' -b /tmp/cookies.txt
   

An example response:

::

    200


Get Workflow Executions
----------------------------

Returns the list of Executions for the logged in user::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-executions'

View execution result of a given execution
------------------------------------------

AnalysisFlowExecutionId = 79

Type = 2::

  curl -X GET --header 'Accept: */*' 'http://localhost:8080/api/v1/execution-results/workflow-executions/79/resultType/{type}'
  
View executions of a Workflow
------------------------------
 
Return the list of Executions for given Analysis Flow Id.

workflowId = 81::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-executions/workflows/81'
  
Stop Executing a Workflow
-------------------------
 
Return the list of Executions for given Analysis Flow Id.

Workflow Execution Id = 1::

  curl -X GET --header 'Accept: text/plain' 'http://localhost:8080/api/v1/workflow-execution/1/stop'
  
View Spark Log of a workflow execution
--------------------------------------
 
Return the logs of a given workflow execution

Workflow Execution Id = 81::

  curl -X GET --header 'Accept: text/plain' 'http://localhost:8080/api/v1/workflow-executions/81/logs/view'
  
  
Get the list of jar files under the fire-lib directory
----------------------------------------------------------

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://localhost:8080/api/v1/lib-jars'
  
  
Delete Workflow Executions by days
----------------------------------
 
"days": "3"::

  curl -X DELETE --header 'Accept: text/plain' 'http://localhost:8080/api/v1/workflow-executions/days/3'
  
  
Get Executed Task Count
-----------------------
 
  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-executions/tasks/count'
  
Get Latest Executions
---------------------
 
  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-executions/latest'
  
Get the latest execution result of workflow
--------------------------------------------
 
"workflowId": "1",

"nodeId": "1"::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/execution-results/workflows/1/nodes/1/latest'



