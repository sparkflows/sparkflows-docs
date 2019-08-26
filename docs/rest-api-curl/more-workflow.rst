More Workflows REST API
=======================

Execute Workflow Locally Synchronous
------------------------------------

* nodeId : 1
* projectId : 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d '{"name":"SQL","nodes":[],"edges":[]}' 'http://localhost:8080/api/v1/workflows/nodes/1/execute?projectId=1'


