Update workflow
-----------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - http://hostname:port/api/v1/workflows
     - PUT
     
  
Update an existing workflow

An example request for updating a workflow:

::

    {
  "analysisflowId": 129,
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
}' 

Request Structure

For updating the workflow required prope projectID & workflowId.

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
     
   * - workflowId
     - The canonical identifier of the workflow to update. This field is required.
   
   * - projecId
     - The canonical identifier of the workflow to update. This field is required.


