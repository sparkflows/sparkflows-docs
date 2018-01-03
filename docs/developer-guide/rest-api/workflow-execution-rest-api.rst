Workflow Execution REST API
===========================

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
-------------------------------------------
AnalysisFlowExecutionId = 79
Type = 2::
 
  curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "analysisFlowExecutionId:79" -H "type:2" -X GET -X GET -b /tmp/cookies.txt localhost:8080/viewExecutionResult
