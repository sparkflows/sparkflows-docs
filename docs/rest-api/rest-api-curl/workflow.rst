Workflow REST API
==================

The Workflow REST API's allow you to interact with the Workflows.

Below are the various Workflow API's available in Fire Insights. They should be executed after you have logged into Fire Insights.


Create Workflow
---------------

Create a new Workflow.
 

An example request for creating workflow:

::

    curl -X POST --header 'token: eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcwMzM3NTQyODY2MSwiaWF0IjoxNzAxNjY4NTc2fQ.YSoEU5w5r4BO2yVVmSRU9NHvk_NwctR43GLG_P52pdG4OTLzlQIhkUL0Y1yBHBny6YZTf9ztVlwY7Bjkyhqjjj' --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{
  "analysisflowId": 1,
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
  }' 'http://hostname:port/api/v1/workflows' -b /tmp/cookies.txt

An example response:

::

    193

Execute Workflow
---------------

Execute specified Workflow.

An example request for Executing specified workflow:

::
   
   curl -X POST --header 'token: eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcwMzM3NTQyODY2MSwiaWF0IjoxNzAxNjY4NTc2fQ.YSoEU5w5r4BO2yVVmSRU9NHvk_NwctR43GLG_P52pdG4OTLzlQIhkUL0Y1yBHBny6YZTf9ztVlwY7Bjkyhqjjj' --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{
  "emailOnFailure": "string",
  "emailOnSuccess": "string",
  "libJars": "string",
  "programParameters": "string",
  "sparkConfig": "string",
  "workflowId": 1
  }' 'http://hostname:port/api/v1/workflow/execute' -b /tmp/cookies.txt
   

An example response:

::

    162

Update Workflow
----------------

Update specified Workflow.

An example request for updating workflow:

::
 
   curl -X PUT --header 'token: eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcwMzM3NTQyODY2MSwiaWF0IjoxNzAxNjY4NTc2fQ.YSoEU5w5r4BO2yVVmSRU9NHvk_NwctR43GLG_P52pdG4OTLzlQIhkUL0Y1yBHBny6YZTf9ztVlwY7Bjkyhqjjj' --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{
  "analysisflowId": 1,
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
  }' 'http://hostname:port/api/v1/workflows' -b /tmp/cookies.txt

An example response:

::

    131

Get workflow by Id
------------------

Gets the workflow with the specified id.

* id: 1

An example request for getting workflow by id:


::

    curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflows/id/1' -b /tmp/cookies.txt

An example response:

::

    {
  "id": 1,
  "userId": 1,
  "uuid": "3a3dfa34-bbd7-4c05-8745-55628d90cbf6",
  "name": "Analyze Flights Delay",
  "category": "Analytics",
  "content": "{\"name\":\"Analyze Flights Delay\",\"uuid\":\"3a3dfa34-bbd7-4c05-8745-55628d90cbf6\",\"category\":\"Analytics\",\"description\":\"Find Flights which are delayed by more than 40 minutes.\",\"nodes\":[{\"id\":\"1\",\"name\":\"DatasetStructured\",\"description\":\"This Node creates a DataFrame by reading data from HDFS, HIVE etc. The dataset has been defined earlier in Fire by using the Dataset Feature. As a user, you just have to select the Dataset of your interest.\",\"details\":\"This Node creates a DataFrame by reading data from HDFS, HIVE etc.\\u003cbr\\u003e\\n\\u003cbr\\u003e\\nThe data has been defined earlier in Fire by using the Dataset Feature. As a user, you just have to select the Dataset of your interest.\\u003cbr\\u003e\",\"examples\":\"\",\"type\":\"dataset\",\"nodeClass\":\"fire.nodes.dataset.NodeDatasetStructured\",\"x\":\"38.9492px\",\"y\":\"275.613px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"dataset\",\"value\":\"2ff32692-9b3c-49de-91a7-401daf2590c1\",\"widget\":\"dataset\",\"title\":\"Dataset\",\"description\":\"Selected Dataset\",\"required\":true,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"2\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"38.4336px\",\"y\":\"59.1094px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"title\",\"value\":\"Row Values\",\"widget\":\"textfield\",\"title\":\"Title\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"3\",\"name\":\"CastColumnType\",\"description\":\"This node creates a new DataFrame by casting input columns with a new data type\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeCastColumnType\",\"x\":\"313.223px\",\"y\":\"61.8633px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"inputCols\",\"value\":\"[\\\"CRS_DEP_TIME\\\",\\\"CRS_ARR_TIME\\\",\\\"CRS_ELAPSED_TIME\\\"]\",\"widget\":\"variables\",\"title\":\"Columns\",\"description\":\"Columns to be cast to new data type\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColType\",\"value\":\"DOUBLE\",\"widget\":\"array\",\"title\":\"New Data Type\",\"description\":\"New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)\",\"optionsArray\":[\"BOOLEAN\",\"BYTE\",\"DATE\",\"DECIMAL\",\"DOUBLE\",\"FLOAT\",\"INTEGER\",\"LONG\",\"SHORT\",\"STRING\",\"TIMESTAMP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"replaceExistingCols\",\"value\":\"true\",\"widget\":\"array\",\"title\":\"Replace Existing Cols\",\"description\":\"Whether to replace existing columns or create new ones\",\"optionsArray\":[\"true\",\"false\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"4\",\"name\":\"CastColumnType\",\"description\":\"This node creates a new DataFrame by casting input columns with a new data type\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeCastColumnType\",\"x\":\"322.949px\",\"y\":\"275.633px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"inputCols\",\"value\":\"[\\\"DAY_OF_MONTH\\\",\\\"DAY_OF_WEEK\\\"]\",\"widget\":\"variables\",\"title\":\"Columns\",\"description\":\"Columns to be cast to new data type\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColType\",\"value\":\"STRING\",\"widget\":\"array\",\"title\":\"New Data Type\",\"description\":\"New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)\",\"optionsArray\":[\"BOOLEAN\",\"BYTE\",\"DATE\",\"DECIMAL\",\"DOUBLE\",\"FLOAT\",\"INTEGER\",\"LONG\",\"SHORT\",\"STRING\",\"TIMESTAMP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"replaceExistingCols\",\"value\":\"true\",\"widget\":\"array\",\"title\":\"Replace Existing Cols\",\"description\":\"Whether to replace existing columns or create new ones\",\"optionsArray\":[\"true\",\"false\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"5\",\"name\":\"StringIndexer\",\"description\":\"StringIndexer encodes a string column of labels to a column of label indices\",\"details\":\"\",\"examples\":\"\",\"type\":\"ml-transformer\",\"nodeClass\":\"fire.nodes.ml.NodeStringIndexer\",\"x\":\"630.238px\",\"y\":\"272.879px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"handleInvalid\",\"value\":\"skip\",\"widget\":\"array\",\"title\":\"Handle Invalid\",\"description\":\"Invalid entries to be skipped or thrown error\",\"optionsArray\":[\"skip\",\"error\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"inputCols\",\"value\":\"[\\\"DAY_OF_MONTH\\\",\\\"DAY_OF_WEEK\\\",\\\"CARRIER\\\",\\\"TAIL_NUM\\\",\\\"FL_NUM\\\",\\\"ORIGIN_AIRPORT_ID\\\",\\\"ORIGIN\\\",\\\"DEST_AIRPORT_ID\\\",\\\"DEST\\\",\\\"CRS_DEP_TIME\\\",\\\"DEP_TIME\\\",\\\"DEP_DELAY_NEW\\\",\\\"CRS_ARR_TIME\\\",\\\"ARR_TIME\\\",\\\"ARR_DELAY_NEW\\\",\\\"CRS_ELAPSED_TIME\\\",\\\"DISTANCE\\\"]\",\"widget\":\"variables_map\",\"title\":\"Input Columns\",\"description\":\"Column containing labels\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputCols\",\"value\":\"[\\\"DAY_OF_MONTH_INDEX\\\",\\\"DAY_OF_WEEK_INDEX\\\",\\\"CARRIER_INDEX\\\",\\\"\\\",\\\"\\\",\\\"ORIGIN_AIRPORT_ID_INDEX\\\",\\\"\\\",\\\"DEST_AIRPORT_ID_INDEX\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\"]\",\"widget\":\"variables_map_edit\",\"title\":\"Output Columns\",\"description\":\"Output  columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"6\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"626.492px\",\"y\":\"63.1289px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"title\",\"value\":\"Row Values\",\"widget\":\"textfield\",\"title\":\"Title\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"7\",\"name\":\"SQL\",\"description\":\"This node runs the given SQL on the incoming DataFrame\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeSQL\",\"x\":\"954.219px\",\"y\":\"59.8711px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"tempTable\",\"value\":\"fire_temp_table\",\"widget\":\"textfield\",\"title\":\"Temp Table\",\"description\":\"Temp Table Name to be used\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"sql\",\"value\":\"select fire_temp_table.* , case  when fire_temp_table.DEP_DELAY_NEW \\u003e 40 then 1.0 else 0.0 END as label from fire_temp_table\",\"widget\":\"textarea_medium\",\"title\":\"SQL\",\"description\":\"SQL to be run\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"schema\",\"value\":\"\",\"widget\":\"tab\",\"title\":\"Schema\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColNames\",\"value\":\"[]\",\"widget\":\"schema_col_names\",\"title\":\"Output Column Names\",\"description\":\"Name of the Output Columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColTypes\",\"value\":\"[]\",\"widget\":\"schema_col_types\",\"title\":\"Output Column Types\",\"description\":\"Data Type of the Output Columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColFormats\",\"value\":\"[]\",\"widget\":\"schema_col_formats\",\"title\":\"Output Column Formats\",\"description\":\"Format of the Output Columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"8\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"927.477px\",\"y\":\"291.137px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"title\",\"value\":\"Row Values\",\"widget\":\"textfield\",\"title\":\"Title\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"}],\"edges\":[{\"source\":\"1\",\"target\":\"2\",\"id\":1},{\"source\":\"2\",\"target\":\"3\",\"id\":2},{\"source\":\"3\",\"target\":\"4\",\"id\":3},{\"source\":\"4\",\"target\":\"5\",\"id\":4},{\"source\":\"5\",\"target\":\"6\",\"id\":5},{\"source\":\"6\",\"target\":\"7\",\"id\":6},{\"source\":\"7\",\"target\":\"8\",\"id\":7}],\"dataSetDetails\":[],\"engine\":\"scala\"}",
  "description": "Find Flights which are delayed by more than 40 minutes.",
  "version": 1,
  "dateCreated": 1566551544583,
  "dateLastUpdated": 1566551544583,
  "lockedByUserId": null,
  "permission": null,
  "workflow": {
    "name": "Analyze Flights Delay",
    "uuid": "3a3dfa34-bbd7-4c05-8745-55628d90cbf6",
    "category": "Analytics",
    "description": "Find Flights which are delayed by more than 40 minutes.",
    "parameters": null,
    "nodes": [
      {
        "id": "1",
        "path": null,
        "name": "DatasetStructured",
        "iconImage": null,
        "description": "This Node creates a DataFrame by reading data from HDFS, HIVE etc. The dataset has been defined earlier in Fire by using the Dataset Feature. As a user, you just have to select the Dataset of your interest.",
        "details": "This Node creates a DataFrame by reading data from HDFS, HIVE etc.<br>\n<br>\nThe data has been defined earlier in Fire by using the Dataset Feature. As a user, you just have to select the Dataset of your interest.<br>",
        "examples": "",
        "type": "dataset",
        "nodeClass": "fire.nodes.dataset.NodeDatasetStructured",
        "x": "38.9492px",
        "y": "275.613px",
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
            "name": "dataset",
            "value": "2ff32692-9b3c-49de-91a7-401daf2590c1",
            "widget": "dataset",
            "title": "Dataset",
            "description": "Selected Dataset",
            "optionsMap": null,
            "datatypes": null,
            "optionsArray": null,
            "required": true,
            "display": true,
            "editable": true,
            "disableRefresh": false
          }
        ],
        "engine": "scala"
       },


Delete Workflow
-------------------

Deletes a workflow with the given workflowId.

* workflowId: 1955

An example request for deleting workflow::


    curl -X DELETE --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflows/id/1955' -b /tmp/cookies.txt
    
An example response:

::

    Workflow deleted successfully.



Get Latest WorkFlows
-------------------- 

Gets the latest workFlows available in the given application:

An example request for getting latest WorkFlows availble in application::



    curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflows/latest' -b /tmp/cookies.txt
    
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

Gets count of the workflows in the given application.

An example request for getting count of the Workflow::


   curl -X GET --header 'token: eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcwMzM3NTQyODY2MSwiaWF0IjoxNzAxNjY4NTc2fQ.YSoEU5w5r4BO2yVVmSRU9NHvk_NwctR43GLG_P52pdG4OTLzlQIhkUL0Y1yBHBny6YZTf9ztVlwY7Bjkyhqjjj' --header 'Accept: application/json'  'https://fire.dev.com/api/v1/workflows/count' --insecure
   
An example response:

::

   92




Get Workflow Versions
------------------------------ 

Gets the versions of workflow.

* workflowId: 1

An example request for getting workflow by id:


::

   curl -X GET --header 'Accept: application/json' 'http://hostname:port/api/v1/workflows/versions?workflowId=1' -b /tmp/cookies.txt
   
An example response:

::

   [
   {
    "id": 1,
    "analysisflowId": 1,
    "content": "{\"name\":\"Analyze Flights Delay\",\"uuid\":\"3a3dfa34-bbd7-4c05-8745-55628d90cbf6\",\"category\":\"Analytics\",\"description\":\"Find Flights which are delayed by more than 40 minutes.\",\"nodes\":[{\"id\":\"1\",\"name\":\"DatasetStructured\",\"type\":\"dataset\",\"nodeClass\":\"fire.nodes.dataset.NodeDatasetStructured\",\"x\":\"38.9492px\",\"y\":\"275.613px\",\"fields\":[{\"name\":\"dataset\",\"value\":\"2ff32692-9b3c-49de-91a7-401daf2590c1\",\"widget\":\"dataset\",\"title\":\"Dataset\",\"description\":\"Selected Dataset\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"2\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"38.4336px\",\"y\":\"59.1094px\",\"fields\":[{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"3\",\"name\":\"CastColumnType\",\"description\":\"This node creates a new DataFrame by casting input columns with a new data type\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeCastColumnType\",\"x\":\"313.223px\",\"y\":\"61.8633px\",\"fields\":[{\"name\":\"inputCols\",\"value\":\"[\\\"CRS_DEP_TIME\\\",\\\"CRS_ARR_TIME\\\",\\\"CRS_ELAPSED_TIME\\\"]\",\"widget\":\"variables\",\"title\":\"Columns\",\"description\":\"Columns to be cast to new data type\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColType\",\"value\":\"DOUBLE\",\"widget\":\"array\",\"title\":\"New Data Type\",\"description\":\"New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)\",\"optionsArray\":[\"BOOLEAN\",\"BYTE\",\"DATE\",\"DOUBLE\",\"FLOAT\",\"INTEGER\",\"LONG\",\"SHORT\",\"STRING\",\"TIMESTAMP\"],\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"4\",\"name\":\"CastColumnType\",\"description\":\"This node creates a new DataFrame by casting input columns with a new data type\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeCastColumnType\",\"x\":\"322.949px\",\"y\":\"275.633px\",\"fields\":[{\"name\":\"inputCols\",\"value\":\"[\\\"DAY_OF_MONTH\\\",\\\"DAY_OF_WEEK\\\"]\",\"widget\":\"variables\",\"title\":\"Columns\",\"description\":\"Columns to be cast to new data type\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColType\",\"value\":\"STRING\",\"widget\":\"array\",\"title\":\"New Data Type\",\"description\":\"New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)\",\"optionsArray\":[\"BOOLEAN\",\"BYTE\",\"DATE\",\"DOUBLE\",\"FLOAT\",\"INTEGER\",\"LONG\",\"SHORT\",\"STRING\",\"TIMESTAMP\"],\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"5\",\"name\":\"StringIndexer\",\"description\":\"StringIndexer encodes a string column of labels to a column of label indices\",\"type\":\"ml-transformer\",\"nodeClass\":\"fire.nodes.ml.NodeStringIndexer\",\"x\":\"630.238px\",\"y\":\"272.879px\",\"fields\":[{\"name\":\"handleInvalid\",\"value\":\"skip\",\"widget\":\"array\",\"title\":\"Handle Invalid\",\"description\":\"Invalid entries to be skipped or thrown error\",\"optionsArray\":[\"skip\",\"error\"],\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"inputCols\",\"value\":\"[\\\"DAY_OF_MONTH\\\",\\\"DAY_OF_WEEK\\\",\\\"CARRIER\\\",\\\"TAIL_NUM\\\",\\\"FL_NUM\\\",\\\"ORIGIN_AIRPORT_ID\\\",\\\"ORIGIN\\\",\\\"DEST_AIRPORT_ID\\\",\\\"DEST\\\",\\\"CRS_DEP_TIME\\\",\\\"DEP_TIME\\\",\\\"DEP_DELAY_NEW\\\",\\\"CRS_ARR_TIME\\\",\\\"ARR_TIME\\\",\\\"ARR_DELAY_NEW\\\",\\\"CRS_ELAPSED_TIME\\\",\\\"DISTANCE\\\"]\",\"widget\":\"variables_map\",\"title\":\"Input Columns\",\"description\":\"Column containing labels\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputCols\",\"value\":\"[\\\"DAY_OF_MONTH_INDEX\\\",\\\"DAY_OF_WEEK_INDEX\\\",\\\"CARRIER_INDEX\\\",\\\"\\\",\\\"\\\",\\\"ORIGIN_AIRPORT_ID_INDEX\\\",\\\"\\\",\\\"DEST_AIRPORT_ID_INDEX\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\"]\",\"widget\":\"variables_map_edit\",\"title\":\"Output Columns\",\"description\":\"Output  columns\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"6\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"626.492px\",\"y\":\"63.1289px\",\"fields\":[{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"7\",\"name\":\"SQL\",\"description\":\"This node runs the given SQL on the incoming DataFrame\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeSQL\",\"x\":\"954.219px\",\"y\":\"59.8711px\",\"fields\":[{\"name\":\"tempTable\",\"value\":\"fire_temp_table\",\"widget\":\"textfield\",\"title\":\"Temp Table\",\"description\":\"Temp Table Name to be used\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"sql\",\"value\":\"select fire_temp_table.* , case  when fire_temp_table.DEP_DELAY_NEW \\u003e 40 then 1.0 else 0.0 END as label from fire_temp_table\",\"widget\":\"textarea_medium\",\"title\":\"SQL\",\"description\":\"SQL to be run\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColNames\",\"value\":\"[]\",\"widget\":\"schema_col_names\",\"title\":\"Output Column Names\",\"description\":\"Name of the Output Columns\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColTypes\",\"value\":\"[]\",\"widget\":\"schema_col_types\",\"title\":\"Output Column Types\",\"description\":\"Data Type of the Output Columns\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColFormats\",\"value\":\"[]\",\"widget\":\"schema_col_formats\",\"title\":\"Output Column Formats\",\"description\":\"Format of the Output Columns\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"8\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"927.477px\",\"y\":\"291.137px\",\"fields\":[{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]}],\"edges\":[{\"source\":\"1\",\"target\":\"2\",\"id\":1},{\"source\":\"2\",\"target\":\"3\",\"id\":2},{\"source\":\"3\",\"target\":\"4\",\"id\":3},{\"source\":\"4\",\"target\":\"5\",\"id\":4},{\"source\":\"5\",\"target\":\"6\",\"id\":5},{\"source\":\"6\",\"target\":\"7\",\"id\":6},{\"source\":\"7\",\"target\":\"8\",\"id\":7}],\"dataSetDetails\":[]}",
    "dateLastUpdated": 1566551544603,
    "userName": null,
    "userId": null,
    "userComment": null
  }
  ],



