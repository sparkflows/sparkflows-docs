List workflows
--------------


.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - http://hostname:8080/api/v1/workflows/all
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
