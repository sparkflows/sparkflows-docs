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
