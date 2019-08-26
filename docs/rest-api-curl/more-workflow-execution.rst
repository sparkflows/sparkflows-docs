More Workflow Execution API's
=================

Consume the message sent from YarnRestWorkflowContext
-----------------------------------------------------
 
jobId=1

message=test::

  curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/plain' 'http://localhost:8080/api/v1/spark-job/messages?jobId=1&message=test'
  

Get the Spark Configuration for the username
------------------------------------------------

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/spark-configs/username/admin'

List all the workflow executions by all users
---------------------------------------------
 
  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflow-executions/users'

