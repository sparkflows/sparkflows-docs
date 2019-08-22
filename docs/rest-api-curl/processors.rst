Processors REST API's
=====================

Overview
--------

The Processors REST API's, allow you to get the list of available Processors and details regarding each Processor.

Below are the various Processor API's available in Sparkflows.

They should be executed after you have logged into Sparkflows. Use the -b option to use the cookies previously saved.

Node Rules
----------

Gets the node rules used in the workflow editor.

An example request for getting the node rules::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/node-rules' -b /tmp/cookies.txt



Get List of available Processors
--------------------------------

Gets the list of available Processors::

An example request::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/nodes' -b /tmp/cookies.txt
  
An example response::

.. code-block:: Result
   :linenos:

   [
   {
    "id": "3",
    "path": "/01-Connectors/",
    "name": "ReadCassandra",
    "iconImage": null,
    "description": "This node reads data from Apache Cassandra",
    "details": "",
    "examples": "",
    "type": "dataset",
    "nodeClass": "fire.nodes.cassandra.NodeReadCassandra",
    "x": null,
    "y": null,
     "fields": [
   {
        "name": "storageLevel",
        "value": "DEFAULT",
        "widget": "array",
        "title": "Output Storage Level",
        "description": "Storage Level of the Output Datasets of this Node",
        "optionsMap": null,
        "datatypes": null,
        "optionsArray": [
          "DEFAULT",
          "NONE",
          "DISK_ONLY",
          "DISK_ONLY_2",
          "MEMORY_ONLY",
          "MEMORY_ONLY_2",
          "MEMORY_ONLY_SER",
          "MEMORY_ONLY_SER_2",
          "MEMORY_AND_DISK",
          "MEMORY_AND_DISK_2",
          "MEMORY_AND_DISK_SER",
          "MEMORY_AND_DISK_SER_2",
          "OFF_HEAP"
   ],
        "required": false,
        "display": true,
        "editable": true,
        "disableRefresh": false
   },
   {
        "name": "table",
        "value": "",
        "widget": "textfield",
        "title": "Cassandra Table",
        "description": "Cassandra Table from which to read the data",
        "optionsMap": null,
        "datatypes": null,
        "optionsArray": null,
        "required": true,
        "display": true,
        "editable": true,
        "disableRefresh": false
   },
   {
        "name": "keyspace",
        "value": "",
        "widget": "textfield",
        "title": "Cassandra Keyspace",
        "description": "Cassandra Keyspace",
        "optionsMap": null,
        "datatypes": null,
        "optionsArray": null,
        "required": true,
        "display": true,
        "editable": true,
        "disableRefresh": false
   },
   {
        "name": "cluster",
        "value": "",
        "widget": "textfield",
        "title": "Cassandra Cluster",
        "description": "The group of the Cluster Level ",
        "optionsMap": null,
        "datatypes": null,
        "optionsArray": null,
        "required": false,
        "display": true,
        "editable": true,
        "disableRefresh": false
   }
   ],
    "engine": "scala"
   },
  

Get Node Count
--------------

This will get the count of the Processors::

An example request:
 
   curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/nodes/count' -b /tmp/cookies.txt
   
An example response::

.. code-block:: Result
   :linenos:
   
   266
   
Get Processors list for Engine
------------------------------

Gets the list of processors for the specified engine::

An example request::

   curl -X GET --header 'Accept: application/json' 'http://localhost:8080//api/v1/nodes/scala' -b /tmp/cookies.txt

An example response:

.. code-block:: Result
   :linenos:
   
   [
   {
    "id": "3",
    "path": "/01-Connectors/",
    "name": "ReadCassandra",
    "iconImage": null,
    "description": "This node reads data from Apache Cassandra",
    "details": "",
    "examples": "",
    "type": "dataset",
    "nodeClass": "fire.nodes.cassandra.NodeReadCassandra",
    "x": null,
    "y": null,
    "fields": [
   {
        "name": "storageLevel",
        "value": "DEFAULT",
        "widget": "array",
        "title": "Output Storage Level",
        "description": "Storage Level of the Output Datasets of this Node",
        "optionsMap": null,
        "datatypes": null,
        "optionsArray": [
          "DEFAULT",
          "NONE",
          "DISK_ONLY",
          "DISK_ONLY_2",
          "MEMORY_ONLY",
          "MEMORY_ONLY_2",
          "MEMORY_ONLY_SER",
          "MEMORY_ONLY_SER_2",
          "MEMORY_AND_DISK",
          "MEMORY_AND_DISK_2",
          "MEMORY_AND_DISK_SER",
          "MEMORY_AND_DISK_SER_2",
          "OFF_HEAP"
   ],
        "required": false,
        "display": true,
        "editable": true,
        "disableRefresh": false
   },
   {
        "name": "table",
        "value": "",
        "widget": "textfield",
        "title": "Cassandra Table",
        "description": "Cassandra Table from which to read the data",
        "optionsMap": null,
        "datatypes": null,
        "optionsArray": null,
        "required": true,
        "display": true,
        "editable": true,
        "disableRefresh": false
   },
   {
        "name": "keyspace",
        "value": "",
        "widget": "textfield",
        "title": "Cassandra Keyspace",
        "description": "Cassandra Keyspace",
        "optionsMap": null,
        "datatypes": null,
        "optionsArray": null,
        "required": true,
        "display": true,
        "editable": true,
        "disableRefresh": false
   },
   {
        "name": "cluster",
        "value": "",
        "widget": "textfield",
        "title": "Cassandra Cluster",
        "description": "The group of the Cluster Level ",
        "optionsMap": null,
        "datatypes": null,
        "optionsArray": null,
        "required": false,
        "display": true,
        "editable": true,
        "disableRefresh": false
   }
   ],
    "engine": "scala"
   },
  
