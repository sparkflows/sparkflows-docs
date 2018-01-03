Workflows REST API
===================


Overview
--------
 
  The Workflow REST API's, allow you to interact with the Workflows.

  Below are the various Workflow API's available in Sparkflows

  They should be executed after you have logged into Sparkflows

Get List of workflows for the logged in user
--------------------------------------------

Returns the list of workflows for the logged in user.
Header: sortPara:asc/desc::

  curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "sortPara:desc" -X GET -b /tmp/cookies.txt localhost:8080/workflowsJSON

Save A Workflow
----------------

Creates a new Workflow or updates an existing one.
 
For creating new AnalysisFlow set analysisFlowId = null::

  curl -v -i -H "Accept:application/json" -H "Content-Type: application/json" -H "analysisFlowId:null" -X POST -b /tmp/cookies.txt -d '{"name": "Workflow123","uuid": "","category": null,"description": null,"nodes": [],"edges": []}' localhost:8080/saveWorkflow

Delete the workflow
-------------------

id: 1::

  curl -X GET --header 'Accept: text/html' --header 'analysisFlowId: 1' 'http://localhost:8080/deleteWorkflow' -b /tmp/cookies.txt

Execute Workflow Locally Synchronous
-------------------------------------
nodeId : 1::

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 1' -d '{"name":"SQL","nodes":[],"edges":[]}' 'http://localhost:8080/executeWorkflowLocallySynchronous' -b /tmp/cookies.txt

Get Latest WorkFlows
---------------------
 
  curl -X GET --header 'Accept: text/html' 'http://localhost:8080/getLatestWorkflows' -b /tmp/cookies.txt


Return the value of a given field in a Node of a Workflow
 
"nodeId": "2",
"fieldName": "imageCol"
​
curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 2' --header 'fieldName: imageCol' -d '{"name":"OCR","nodes":[],"edges":[]}' 'http://localhost:8080/getValue1d' -b /tmp/cookies.txt
​
​
Get Workflow Count
 
​
curl -X GET --header 'Accept: text/html' 'http://localhost:8080/getWorkflowCount' -b /tmp/cookies.txt
​
​
Is Execute Enabled in Configurations
 
​
curl -X GET --header 'Accept: text/html' 'http://localhost:8080/isExecuteEnabled' -b /tmp/cookies.txt
​
​
Load Example Dataset And Workflow
 
​
curl -X GET --header 'Accept: text/html' 'http://localhost:8080/loadExampleDatasetAndWorkflow' -b /tmp/cookies.txt
​
​
Return the updated values for a node given the workflow
 
nodeId: 1
​
curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 1' -d '{"name":"string","nodes":[],"edges":[]}' 'http://localhost:8080/nodeWithUpdatedValuesJSON' -b /tmp/cookies.txt
​
​
Return the list of nodes that are in an inconsistent state - mainly with regard to schema
 
nodeId: 1
​
curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{"name":"Elastic Search","nodes":[],"edges":[]}' 'http://localhost:8080/nodesInconsistentStateJSON' -b /tmp/cookies.txt
​
​
Retrieve the workflow versions
 
​
​
curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'analysisflowId: 1' 'http://localhost:8080/retrieveWorkflowVersions' -b /tmp/cookies.txt 
​
​
Retrieve  schema For Node
 
nodeId: 1
​
curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 1' -d '{"name":"string","nodes":[],"edges":[]}
' 'http://localhost:8080/schemaForNodeJSON' -b /tmp/cookies.txt
​
​
Retrieve  schema Output For Node
 
nodeId: 1
​
curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 1' -d '{"name":"string","nodes":[],"edges":[]}
' 'http://localhost:8080/schemaOutputForNodeJSON' -b /tmp/cookies.txt
Get workflow by Id
 
Id : 1
​
curl -X GET --header 'Accept: text/html' 'http://localhost:8080/workflowById/1' -b /tmp/cookies.txt
Get fire workflow by Id
 
Id : 1
​
curl -X GET --header 'Accept: text/html' 'http://localhost:8080/workflowFireById/1' -b /tmp/cookies.txt
Model Schema of workflow
 
​
{
"name": "string",
"category": "string",
"description": "string",
"nodes": [
{
"id": "string",
"name": "string",
"description": "string",
"nodeClass": "string",
"path": "string",
"type": "string",
"x": "string",
"y": "string"
"fields": [
{
"datatypes": [
"string"
],
"description": "string",
"display": true,
"name": "string",
"optionsArray": [
"string"
],
"optionsMap": {},
"required": true,
"title": "string",
"value": "string",
"widget": "string"
}
],
},
],
"edges": [
{
"id": 0,
"source": "string",
"target": "string"
},
]
}
