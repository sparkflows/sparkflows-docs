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

  curl -v -i -H "Accept:application/json" -H "Content-Type: application/json" -H "workflowId:1" -X POST -b /tmp/cookies.txt -d '{ "userName": "admin", "sparkConfig": "", "libJars": "" }' localhost:8080/workflowexecuterest
  
Get Analysis Flow Executions
----------------------------

Returns the list of Executions for the logged in user::

  curl -i --header "Accept:application/json" -X GET -b /tmp/cookies.txt localhost:8080/allWorkflowExecutions -b /tmp/cookies.txt

View execution result of a given execution
------------------------------------------

AnalysisFlowExecutionId = 79

Type = 2::

  curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "analysisFlowExecutionId:79" -H "type:2" -X GET -X GET -b /tmp/cookies.txt localhost:8080/viewExecutionResult
  
View executions of a Workflow
------------------------------
 
Return the list of Executions for given Analysis Flow Id.

workflowId = 81::

  curl -X GET --header 'Accept: text/html' --header 'workflowId: 81' 'http://localhost:8080/workflowExecutions' -b /tmp/cookies.txt
  
Stop Executing a Workflow
-------------------------
 
Return the list of Executions for given Analysis Flow Id.

Workflow Execution Id = 1::

  curl -X GET --header 'Accept: text/html' --header 'workflowExecutionId: 1' 'http://localhost:8080/stopWorkflowExecution' -b /tmp/cookies.txt
  
View Spark Log of a workflow execution
--------------------------------------
 
Return the logs of a given workflow execution

Workflow Execution Id = 81::

  curl -X GET --header 'Accept: text/html' --header 'workflowExecutionId: 81' 'http://localhost:8080/viewLogs' -b /tmp/cookies.txt
  
Consume the message sent from YarnRestWorkflowContext
-----------------------------------------------------
 
jobId=1

message=test::

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/plain' 'http://localhost:8080//messageFromSparkJob ?jobId=1&message=test' -b /tmp/cookies.txt
