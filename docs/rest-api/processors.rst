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

  curl -i --header "Accept:application/json" -X GET -b /tmp/cookies.txt localhost:8080/nodeList
  

Get details of a given Processor 
--------------------------------
 
The below gets the details of the Processor 'ApacheLogs'::
 
 
  curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "name:ApacheLogs" -X GET -X GET -b /tmp/cookies.txt localhost:8080/getSelNode

