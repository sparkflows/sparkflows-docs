Create-workflows
------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - http://localhost:8080/api/v1/workflows
     - GET  
     
 Create a new workflow.
 
 An example request for creating workflow:
 
 ::
 
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
