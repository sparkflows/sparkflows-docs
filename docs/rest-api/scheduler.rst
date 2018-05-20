Scheduler REST API
==================

Get list of all Workflows Scheduled
-----------------------------------

analysisflowId = 1::

  curl -X GET --header 'Accept: application/json' --header 'analysisflowId: 1'   http://localhost:8080/listWorkflowsScheduled  -b /tmp/cookies.txt


