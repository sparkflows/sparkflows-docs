Import Workflow REST API
==================

The Import Workflow REST API allow you to import workflow through exported workflow json.

Below is the Import Workflow API available in Sparkflows. They should be executed after you generate access token for user in Sparkflows.


An example request for importing specified workflow json file:

::
 
 curl --location --request POST 'http://localhost:8080/api/v1/workflows/import?projectId=2&uuidOption=createNewUUID' \
 --header 'token: eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY2NTQzNzI4NDQ1OSwiaWF0IjoxNjYzNzY4MzMyfQ.uOA_9CO9uRxIT8WuS3ceL8I1k1nON-X4Bv4L8gfWEsNKnTYb-Bsgym08qvmDI6O51xFA-wkZhDv5reX3r0GPbQ' \
 --form 'file=@"/C:/Users/NMBR/Downloads/readcsvAndPrintRows.json"'


* projectId : Project Id where added workflow json file needs to imported.
* uuidOption: UUID Option can be any one of these 3 below options
            * createNewUUID : Create new Workflow with new UUID
            * createNewUUIDIfExist : First, it checks if UUID similar to one in imported json file is present in added project id or not. If present then create new workflow with new UUID and if not then, create new workflow with UUID present in json file.
            * overwriteWorkflowIfUUIDExistInProject : It checks if UUID similar to one in imported json file is present in added project id. If Workflow is present with same UUID then overwrite content in json file in existing workflow. Else, create new workflow with UUID present in json file.

An example of exported Workflow JSON file:

JSON
++++

::

    {
  "name": "readcsvAndPrintRows",
  "uuid": "799d922b-f2b6-4e0d-bafa-d6d784b7cf1c",
  "category": "-",
  "nodes": [
    {
      "id": "1",
      "name": "Read CSV",
      "description": "It reads in CSV files and creates a DataFrame from it",
      "type": "dataset",
      "nodeClass": "fire.nodes.dataset.NodeDatasetCSV",
      "x": "323px",
      "y": "291px",
      "hint": "Whenever the file is changed, Refresh the Schema",
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
          "value": "\\spark3\\fire\\data\\churn_prediction\\churn.all",
          "widget": "textfield",
          "title": "Path",
          "description": "Path of the Text file/directory",
          "required": false,
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
          "value": "false",
          "widget": "array",
          "title": "Header",
          "description": "Whether the file has a header row",
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
          "name": "dropSpecialCharacterInColumnName",
          "value": "true",
          "widget": "array",
          "title": "Drop Special Character In ColumnName",
          "description": "Whether to drop the Special Characters and Spaces in Column Name.",
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
          "name": "mode",
          "value": "PERMISSIVE",
          "widget": "array",
          "title": "Mode",
          "description": "Mode for dealing with corrupt records during parsing.",
          "optionsArray": [
            "PERMISSIVE",
            "DROPMALFORMED",
            "FAILFAST"
          ],
          "required": false,
          "display": true,
          "editable": true,
          "disableRefresh": false
        },
        {
          "name": "enforceSchema",
          "value": "false",
          "widget": "array",
          "title": "Enforce Schema",
          "description": "If it is set to true, the specified or inferred schema will be forcibly applied to datasource files, and headers in CSV files will be ignored. If the option is set to false, the schema will be validated against all headers in CSV files in the case when the header option is set to true.",
          "optionsArray": [
            "false",
            "true"
          ],
          "required": false,
          "display": true,
          "editable": true,
          "disableRefresh": false
        },
        {
          "name": "addInputFileName",
          "value": "false",
          "widget": "array",
          "title": "Whether to add Input File Name as a column in the Dataframe",
          "description": "Add the new field:input_file_name",
          "optionsArray": [
            "false",
            "true"
          ],
          "required": false,
          "display": true,
          "editable": true,
          "disableRefresh": false
        },
        {
          "name": "outputColNames",
          "value": "[\"C0\",\"C1\",\"C2\",\"C3\",\"C4\",\"C5\",\"C6\",\"C7\",\"C8\",\"C9\",\"C10\",\"C11\",\"C12\",\"C13\",\"C14\",\"C15\",\"C16\",\"C17\",\"C18\",\"C19\",\"C20\"]",
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
          "value": "[\"STRING\",\"DOUBLE\",\"DOUBLE\",\"STRING\",\"STRING\",\"STRING\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"DOUBLE\",\"STRING\"]",
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
          "value": "[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"]",
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
      "name": "Print N Rows",
      "description": "Prints the specified number of records in the DataFrame. It is useful for seeing intermediate output",
      "type": "transform",
      "nodeClass": "fire.nodes.util.NodePrintFirstNRows",
      "x": "469px",
      "y": "282px",
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
        },
        {
          "name": "displayDataType",
          "value": "true",
          "widget": "array",
          "title": "Display Data Type",
          "description": "If true display rows DataType",
          "optionsArray": [
            "true",
            "false"
          ],
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
}
