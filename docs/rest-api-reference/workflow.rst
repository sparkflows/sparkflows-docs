Workflows REST API
==================

The Workflow REST API's, allow you you to create, edit, and delete workflows.

Below are the various Workflow API's available in Fire Insights. They should be executed after you have logged into Fire Insights.

Create workflows
----------------


.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - http://hostname:port/api/v1/workflows
     - POST  
     
Create a new workflow.
 
An example request for creating workflow:
 
::
 
     [
  "analysisflowId": 0,
  "comment": "string",
  "projectId": 1,
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
  },
  
An Example response:

:: 

    97

Execute workflow
------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - http://hostname:port/api/v1/workflow/execute
     - POST
     
An example request to Execute specific workflow:   

::

    {
	"name": "Test_workflow",
	"uuid": "2dfd33ee-b43c-4135-8d9f-be420121fc12",
    "workflowId": 131,
    "projectId": 33,
	"category": "-",
	"nodes": [
		{
			"id": "1",
			"name": "ReadCSV",
			"description": "It reads in CSV files and creates a DataFrame from it",
			"details": "",
			"examples": "",
			"type": "dataset",
			"nodeClass": "fire.nodes.dataset.NodeDatasetCSV",
			"x": "234.819px",
			"y": "56.3229px",
			"fields": [
				{
					"name": "storageLevel",
					"value": "DEFAULT",
					"widget": "array",
					"title": "Output Storage Level",
					"description": "Storage Level of the Output Datasets of this Node",
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
					"required": false,
					"display": true,
					"editable": true,
					"disableRefresh": false
				}
			],
			"engine": "all"
		},
		{
			"id": "2",
			"name": "PrintNRows",
			"description": "Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output",
			"details": "",
			"examples": "",
			"type": "transform",
			"nodeClass": "fire.nodes.util.NodePrintFirstNRows",
			"x": "431.826px",
			"y": "55.3229px",
			"fields": [
				{
					"name": "storageLevel",
					"value": "DEFAULT",
					"widget": "array",
					"title": "Output Storage Level",
					"description": "Storage Level of the Output Datasets of this Node",
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
					"name": "title",
					"value": "Row Values",
					"widget": "textfield",
					"title": "Title",
					"required": false,
					"display": true,
					"editable": true,
					"disableRefresh": false
				},
				{
					"name": "n",
					"value": "10",
					"widget": "textfield",
					"title": "Num Rows to Print",
					"description": "number of rows to be printed",
					"required": false,
					"display": true,
					"editable": true,
					"disableRefresh": false
				}
			],
			"engine": "all"
		}
	],
	"edges": [
		{
			"source": "1",
			"target": "2",
			"id": 1
		}
	],
	"dataSetDetails": [],
	"engine": "scala"
},

Request Structure

For Executing specific workflow, we need to add below parameters

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - projectId
     - The canonical identifier of the workflow to Execute. This field is required.
   
   * - workflowId
     - The canonical identifier of the workflow to Execute. This field is required.
     

An Example response:

::

   200

Delete workflow
----------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - http://hostname:port/api/v1/workflows/id/{workflowId}
     - DELETE  
     
An example request to delete the workflow:    
 
::

     {
    "workflowId": 130
    }    
     
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
 
    Workflow deleted successfully.





