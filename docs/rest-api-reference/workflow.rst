Workflow API
==================

The Workflow REST APIs, allow you you to create, update, and delete workflows.

Below are the various Workflow APIs available in Fire Insights. They should be executed after you have logged into Fire Insights.

Create
----------------


.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflows
     - POST  
     
Create a new workflow.
 
An example request for creating workflow:
 
::
 
     {
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
      },
  
An Example response:

:: 

    193

Execute
------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow/execute
     - POST
     
An example request to Execute specific workflow:   

::

    {
     "emailOnFailure": "string",
     "emailOnSuccess": "string",
     "libJars": "string",
     "programParameters": "string",
     "sparkConfig": "string",
     "workflowId": 1
    },

Request Structure

For Executing specific workflow, we need to add below parameters

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - workflowId
     - The canonical identifier of the workflow to Execute. This field is required.
     

An Example response:

::

   200

Update
-----------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflows
     - PUT
     
  
Update an existing workflow

An example request for updating a workflow:

::

    {
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
       },
 

Request Structure

For updating en example workflow, required projectId & workflowId.

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
     
   * - workflowId
     - The canonical identifier of the workflow to update. This field is required.
   
   * - projecId
     - The canonical identifier of the workflow to update. This field is required.

An Example Response:

::

    131

List
--------------


.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflows/all
     - GET  
     
List all workflows. An example response:

::

    [
    {
    "id": 1,
    "userId": 1,
    "uuid": "f0cbdb0a-3415-487c-b7f0-593bf1397ef0",
    "name": "Analyze Flights Delay",
    "category": "Analytics",
    "content": "{\"name\":\"Analyze Flights Delay\",\"uuid\":\"f0cbdb0a-3415-487c-b7f0-593bf1397ef0\",\"category\":\"Analytics\",\"description\":\"Find Flights which are delayed by more than 40 minutes.\",\"nodes\":[{\"id\":\"1\",\"name\":\"DatasetStructured\",\"type\":\"dataset\",\"nodeClass\":\"fire.nodes.dataset.NodeDatasetStructured\",\"x\":\"38.9492px\",\"y\":\"275.613px\",\"fields\":[{\"name\":\"dataset\",\"value\":\"2ff32692-9b3c-49de-91a7-401daf2590c1\",\"widget\":\"dataset\",\"title\":\"Dataset\",\"description\":\"Selected Dataset\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"2\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"38.4336px\",\"y\":\"59.1094px\",\"fields\":[{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"3\",\"name\":\"CastColumnType\",\"description\":\"This node creates a new DataFrame by casting input columns with a new data type\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeCastColumnType\",\"x\":\"313.223px\",\"y\":\"61.8633px\",\"fields\":[{\"name\":\"inputCols\",\"value\":\"[\\\"CRS_DEP_TIME\\\",\\\"CRS_ARR_TIME\\\",\\\"CRS_ELAPSED_TIME\\\"]\",\"widget\":\"variables\",\"title\":\"Columns\",\"description\":\"Columns to be cast to new data type\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColType\",\"value\":\"DOUBLE\",\"widget\":\"array\",\"title\":\"New Data Type\",\"description\":\"New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)\",\"optionsArray\":[\"BOOLEAN\",\"BYTE\",\"DATE\",\"DOUBLE\",\"FLOAT\",\"INTEGER\",\"LONG\",\"SHORT\",\"STRING\",\"TIMESTAMP\"],\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"4\",\"name\":\"CastColumnType\",\"description\":\"This node creates a new DataFrame by casting input columns with a new data type\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeCastColumnType\",\"x\":\"322.949px\",\"y\":\"275.633px\",\"fields\":[{\"name\":\"inputCols\",\"value\":\"[\\\"DAY_OF_MONTH\\\",\\\"DAY_OF_WEEK\\\"]\",\"widget\":\"variables\",\"title\":\"Columns\",\"description\":\"Columns to be cast to new data type\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColType\",\"value\":\"STRING\",\"widget\":\"array\",\"title\":\"New Data Type\",\"description\":\"New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)\",\"optionsArray\":[\"BOOLEAN\",\"BYTE\",\"DATE\",\"DOUBLE\",\"FLOAT\",\"INTEGER\",\"LONG\",\"SHORT\",\"STRING\",\"TIMESTAMP\"],\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"5\",\"name\":\"StringIndexer\",\"description\":\"StringIndexer encodes a string column of labels to a column of label indices\",\"type\":\"ml-transformer\",\"nodeClass\":\"fire.nodes.ml.NodeStringIndexer\",\"x\":\"630.238px\",\"y\":\"272.879px\",\"fields\":[{\"name\":\"handleInvalid\",\"value\":\"skip\",\"widget\":\"array\",\"title\":\"Handle Invalid\",\"description\":\"Invalid entries to be skipped or thrown error\",\"optionsArray\":[\"skip\",\"error\"],\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"inputCols\",\"value\":\"[\\\"DAY_OF_MONTH\\\",\\\"DAY_OF_WEEK\\\",\\\"CARRIER\\\",\\\"TAIL_NUM\\\",\\\"FL_NUM\\\",\\\"ORIGIN_AIRPORT_ID\\\",\\\"ORIGIN\\\",\\\"DEST_AIRPORT_ID\\\",\\\"DEST\\\",\\\"CRS_DEP_TIME\\\",\\\"DEP_TIME\\\",\\\"DEP_DELAY_NEW\\\",\\\"CRS_ARR_TIME\\\",\\\"ARR_TIME\\\",\\\"ARR_DELAY_NEW\\\",\\\"CRS_ELAPSED_TIME\\\",\\\"DISTANCE\\\"]\",\"widget\":\"variables_map\",\"title\":\"Input Columns\",\"description\":\"Column containing labels\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputCols\",\"value\":\"[\\\"DAY_OF_MONTH_INDEX\\\",\\\"DAY_OF_WEEK_INDEX\\\",\\\"CARRIER_INDEX\\\",\\\"\\\",\\\"\\\",\\\"ORIGIN_AIRPORT_ID_INDEX\\\",\\\"\\\",\\\"DEST_AIRPORT_ID_INDEX\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\"]\",\"widget\":\"variables_map_edit\",\"title\":\"Output Columns\",\"description\":\"Output  columns\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"6\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"626.492px\",\"y\":\"63.1289px\",\"fields\":[{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"7\",\"name\":\"SQL\",\"description\":\"This node runs the given SQL on the incoming DataFrame\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeSQL\",\"x\":\"954.219px\",\"y\":\"59.8711px\",\"fields\":[{\"name\":\"tempTable\",\"value\":\"fire_temp_table\",\"widget\":\"textfield\",\"title\":\"Temp Table\",\"description\":\"Temp Table Name to be used\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"sql\",\"value\":\"select fire_temp_table.* , case  when fire_temp_table.DEP_DELAY_NEW \\u003e 40 then 1.0 else 0.0 END as label from fire_temp_table\",\"widget\":\"textarea_medium\",\"title\":\"SQL\",\"description\":\"SQL to be run\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColNames\",\"value\":\"[]\",\"widget\":\"schema_col_names\",\"title\":\"Output Column Names\",\"description\":\"Name of the Output Columns\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColTypes\",\"value\":\"[]\",\"widget\":\"schema_col_types\",\"title\":\"Output Column Types\",\"description\":\"Data Type of the Output Columns\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColFormats\",\"value\":\"[]\",\"widget\":\"schema_col_formats\",\"title\":\"Output Column Formats\",\"description\":\"Format of the Output Columns\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]},{\"id\":\"8\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"927.477px\",\"y\":\"291.137px\",\"fields\":[{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":false,\"editable\":true,\"disableRefresh\":false}]}],\"edges\":[{\"source\":\"1\",\"target\":\"2\",\"id\":1},{\"source\":\"2\",\"target\":\"3\",\"id\":2},{\"source\":\"3\",\"target\":\"4\",\"id\":3},{\"source\":\"4\",\"target\":\"5\",\"id\":4},{\"source\":\"5\",\"target\":\"6\",\"id\":5},{\"source\":\"6\",\"target\":\"7\",\"id\":6},{\"source\":\"7\",\"target\":\"8\",\"id\":7}],\"dataSetDetails\":[]}",
    "description": "Find Flights which are delayed by more than 40 minutes.",
    "version": 0,
    "dateCreated": 1566540807581,
    "dateLastUpdated": 1566540807581,
    "lockedByUserId": null,
    "permission": null,
    "workflow": null,
    "projectId": 1,
    "engine": scala
    },
  
- Response Structure


.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
     
     
   * - workflow
     - List all workflows

Delete
----------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflows/id/{workflowId}
     - DELETE  
     
An example request to delete the workflow:    
 

     
Request Structure

For Deleting a workflow, No action occurs if the workflow has already been deleted. After the workflow is deleted, neither its details nor its run history is visible via the workflow UI or API 

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
     
   * - workflowId
     - The canonical identifier of the workflow to delete. This field is required.
     
An Example Response:
 
::
 
    200




