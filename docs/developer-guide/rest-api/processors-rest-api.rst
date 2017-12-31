Processors REST API
===================

Overview
---------
 
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



Get list of Node Rules
-------------------------
 
This provides the rules associated with the nodes::
 
 
    curl -X GET --header 'Accept: application/json' -b /tmp/cookies.txt  localhost:8080/nodeRules



Get Node Count
---------------
 
The below gets the count of all Nodes::

    curl -X GET --header 'Accept: application/json'   http://localhost:8080/getNodeCount   -b /tmp/cookies.txt
  
  


