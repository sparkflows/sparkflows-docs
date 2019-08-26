Workflows REST API
==================

The Workflow REST API's, allow you to interact with the Workflows.

Below are the various Workflow API's available in Fire Insights. They should be executed after you have logged into Fire Insights.


Create Workflow
---------------

Creates a new Workflow.
 
For creating a new Workflow set analysisFlowId = 0 & projectId = 33:

An example request for Creating workflow:

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/plain' -d '{
  "analysisflowId": 0,
  "comment": "string",
  "projectId": 33,
  "workflow": {
    "category": "string",
    "dataSetDetails": [
      {
        "datasetSchema": "string",
        "datasetType": "CSV",
        "delimiter": "string",
        "description": "string",
        "filterLinesContaining": "string",
        "header": true,
        "id": 0,
        "name": "string",
        "path": "string",
        "readOptions": "string",
        "uuid": "string",
        "version": 0
      }
    ],
    "description": "string",
    "edges": [
      {
        "id": 0,
        "source": "string",
        "target": "string"
      }
    ],
    "engine": "string",
    "h2OWorkflow": true,
    "name": "string",
    "nodes": [
      {
        "description": "string",
        "details": "string",
        "engine": "string",
        "examples": "string",
        "fields": [
          {
            "datatypes": [
              "string"
            ],
            "description": "string",
            "disableRefresh": true,
            "display": true,
            "editable": true,
            "name": "string",
            "optionsArray": [
              "string"
            ],
            "optionsMap": {},
            "required": true,
            "title": "string",
            "value": "string",
            "widget": "string"
          }
        ],
        "iconImage": "string",
        "id": "string",
        "name": "string",
        "nodeClass": "string",
        "path": "string",
        "type": "string",
        "x": "string",
        "y": "string"
      }
    ],
    "parameters": "string",
    "uuid": "string"
  }
}' 'http://localhost:8080/api/v1/workflows' -b /tmp/cookies.txt

An example response:

::

    200

Get workflow by Id
------------------

* Id : 1

::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/id/1'



Delete the workflow
-------------------

Deletes a workflow with the given workflowId.

* workflowId: 1955

An example request for deleting workflow::


    curl -X DELETE --header 'Accept: text/plain' 'http://localhost:8080/api/v1/workflows/id/1955' -b /tmp/cookies.txt
    
An example response:

::

    Workflow deleted successfully.



Get Latest WorkFlows
-------------------- 

Get Latest WorkFlows availble in application:

An example request for getting Latest WorkFlows availble in application::



    curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflows/latest' -b /tmp/cookies.txt
    
An example response:

::

    {
    "id": 1954,
    "userId": 3,
    "uuid": "0e119cf1-2833-4c62-8466-21853fc1fb21",
    "name": "aaaaawqw",
    "category": "-",
    "content": "{\"name\":\"aaaaawqw\",\"uuid\":\"0e119cf1-2833-4c62-8466-21853fc1fb21\",\"category\":\"-\",\"description\":\"1111\",\"parameters\":\"2222@1111\",\"nodes\":[{\"id\":\"1\",\"name\":\"ReadCSV\",\"description\":\"It reads in CSV files and creates a DataFrame from it\",\"details\":\"\",\"examples\":\"\",\"type\":\"dataset\",\"nodeClass\":\"fire.nodes.dataset.NodeDatasetCSV\",\"x\":\"243.5px\",\"y\":\"206px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"path\",\"value\":\"/user/sparkflows/Clickthru.csv\",\"widget\":\"textfield\",\"title\":\"Path\",\"description\":\"Path of the Text file/directory\",\"required\":true,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"separator\",\"value\":\",\",\"widget\":\"textfield\",\"title\":\"Separator\",\"description\":\"CSV Separator\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"header\",\"value\":\"true\",\"widget\":\"array\",\"title\":\"Header\",\"description\":\"Does the file have a header row\",\"optionsArray\":[\"true\",\"false\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"dropMalformed\",\"value\":\"false\",\"widget\":\"array\",\"title\":\"Drop Malformed\",\"description\":\"Whether to drop Malformed records or error\",\"optionsArray\":[\"true\",\"false\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColNames\",\"value\":\"[\\\"Timestamp\\\",\\\"UserId\\\",\\\"IP Address\\\",\\\" Product Id\\\"]\",\"widget\":\"schema_col_names\",\"title\":\"Column Names for the CSV\",\"description\":\"New Output Columns of the SQL\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColTypes\",\"value\":\"[\\\"STRING\\\",\\\"INTEGER\\\",\\\"STRING\\\",\\\"INTEGER\\\"]\",\"widget\":\"schema_col_types\",\"title\":\"Column Types for the CSV\",\"description\":\"Data Type of the Output Columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColFormats\",\"value\":\"[\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\"]\",\"widget\":\"schema_col_formats\",\"title\":\"Column Formats for the CSV\",\"description\":\"Format of the Output Columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"all\"},{\"id\":\"2\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"424.83px\",\"y\":\"191.323px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"title\",\"value\":\"Row Values\",\"widget\":\"textfield\",\"title\":\"Title\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"all\"}],\"edges\":[{\"source\":\"1\",\"target\":\"2\",\"id\":1}],\"dataSetDetails\":[],\"engine\":\"scala\"}",
    "description": "1111",
    "version": 4,
    "dateCreated": 1566395460079,
    "dateLastUpdated": 1566395644690,
    "lockedByUserId": null,
    "permission": null,
    "workflow": {
      "name": "aaaaawqw",
      "uuid": "0e119cf1-2833-4c62-8466-21853fc1fb21",
      "category": "-",
      "description": "1111",
      "parameters": "2222@1111",
      "nodes": [
        {
          "id": "1",
          "path": null,
          "name": "ReadCSV",
          "iconImage": null,
          "description": "It reads in CSV files and creates a DataFrame from it",
          "details": "",
          "examples": "",
          "type": "dataset",
          "nodeClass": "fire.nodes.dataset.NodeDatasetCSV",
          "x": "243.5px",
          "y": "206px",
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
              "value": "/user/sparkflows/Clickthru.csv",
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
              "value": "true",
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
              "value": "[\"Timestamp\",\"UserId\",\"IP Address\",\" Product Id\"]",
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
              "value": "[\"STRING\",\"INTEGER\",\"STRING\",\"INTEGER\"]",
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
              "value": "[\"\",\"\",\"\",\"\"]",
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



Get Workflow Count
------------------
Gets the count of the Workflow in application.

An example request for getting count of the Workflow::


   curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflows/count' -b /tmp/cookies.txt
   
An example response:

::

   246




Get the workflow versions
------------------------------ 

::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/versions?workflowId=1'




