Processors REST APIs
=====================

Overview
--------

The Processors REST APIs, allow you to get the list of available Processors and details regarding each Processor.

Below are the various Processor APIs available in Fire Insights.

They should be executed after you have logged into Fire Insights. Use the -b option to use the cookies previously saved.


GET Processors List
-------------------

Gets the list of processors available.

An example request for getting list of processors::

   curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/nodes' -b /tmp/cookies.txt 

An example response:

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
   

GET Node Count
--------------

Gets the count of the processors.

An example request for getting count of the processors::

   curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/nodes/count' -b /tmp/cookies.txt   

An example response:

::
   
    266
   
   
GET Processors list for Engine
------------------------------

Gets the list of processors for the specified engine(scala or pyspark or empty-field for all).

An example request for getting list of processors for scala ::

   curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/nodes?engine=scala' -b /tmp/cookies.txt

An example response:

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

GET Processor Details by Name
-----------------------------

Gets Processor Details by Name

An example request for getting Processor Details by Name::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/nodes/names/ReadCSV' -b /tmp/cookies.txt

An example response:

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
 }

Node Rules
----------

Gets the node rules used in the workflow editor.

An example request for getting the node rules::

   curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/node-rules' -b /tmp/cookies.txt
   
An example response:

::
   
    [
  {
    "nodeType": "dataset",
    "possibleSources": [
      "shellcommand"
    ],
    "minNumOfInputs": 0,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#F0F1F9",
    "nodeIcon": "fa-th-list",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "shellcommand",
    "possibleSources": [
      "dataset",
      "scala",
      "pyspark",
      "transform",
      "join",
      "ml-transformer",
      "ml-predict",
      "sparkstreaming"
    ],
    "minNumOfInputs": 0,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#F0F1F9",
    "nodeIcon": "fa-th-list",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "sparkstreaming",
    "possibleSources": [],
    "minNumOfInputs": 0,
    "maxNumOfInputs": 0,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#FFEB94",
    "nodeIcon": "fa-external-link",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "transform",
    "possibleSources": [
      "dataset",
      "scala",
      "pyspark",
      "transform",
      "join",
      "ml-transformer",
      "ml-predict",
      "sparkstreaming",
      "shellcommand"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#AFD4F0",
    "nodeIcon": "fa-tumblr-square",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "scala",
    "possibleSources": [
      "dataset",
      "transform",
      "join",
      "ml-transformer",
      "ml-predict",
      "sparkstreaming",
      "shellcommand"
    ],
    "minNumOfInputs": 0,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#AFD4F0",
    "nodeIcon": "fa-tumblr-square",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "pyspark",
    "possibleSources": [
      "dataset",
      "transform",
      "join",
      "ml-transformer",
      "ml-predict",
      "sparkstreaming",
      "shellcommand"
    ],
    "minNumOfInputs": 0,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#AFD4F0",
    "nodeIcon": "fa-tumblr-square",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "join",
    "possibleSources": [
      "dataset",
      "transform",
      "join",
      "shellcommand",
      "sparkstreaming"
    ],
    "minNumOfInputs": 2,
    "maxNumOfInputs": 8,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#D4A190",
    "nodeIcon": "fa-stumbleupon",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-transformer",
    "possibleSources": [
      "dataset",
      "transform",
      "ml-transformer",
      "join",
      "shellcommand"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": "2",
    "sourceRestrictions": [],
    "backgroundColor": "#dfe166",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-estimator",
    "possibleSources": [
      "dataset",
      "transform",
      "ml-transformer",
      "join",
      "shellcommand"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": "2",
    "sourceRestrictions": [],
    "backgroundColor": "#F7EFE2",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-predict",
    "possibleSources": [
      "dataset",
      "transform",
      "join",
      "ml-estimator",
      "ml-transformer",
      "ml-pipeline",
      "ml-crossvalidator",
      "ml-modelload"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 2,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#D7CFC2",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-evaluator",
    "possibleSources": [
      "ml-predict",
      "ml-estimator",
      "ml-pipeline"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": "1",
    "sourceRestrictions": [],
    "backgroundColor": "#ff9900",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-pipeline",
    "possibleSources": [
      "ml-estimator",
      "ml-transformer"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": "1",
    "sourceRestrictions": [],
    "backgroundColor": "#1FFF62",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-crossvalidator",
    "possibleSources": [
      "ml-evaluator"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#F9FC81",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-trainvalidationsplit",
    "possibleSources": [
      "ml-evaluator"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#B681FC",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-modelsave",
    "possibleSources": [
      "ml-estimator",
      "ml-pipeline",
      "ml-crossvalidator",
      "ml-trainvalidationsplit"
    ],
    "minNumOfInputs": 1,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": "1",
    "sourceRestrictions": [],
    "backgroundColor": "#FCB881",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "ml-modelload",
    "possibleSources": [
      "dataset",
      "transform",
      "join",
      "ml-estimator",
      "ml-transformer",
      "ml-pipeline",
      "ml-crossvalidator",
      "ml-modelsave"
    ],
    "minNumOfInputs": 0,
    "maxNumOfInputs": 1,
    "maxNumOfOutputs": "1",
    "sourceRestrictions": [],
    "backgroundColor": "#FCB881",
    "nodeIcon": "fa-qrcode",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "doc",
    "possibleSources": [
      "doc"
    ],
    "minNumOfInputs": 0,
    "maxNumOfInputs": 0,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#FFFF88",
    "nodeIcon": "fa-file-text",
    "nodeShape": "rectangle"
  },
  {
    "nodeType": "sticky",
    "possibleSources": [],
    "minNumOfInputs": 0,
    "maxNumOfInputs": 0,
    "maxNumOfOutputs": null,
    "sourceRestrictions": [],
    "backgroundColor": "#FFFF88",
    "nodeIcon": "fa-file-text",
    "nodeShape": "rectangle"
  },
