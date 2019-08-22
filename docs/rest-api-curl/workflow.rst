Workflows REST API
==================

The Workflow REST API's, allow you to interact with the Workflows.

Below are the various Workflow API's available in Fire Insights. They should be executed after you have logged into Fire Insights.

Get List of workflows
---------------------

Get the list of workflows.

An example request for getting list of workflows:

::

    curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/workflows/all' -b /tmp/cookies.txt
    
An example response:

::

    [
  {
    "id": 1,
    "userId": 1,
    "uuid": "9888b0c6-a385-4875-8958-dc22441e14bd",
    "name": "Analyze Flights Delay",
    "category": "Flights Delay",
    "content": "{\"name\":\"Analyze Flights Delay\",\"uuid\":\"9888b0c6-a385-4875-8958-dc22441e14bd\",\"category\":\"Flights Delay\",\"description\":\"Find Flights which are delayed by more than 40 minutes.\",\"nodes\":[{\"id\":\"1\",\"name\":\"DatasetStructured\",\"description\":\"This Node creates a DataFrame by reading data from HDFS, HIVE etc. The dataset has been defined earlier in Fire by using the Dataset Feature. As a user, you just have to select the Dataset of your interest.\",\"details\":\"This Node creates a DataFrame by reading data from HDFS, HIVE etc.\\u003cbr\\u003e\\n\\u003cbr\\u003e\\nThe data has been defined earlier in Fire by using the Dataset Feature. As a user, you just have to select the Dataset of your interest.\\u003cbr\\u003e\",\"examples\":\"\",\"type\":\"dataset\",\"nodeClass\":\"fire.nodes.dataset.NodeDatasetStructured\",\"x\":\"38.9492px\",\"y\":\"275.613px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"dataset\",\"value\":\"2ff32692-9b3c-49de-91a7-401daf2590c1\",\"widget\":\"dataset\",\"title\":\"Dataset\",\"description\":\"Selected Dataset\",\"required\":true,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"2\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"38.4336px\",\"y\":\"59.1094px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"title\",\"value\":\"Row Values\",\"widget\":\"textfield\",\"title\":\"Title\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"3\",\"name\":\"CastColumnType\",\"description\":\"This node creates a new DataFrame by casting input columns with a new data type\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeCastColumnType\",\"x\":\"313.223px\",\"y\":\"61.8633px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"inputCols\",\"value\":\"[\\\"CRS_DEP_TIME\\\",\\\"CRS_ARR_TIME\\\",\\\"CRS_ELAPSED_TIME\\\"]\",\"widget\":\"variables\",\"title\":\"Columns\",\"description\":\"Columns to be cast to new data type\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColType\",\"value\":\"DOUBLE\",\"widget\":\"array\",\"title\":\"New Data Type\",\"description\":\"New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)\",\"optionsArray\":[\"BOOLEAN\",\"BYTE\",\"DATE\",\"DECIMAL\",\"DOUBLE\",\"FLOAT\",\"INTEGER\",\"LONG\",\"SHORT\",\"STRING\",\"TIMESTAMP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"replaceExistingCols\",\"value\":\"true\",\"widget\":\"array\",\"title\":\"Replace Existing Cols\",\"description\":\"Whether to replace existing columns or create new ones\",\"optionsArray\":[\"true\",\"false\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"4\",\"name\":\"CastColumnType\",\"description\":\"This node creates a new DataFrame by casting input columns with a new data type\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeCastColumnType\",\"x\":\"322.949px\",\"y\":\"275.633px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"inputCols\",\"value\":\"[\\\"DAY_OF_MONTH\\\",\\\"DAY_OF_WEEK\\\"]\",\"widget\":\"variables\",\"title\":\"Columns\",\"description\":\"Columns to be cast to new data type\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColType\",\"value\":\"STRING\",\"widget\":\"array\",\"title\":\"New Data Type\",\"description\":\"New data type(INTEGER, DOUBLE, STRING, LONG, SHORT)\",\"optionsArray\":[\"BOOLEAN\",\"BYTE\",\"DATE\",\"DECIMAL\",\"DOUBLE\",\"FLOAT\",\"INTEGER\",\"LONG\",\"SHORT\",\"STRING\",\"TIMESTAMP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"replaceExistingCols\",\"value\":\"true\",\"widget\":\"array\",\"title\":\"Replace Existing Cols\",\"description\":\"Whether to replace existing columns or create new ones\",\"optionsArray\":[\"true\",\"false\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"5\",\"name\":\"StringIndexer\",\"description\":\"StringIndexer encodes a string column of labels to a column of label indices\",\"details\":\"\",\"examples\":\"\",\"type\":\"ml-transformer\",\"nodeClass\":\"fire.nodes.ml.NodeStringIndexer\",\"x\":\"630.238px\",\"y\":\"272.879px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"handleInvalid\",\"value\":\"skip\",\"widget\":\"array\",\"title\":\"Handle Invalid\",\"description\":\"Invalid entries to be skipped or thrown error\",\"optionsArray\":[\"skip\",\"error\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"inputCols\",\"value\":\"[\\\"DAY_OF_MONTH\\\",\\\"DAY_OF_WEEK\\\",\\\"CARRIER\\\",\\\"TAIL_NUM\\\",\\\"FL_NUM\\\",\\\"ORIGIN_AIRPORT_ID\\\",\\\"ORIGIN\\\",\\\"DEST_AIRPORT_ID\\\",\\\"DEST\\\",\\\"CRS_DEP_TIME\\\",\\\"DEP_TIME\\\",\\\"DEP_DELAY_NEW\\\",\\\"CRS_ARR_TIME\\\",\\\"ARR_TIME\\\",\\\"ARR_DELAY_NEW\\\",\\\"CRS_ELAPSED_TIME\\\",\\\"DISTANCE\\\"]\",\"widget\":\"variables_map\",\"title\":\"Input Columns\",\"description\":\"Column containing labels\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputCols\",\"value\":\"[\\\"DAY_OF_MONTH_INDEX\\\",\\\"DAY_OF_WEEK_INDEX\\\",\\\"CARRIER_INDEX\\\",\\\"\\\",\\\"\\\",\\\"ORIGIN_AIRPORT_ID_INDEX\\\",\\\"\\\",\\\"DEST_AIRPORT_ID_INDEX\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\"]\",\"widget\":\"variables_map_edit\",\"title\":\"Output Columns\",\"description\":\"Output  columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"6\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"626.492px\",\"y\":\"63.1289px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"title\",\"value\":\"Row Values\",\"widget\":\"textfield\",\"title\":\"Title\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"7\",\"name\":\"SQL\",\"description\":\"This node runs the given SQL on the incoming DataFrame\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.etl.NodeSQL\",\"x\":\"954.219px\",\"y\":\"59.8711px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"tempTable\",\"value\":\"fire_temp_table\",\"widget\":\"textfield\",\"title\":\"Temp Table\",\"description\":\"Temp Table Name to be used\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"sql\",\"value\":\"select fire_temp_table.* , case  when fire_temp_table.DEP_DELAY_NEW \\u003e 40 then 1.0 else 0.0 END as label from fire_temp_table\",\"widget\":\"textarea_medium\",\"title\":\"SQL\",\"description\":\"SQL to be run\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"schema\",\"value\":\"\",\"widget\":\"tab\",\"title\":\"Schema\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColNames\",\"value\":\"[]\",\"widget\":\"schema_col_names\",\"title\":\"Output Column Names\",\"description\":\"Name of the Output Columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColTypes\",\"value\":\"[]\",\"widget\":\"schema_col_types\",\"title\":\"Output Column Types\",\"description\":\"Data Type of the Output Columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"outputColFormats\",\"value\":\"[]\",\"widget\":\"schema_col_formats\",\"title\":\"Output Column Formats\",\"description\":\"Format of the Output Columns\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"},{\"id\":\"8\",\"name\":\"PrintNRows\",\"description\":\"Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output\",\"details\":\"\",\"examples\":\"\",\"type\":\"transform\",\"nodeClass\":\"fire.nodes.util.NodePrintFirstNRows\",\"x\":\"927.477px\",\"y\":\"291.137px\",\"fields\":[{\"name\":\"storageLevel\",\"value\":\"DEFAULT\",\"widget\":\"array\",\"title\":\"Output Storage Level\",\"description\":\"Storage Level of the Output Datasets of this Node\",\"optionsArray\":[\"DEFAULT\",\"NONE\",\"DISK_ONLY\",\"DISK_ONLY_2\",\"MEMORY_ONLY\",\"MEMORY_ONLY_2\",\"MEMORY_ONLY_SER\",\"MEMORY_ONLY_SER_2\",\"MEMORY_AND_DISK\",\"MEMORY_AND_DISK_2\",\"MEMORY_AND_DISK_SER\",\"MEMORY_AND_DISK_SER_2\",\"OFF_HEAP\"],\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"title\",\"value\":\"Row Values\",\"widget\":\"textfield\",\"title\":\"Title\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false},{\"name\":\"n\",\"value\":\"10\",\"widget\":\"textfield\",\"title\":\"Num Rows to Print\",\"description\":\"number of rows to be printed\",\"required\":false,\"display\":true,\"editable\":true,\"disableRefresh\":false}],\"engine\":\"scala\"}],\"edges\":[{\"source\":\"1\",\"target\":\"2\",\"id\":1},{\"source\":\"2\",\"target\":\"3\",\"id\":2},{\"source\":\"3\",\"target\":\"4\",\"id\":3},{\"source\":\"4\",\"target\":\"5\",\"id\":4},{\"source\":\"5\",\"target\":\"6\",\"id\":5},{\"source\":\"6\",\"target\":\"7\",\"id\":6},{\"source\":\"7\",\"target\":\"8\",\"id\":7}],\"dataSetDetails\":[],\"engine\":\"scala\"}",
    "description": "Find Flights which are delayed by more than 40 minutes.",
    "version": 1,
    "dateCreated": 1561352487217,
    "dateLastUpdated": 1561352487217,
    "lockedByUserId": null,
    "permission": null,
    "workflow": null,
    "projectId": 1,
    "engine": "scala"
  },

Create / Save A Workflow
------------------------

Creates a new Workflow or updates an existing one.
 
For creating new Workflow set analysisFlowId = null

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d '{"name": "Workflow123","uuid": "","category": null,"description": null,"nodes": [],"edges": []}' 'http://localhost:8080/api/v1/workflows'
    
    
Delete the workflow
-------------------

Deletes a workflow with the given id.

* id: 1

::

    curl -X DELETE --header 'Accept: text/plain' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/id/1'

Execute Workflow Locally Synchronous
------------------------------------

* nodeId : 1
* projectId : 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d '{"name":"SQL","nodes":[],"edges":[]}' 'http://localhost:8080/api/v1/workflows/nodes/1/execute?projectId=1'


Get Latest WorkFlows
-------------------- 

::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/latest'


Get the value of a given field in a Node of a Workflow
------------------------------------------------------

* "nodeId": "2",
* "fieldName": "imageCol"

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 2' --header 'fieldName: imageCol' -d '{"name":"OCR","nodes":[],"edges":[]}' 'http://localhost:8080/getValue1d' -b /tmp/cookies.txt

Get Workflow Count
------------------

::

   curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/count'


Load Example Datasets And Workflows
---------------------------------

::

    curl -X GET --header 'Accept: text/plain' --header 'api_key: cookies' 'http://localhost:8080/api/v1/apps/example-datasets-and-workflows/load'


Get the updated values for a node in the workflow
----------------------------------------------------

* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' --header 'nodeId: 1' -d '{"name":"string","nodes":[],"edges":[]}' 'http://localhost:8080/nodeWithUpdatedValuesJSON' -b /tmp/cookies.txt


Get the list of nodes that are in an inconsistent state - mainly with regard to schema
 
* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: text/html' -d '{"name":"Elastic Search","nodes":[],"edges":[]}' 'http://localhost:8080/nodesInconsistentStateJSON' -b /tmp/cookies.txt



Get the workflow versions
------------------------------ 

::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/versions?workflowId=1'



Get input schema For a Node
------------------
 
* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d  '{"name":"string","nodes":[],"edges":[]}
' 'http://localhost:8080/api/v1/nodes/2/schema/input?projectId=1'


Get output schema of a Node
---------------------------

* nodeId: 1

::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d '{"name":"string","nodes":[],"edges":[]}
' 'http://localhost:8080/api/v1/nodes/2/schema/output?projectId=3'

Get workflow by Id
------------------

* Id : 1

::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/workflows/id/1'

