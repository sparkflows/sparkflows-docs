processor API
===============

The Processors REST APIs, allow you to get the list of available Processors and details regarding each Processor.

Below are the various Processor APIs available in Fire Insights.They should be executed after you have logged into Fire Insights. 

Get Processors List by Engine
-----------------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/nodes?engine=?
     - GET
   
Request Structure

For Getting Processors List by engine, we need to add below parameters

.. list-table:: 
   :widths: 10 40 40
   :header-rows: 1

   * - Parameter
     - Description
     - Value
   
   * - engine
     - The canonical identifier for Getting Processors List by engine. This field is required
     - scala, pyspark or empty-field

An example response for Getting Processors List by Engine for "scala":
 
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

Get Node Count
--------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/nodes/count
     - GET
   

An example response for Getting Node Count:
 
::

    266
    

GET Processor details by Name
-----------------------------
   
.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/nodes/names/{name}
     - GET

Request Structure

For Getting Processor details by Name, we need to add below parameters

.. list-table:: 
   :widths: 10 40 40
   :header-rows: 1

   * - Parameter
     - Description
     - Value
   
   * - Name
     - The canonical identifier for Getting Processor details by Name. This field is required
     - Node Name for which details are required

An example response for Getting Processor details by Name for "Readcsv Node":
 
::

   {
    "id": "17",
    "path": "/02-ReadStructured/",
    "name": "ReadCSV",
    "iconImage": null,
    "description": "It reads in CSV files and creates a DataFrame from it",
    "details": "",
    "examples": "",
    "type": "dataset",
    "nodeClass": "fire.nodes.dataset.NodeDatasetCSV",
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
      "name": "path",
      "value": "",
      "widget": "textfield",
      "title": "Path",
      "description": "Path of the Text file/directory",
      "optionsMap": null,
      "datatypes": null,
      "optionsArray": null,
      "required": true,
      "display": true,
      "editable": true,
      "disableRefresh": false
   },
   {
      "name": "separator",
      "value": ",",
      "widget": "textfield",
      "title": "Separator",
      "description": "CSV Separator",
      "optionsMap": null,
      "datatypes": null,
      "optionsArray": null,
      "required": false,
      "display": true,
      "editable": true,
      "disableRefresh": false
   },
   {
      "name": "header",
      "value": "false",
      "widget": "array",
      "title": "Header",
      "description": "Does the file have a header row",
      "optionsMap": null,
      "datatypes": null,
      "optionsArray": [
        "true",
        "false"
   ],
      "required": false,
      "display": true,
      "editable": true,
      "disableRefresh": false
   },
   {
      "name": "dropMalformed",
      "value": "false",
      "widget": "array",
      "title": "Drop Malformed",
      "description": "Whether to drop Malformed records or error",
      "optionsMap": null,
      "datatypes": null,
      "optionsArray": [
        "true",
        "false"
   ],
      "required": false,
      "display": true,
      "editable": true,
      "disableRefresh": false
   },
   {
      "name": "outputColNames",
      "value": "[]",
      "widget": "schema_col_names",
      "title": "Column Names for the CSV",
      "description": "New Output Columns of the SQL",
      "optionsMap": null,
      "datatypes": null,
      "optionsArray": null,
      "required": false,
      "display": true,
      "editable": true,
      "disableRefresh": false
   },
   {
      "name": "outputColTypes",
      "value": "[]",
      "widget": "schema_col_types",
      "title": "Column Types for the CSV",
      "description": "Data Type of the Output Columns",
      "optionsMap": null,
      "datatypes": null,
      "optionsArray": null,
      "required": false,
      "display": true,
      "editable": true,
      "disableRefresh": false
   },
   {
      "name": "outputColFormats",
      "value": "[]",
      "widget": "schema_col_formats",
      "title": "Column Formats for the CSV",
      "description": "Format of the Output Columns",
      "optionsMap": null,
      "datatypes": null,
      "optionsArray": null,
      "required": false,
      "display": true,
      "editable": true,
      "disableRefresh": false
   }
   ],
     "engine": "all"
   },
