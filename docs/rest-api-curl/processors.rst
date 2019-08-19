Processors REST API's
=====================

Overview
--------

The Processors REST API's, allow you to get the list of available Processors and details regarding each Processor

Below are the various Processor API's available in Sparkflows

They should be executed after you have logged into Sparkflows


Get List of available Processors
--------------------------------

It gets the list of available Processors::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/nodes' -b /tmp/cookies.txt
  

Get details of a given Processor 
--------------------------------
 
The below gets the details of the Processor 'ApacheLogs'::
 
  curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/nodes/names/{name}' -b /tmp/cookies.txt

Get list of Node Rules
----------------------
 
This provides the rules associated with the nodes::
 
 
  curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/node-rules' -b /tmp/cookies.txt

Get Node Count
--------------

This gets the count of the Processors::
 
   curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/nodes/count' -b /tmp/cookies.txt
