Scheduler REST API
==================

Get list of all Workflows Scheduled
-----------------------------------

* analysisflowId = 1

::

    curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-schedules/projects/1/workflows/1'  -b /tmp/cookies.txt
  
Schedule new Workflow
---------------------

curl::

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: */*' -d '1' 'http://localhost:8080/api/v1/workflow-schedules'
  
JSON::

    "analysisFlowId": 0,
    "cronPattern": "string",
    "dateCreated": "2019-08-06T11:77:17.221Z",
    "dateLastUpdated": "2019-08-06T11:77:17.221Z",
    "day": "string",
    "dayOfTheMonth": 0,
    "description": "string",
    "emailonFailure":"string",
    "emailonSuccess": "string"
    "endTime": "2019-08-06T11:77:17.221Z",
    "fireEvery": "string",
    "firedTime": "2019-08-06T11:77:17.221Z",
    "hour": 0,
    "id": 0,
    "Libjars": "string",
    "minute": 0,
   "name": "string",
   "sparkSubmitOptions": "string",
   "startTime": "22019-08-06T11:77:17.221Z",
   "userId": "0",
   "id": "string",
   }'    'http://137.117.83.79:8080/api/v1/workflow-schedules'  -b /tmp/cookies.txt


Delete Scheduled Workflow
-------------------------

It deletes a scheduled instance of a workflow::

    curl  -X GET    --header 'Accept: application/json'    --header 'id: 1'    'http://localhost:8080/api/v1/workflow-schedules/1' -b /tmp/cookies.txt




