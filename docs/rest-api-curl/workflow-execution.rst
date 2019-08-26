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

List all the executions
------------------------

List all the workflow  executions.

An example request for List all the executions:

::

    curl -X GET --header 'Accept: text/html' 'http://hostname:port/api/v1/workflow-executions?page=0&size=1000' -b /tmp/cookies.txt
    
An example response:

::

    200    
    
    
  
List executions of a Workflow
------------------------------
 
Return the list of Executions for given workflowId.

workflowId = 81::

An example request for List executions of a Workflow::

  curl -X GET --header 'Accept: text/html' 'http://hostname:port/api/v1/workflow-executions/workflows/131' -b /tmp/cookies.txt

An example response:

::

    200
  
Stops the execution of workflow
--------------------------------
 
Stops the execution of workflow with specified workflowExecutionId.

Workflow Execution Id = 100::

An example request for Stopping specified workflow:

::

  curl -X GET --header 'Accept: text/plain' 'http://hostname:port/api/v1/workflow-execution/100/stop'' -b /tmp/cookies.txt
  
An example response:

::

    200  
  
Kill the execution of workflow
------------------------------
 
Kill the execution of workflow with specified workflowExecutionId.

Workflow Execution Id = 100::

An example request for Killing specified workflow::

  curl -X GET --header 'Accept: text/plain' 'http://hostname:port/api/v1/workflow-execution/100/kill' -b /tmp/cookies.txt

An example response:

::

    200
  
  
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



