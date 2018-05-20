Workflows REST API
==================

The Workflow REST API's, allow you to interact with the Workflows.

Below are the various Workflow API's available in Sparkflows

They should be executed after you have logged into Sparkflows

Get List of workflows
---------------------

Returns the list of workflows for the logged in user.

* Header: sortPara:asc/desc.

::

    curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "sortPara:desc" -X GET -b /tmp/cookies.txt localhost:8080/workflowsJSON

Create / Save A Workflow
------------------------

Creates a new Workflow or updates an existing one.
 
For creating new Workflow set analysisFlowId = null

::

    curl -v -i -H "Accept:application/json" -H "Content-Type: application/json" -H "analysisFlowId:null" -X POST -b /tmp/cookies.txt -d '{"name": "Workflow123","uuid": "","category": null,"description": null,"nodes": [],"edges": []}' localhost:8080/saveWorkflow
    
    
Delete the workflow
-------------------

Deletes a workflow with the given id.

* id: 1

::

    curl -X GET --header 'Accept: text/html' --header 'analysisFlowId: 1' 'http://localhost:8080/deleteWorkflow' -b /tmp/cookies.txt

Execute Workflow Locally Synchronous
------------------------------------

* nodeId : 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 1' -d '{"name":"SQL","nodes":[],"edges":[]}' 'http://localhost:8080/executeWorkflowLocallySynchronous' -b /tmp/cookies.txt


Get Latest WorkFlows
-------------------- 

::

    curl -X GET --header 'Accept: text/html' 'http://localhost:8080/getLatestWorkflows' -b /tmp/cookies.txt


Get the value of a given field in a Node of a Workflow
------------------------------------------------------

* "nodeId": "2",
* "fieldName": "imageCol"

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 2' --header 'fieldName: imageCol' -d '{"name":"OCR","nodes":[],"edges":[]}' 'http://localhost:8080/getValue1d' -b /tmp/cookies.txt

Get Workflow Count
------------------

::

    curl -X GET --header 'Accept: text/html' 'http://localhost:8080/getWorkflowCount' -b /tmp/cookies.txt


Load Example Datasets And Workflows
---------------------------------

::

    curl -X GET --header 'Accept: text/html' 'http://localhost:8080/loadExampleDatasetAndWorkflow' -b /tmp/cookies.txt


Get the updated values for a node in the workflow
----------------------------------------------------

* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 1' -d '{"name":"string","nodes":[],"edges":[]}' 'http://localhost:8080/nodeWithUpdatedValuesJSON' -b /tmp/cookies.txt


Get the list of nodes that are in an inconsistent state - mainly with regard to schema
 
* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{"name":"Elastic Search","nodes":[],"edges":[]}' 'http://localhost:8080/nodesInconsistentStateJSON' -b /tmp/cookies.txt



Get the workflow versions
------------------------------ 

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'analysisflowId: 1' 'http://localhost:8080/retrieveWorkflowVersions' -b /tmp/cookies.txt 

