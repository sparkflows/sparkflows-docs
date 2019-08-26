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


