More Workflows REST API
=======================

Execute Workflow Locally Synchronous
------------------------------------

* nodeId : 1
* projectId : 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d '{"name":"SQL","nodes":[],"edges":[]}' 'http://localhost:8080/api/v1/workflows/nodes/1/execute?projectId=1'


Get the updated values for a node in the workflow
----------------------------------------------------

* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 1' -d '{"name":"string","nodes":[],"edges":[]}' 'http://localhost:8080/nodeWithUpdatedValuesJSON' -b /tmp/cookies.txt


Get the list of nodes that are in an inconsistent state - mainly with regard to schema
 
* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{"name":"Elastic Search","nodes":[],"edges":[]}' 'http://localhost:8080/nodesInconsistentStateJSON' -b /tmp/cookies.txt


Get the value of a given field in a Node of a Workflow
------------------------------------------------------

* "nodeId": "2",
* "fieldName": "imageCol"

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 2' --header 'fieldName: imageCol' -d '{"name":"OCR","nodes":[],"edges":[]}' 'http://localhost:8080/getValue1d' -b /tmp/cookies.txt


Load Example Applications
-------------------------

Load Example Applications

An example request for Loading Example Applications

::

    curl -X GET --header 'Accept: text/plain' 'http://localhost:8080/api/v1/apps/example-datasets-and-workflows/load' -b /tmp/cookies.txt
    
An example response:

Since already Example application is there

::

   "Example Applications might already have been loaded"

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


