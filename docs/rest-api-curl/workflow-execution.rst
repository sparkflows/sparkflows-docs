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
  "workflowId": 0
  }' 'http://hostname:port/api/v1/workflow/execute' -b /tmp/cookies.txt
   

An Example response:

::

    200

List all the Executions
------------------------

List all the workflow executions.

An example request for List all the executions:

::

    curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflow-executions?page=0&size=1000' -b /tmp/cookies.txt
    
An Example response:

::

    200    
    
    
  
List Executions of a Workflow
------------------------------
 
Return the list of Executions for given workflowId.

workflowId = 131::

An Example request for List executions of a Workflow::

  curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflow-executions/workflows/131' -b /tmp/cookies.txt

An Example response:

::

    200
  
Stop the Execution of workflow
--------------------------------
 
Stops the execution of workflow with specified workflowExecutionId.

Workflow Execution Id = 100::

An Example request for Stopping specified workflow:

::

  curl -X GET --header 'Accept: text/plain' 'http://hostname:port/api/v1/workflow-execution/100/stop'' -b /tmp/cookies.txt
  
An Example response:

::

    200  
  
Kill the Execution of workflow
------------------------------
 
Kill the execution of workflow with specified workflowExecutionId.

Workflow Execution Id = 100::

An example request for Killing specified workflow::

  curl -X GET --header 'Accept: text/plain' 'http://hostname:port/api/v1/workflow-execution/100/kill' -b /tmp/cookies.txt

An Example response:

::

    200
  
 
  
Delete Workflow Executions by days
----------------------------------
 
Delete Workflow Executions by days
 
"days": "7"::

An example request for deleting workflow executions by days::

  curl -X DELETE --header 'Accept: text/plain' 'http://hostname:port/api/v1/workflow-executions/days/7' -b /tmp/cookies.txt
  

An Example response:

::

    200

Get Executed Task Count
-----------------------

Get Executed Task Count:

An example request for Getting Executed Task Count::

  curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflow-executions/tasks/count' -b /tmp/cookies.txt
  

An Example response:

::

    200

Get Latest Executions
---------------------

Get Latest Executions:

An Example request for Getting Latest Executions::

  curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflow-executions/latest' -b /tmp/cookies.txt
   
An Example response:

::

    200  

