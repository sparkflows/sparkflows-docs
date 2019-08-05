Workflow Execution REST API
============================

Overview
--------
 
The Workflow Execution REST API's, allow you to execute Workflows, get results etc.

Below are the various Workflow Execution API's available in Sparkflows

They should be executed after you have logged into Sparkflows

Execute a Workflow
------------------

It executes a given Workflow.

It returns the workflow execution id::

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'workflowId: 1' --header 'api_key: cookies' -d '{ "userName": "admin", "userId": 1, "sparkConfig": "", "libJarsList": [], "emailOnFailure": "", "emailOnSuccess": "" }' 'http://localhost:8080/api/v1/workflow/execute'


Get Analysis Flow Executions
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
  
Consume the message sent from YarnRestWorkflowContext
-----------------------------------------------------
 
jobId=1

message=test::

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/plain' 'http://localhost:8080/api/v1/spark-job/messages?jobId=1&message=test'
  
Returns the list of jar files under the fire-lib directory
----------------------------------------------------------

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' 'http://localhost:8080/api/v1/lib-jars'
  
Returns the Spark Configuration for the username
------------------------------------------------

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/spark-configs/username/admin'
  
Delete Workflow Executions by days
----------------------------------
 
"days": "3"::

  curl -X DELETE --header 'Accept: text/plain' 'http://localhost:8080/api/v1/workflow-executions/days/3'
  
List all the workflow executions by all users
---------------------------------------------
 
  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-executions/users'
  
Get Executed Task Count
-----------------------
 
  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-executions/tasks/count'
  
Get Latest Executions
---------------------
 
  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-executions/latest'
  
View the latest execution result of workflow
--------------------------------------------
 
"workflowId": "1",

"nodeId": "1"::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/execution-results/workflows/1/nodes/1/latest'



