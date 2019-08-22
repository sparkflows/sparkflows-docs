Workflows REST API
==================

The Workflow REST API's, allow you to interact with the Workflows.

Below are the various Workflow API's available in Sparkflows. They should be executed after you have logged into Sparkflows.

Get List of workflows
---------------------

Returns the list of workflows for the given application.

* Header: sortPara:asc/desc.

::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows?projectId=1&sortPara=asc'

Create / Save A Workflow
------------------------

Creates a new Workflow or updates an existing one.
 
For creating new Workflow set analysisFlowId = null

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d '{"name": "Workflow123","uuid": "","category": null,"description": null,"nodes": [],"edges": []}' 'http://localhost:8080/api/v1/workflows'
    
    
Delete the workflow
-------------------

Deletes a workflow with the given id.

* id: 1

::

    curl -X DELETE --header 'Accept: text/plain' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/id/1'

Execute Workflow Locally Synchronous
------------------------------------

* nodeId : 1
* projectId : 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d '{"name":"SQL","nodes":[],"edges":[]}' 'http://localhost:8080/api/v1/workflows/nodes/1/execute?projectId=1'


Get Latest WorkFlows
-------------------- 

::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/latest'


Get the value of a given field in a Node of a Workflow
------------------------------------------------------

* "nodeId": "2",
* "fieldName": "imageCol"

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 2' --header 'fieldName: imageCol' -d '{"name":"OCR","nodes":[],"edges":[]}' 'http://localhost:8080/getValue1d' -b /tmp/cookies.txt

Get Workflow Count
------------------

::

   curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/count'


Load Example Datasets And Workflows
---------------------------------

::

    curl -X GET --header 'Accept: text/plain' --header 'api_key: cookies' 'http://localhost:8080/api/v1/apps/example-datasets-and-workflows/load'


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

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/versions?workflowId=1'



Get input schema For a Node
------------------
 
* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d  '{"name":"string","nodes":[],"edges":[]}
' 'http://localhost:8080/api/v1/nodes/2/schema/input?projectId=1'


Get output schema of a Node
---------------------------

* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d '{"name":"string","nodes":[],"edges":[]}
' 'http://localhost:8080/api/v1/nodes/2/schema/output?projectId=3'

Get workflow by Id
------------------

* Id : 1

::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/id/1'

