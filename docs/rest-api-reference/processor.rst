processor
============

The Processors REST APIs, allow you to get the list of available Processors and details regarding each Processor.

Below are the various Processor APIs available in Fire Insights.They should be executed after you have logged into Fire Insights. 

Get Processors List
-------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/nodes
     - GET
     
Create a new workflow.
 
An example request for creating workflow:
 
::

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

