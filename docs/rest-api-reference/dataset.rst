Dataset API
============

The Dataset REST APIs, allow you to manage the Datasets.

Below are the various Dataset APIs available in Fire Insights. They should be executed after you have logged into Fire Insights.

Create
------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/datasets
     - POST

An example request to Create Dataset:   

::

    {
     "category": "string",
     "datasetSchema": "string",
     "datasetType": "CSV",
     "dateCreated": "2019-08-28T04:19:09.520Z",
     "dateLastUpdated": "2019-08-28T04:19:09.520Z",
     "delimiter": "string",
     "description": "string",
    "filterLinesContaining": "string",
    "header": true,
    "json": "string",
    "name": "string",
    "path": "string",
    "permission": "PERMISSION_NONE",
    "projectId": 33,
    "readOptions": "string",
    "readOptionsModel": {},
    "sampleData": {
    "cells": [
      [
        "string"
      ]
    ],
    "headers": [
      "string"
    ]
    },
     "schemaModel": {
      "schemaColList": [
      {
        "colFormat": "string",
        "colMLType": "NUMERIC",
        "colName": "string",
        "colType": "ARRAY"
      }
    ]
    },
     "userId": 0,
     "uuid": "string",
     "version": 0
    },

Request Structure

For Creating a datset, Id value should not be passed.

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - Id
     - id value should not be passed, As its not required
     
An example response:

::  

    Dataset created successfully.





GET List of Datasets by Application
--------------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/datasets/projects/{projectId}
     - GET

Request Structure

For Getting List of Datasets by Application, Below Parameter are required

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Parameter
     - Value
   
   * - projectId
     - The canonical identifier for Getting List of Datasets by Application. This field is required.
     

An example response:

::  

    {
     "string": "Test",
      "1e13ec2a-4094-405e-a6e7-ffed3bd027f7": "Test-dataset"
    },

Delete Dataset
--------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/datasets/{datasetId}
     - DELETE

Request Structure

For Getting List of Datasets by Application, Below Parameter are required

.. list-table:: 
   :widths: 10 20 40
   :header-rows: 1

   * - Parameter
     - Value
   
   * - datasetId
     - The canonical identifier for Deleting Dataset. This field is required.
   
   * - projectId
     - The canonical identifier for Deleting Dataset. This field is required.
     

An example response with datasetId 98 & projectId 33::

   Dataset with id 98 deleted successfully



