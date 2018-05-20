Scheduler REST API
==================

Get list of all Workflows Scheduled
-----------------------------------

analysisflowId = 1::

  curl -X GET --header 'Accept: application/json' --header 'analysisflowId: 1'   http://localhost:8080/listWorkflowsScheduled  -b /tmp/cookies.txt
  
Schedule new Workflow
---------------------

::

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: /' --header 'id: 1' -d '{


