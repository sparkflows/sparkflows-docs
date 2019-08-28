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

   * - Parameter
     - Value
   
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

GET Dataset by Id
------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/datasets/{datasetId}
     - GET

Request Structure

For Getting List of Datasets by Application, Below Parameter are required

.. list-table:: 
   :widths: 10 20 40
   :header-rows: 1

   * - Parameter
     - Value
   
   * - datasetId
     - The canonical identifier for Getting Dataset by Id. This field is required.
   
   * - projectId
     - The canonical identifier for Getting Dataset by Id. This field is required.

An example response with datasetId 65 & projectId 33::

  {
    "id": 65,
    "userId": 33,
    "uuid": "1e13ec2a-4094-405e-a6e7-ffed3bd027f7",
    "version": 0,
    "name": "Test-dataset",
    "category": null,
    "description": "Test",
    "header": true,
    "readOptions": null,
    "path": "/user/sparkflows/Clickthru.csv",
    "delimiter": ",",
    "datasetType": "CSV",
    "filterLinesContaining": null,
    "datasetSchema": "{colNames:[\"Timestamp\",\"UserId\",\"IP Address\",\"Product Id\"],colTypes:[\"STRING\",\"INTEGER\",\"STRING\",\"INTEGER\"],colFormats:[\"\",\"\",\"\",\"\"],colMLTypes:[\"TEXT\",\"NUMERIC\",\"TEXT\",\"NUMERIC\"]}",
    "dateCreated": 1566880637842,
    "dateLastUpdated": 1566880637846,
    "permission": null,
    "readOptionsModel": null,
    "schemaModel": {
    "schemaColList": [
      {
        "colName": "Timestamp",
        "colType": "STRING",
        "colFormat": "",
        "colMLType": "TEXT"
      },
      {
        "colName": "UserId",
        "colType": "INTEGER",
        "colFormat": "",
        "colMLType": "NUMERIC"
      },
      {
        "colName": "IP Address",
        "colType": "STRING",
        "colFormat": "",
        "colMLType": "TEXT"
      },
      {
        "colName": "Product Id",
        "colType": "INTEGER",
        "colFormat": "",
        "colMLType": "NUMERIC"
      }
    ]
    },
     "sampleData": {
     "headers": [
      "Timestamp",
      "UserId",
      "IP Address",
      " Product Id"
    ],
    "cells": [
      [
        "9:03 AM",
        "275",
        "207.51.113.192",
        "1"
      ],
      [
        "12:57 AM",
        "586",
        "62.34.98.94",
        "2"
      ],
      [
        "2:45 AM",
        "508",
        "20.237.172.182",
        "3"
      ],
      [
        "2:13 PM",
        "378",
        "69.215.255.150",
        "4"
      ],
      [
        "9:27 AM",
        "965",
        "56.101.183.251",
        "5"
      ],
      [
        "8:18 AM",
        "263",
        "9.151.97.180",
        "6"
      ],
      [
        "9:40 AM",
        "670",
        "101.195.1.186",
        "7"
      ],
      [
        "7:14 AM",
        "447",
        "232.29.216.95",
        "8"
      ],
      [
        "12:57 AM",
        "33",
        "85.119.50.62",
        "9"
      ],
      [
        "12:56 AM",
        "589",
        "185.132.243.178",
        "10"
      ],
      [
        "11:04 PM",
        "22",
        "120.212.232.218",
        "11"
      ],
      [
        "8:29 PM",
        "504",
        "226.70.25.117",
        "12"
      ],
      [
        "5:18 PM",
        "228",
        "213.53.100.18",
        "13"
      ],
      [
        "2:56 PM",
        "536",
        "60.65.25.167",
        "14"
      ],
      [
        "3:57 AM",
        "46",
        "149.156.17.120",
        "15"
      ],
      [
        "8:05 AM",
        "812",
        "23.213.182.107",
        "16"
      ],
      [
        "12:02 PM",
        "980",
        "93.20.165.16",
        "17"
      ],
      [
        "12:53 PM",
        "915",
        "24.180.112.147",
        "18"
      ],
      [
        "11:32 AM",
        "814",
        "110.81.139.11",
        "19"
      ],
      [
        "11:01 PM",
        "429",
        "115.123.246.193",
        "20"
      ]
    ]
    },
  "json": "{\"id\":65,\"userId\":33,\"uuid\":\"1e13ec2a-4094-405e-a6e7-ffed3bd027f7\",\"version\":0,\"name\":\"Test-dataset\",\"description\":\"Test\",\"header\":true,\"path\":\"/user/sparkflows/Clickthru.csv\",\"delimiter\":\",\",\"datasetType\":\"CSV\",\"datasetSchema\":\"{colNames:[\\\"Timestamp\\\",\\\"UserId\\\",\\\"IP Address\\\",\\\"Product Id\\\"],colTypes:[\\\"STRING\\\",\\\"INTEGER\\\",\\\"STRING\\\",\\\"INTEGER\\\"],colFormats:[\\\"\\\",\\\"\\\",\\\"\\\",\\\"\\\"],colMLTypes:[\\\"TEXT\\\",\\\"NUMERIC\\\",\\\"TEXT\\\",\\\"NUMERIC\\\"]}\",\"dateCreated\":\"Aug 27, 2019 4:37:17 AM\",\"dateLastUpdated\":\"Aug 27, 2019 4:37:17 AM\",\"schemaModel\":{\"schemaColList\":[{\"colName\":\"Timestamp\",\"colType\":\"STRING\",\"colFormat\":\"\",\"colMLType\":\"TEXT\"},{\"colName\":\"UserId\",\"colType\":\"INTEGER\",\"colFormat\":\"\",\"colMLType\":\"NUMERIC\"},{\"colName\":\"IP Address\",\"colType\":\"STRING\",\"colFormat\":\"\",\"colMLType\":\"TEXT\"},{\"colName\":\"Product Id\",\"colType\":\"INTEGER\",\"colFormat\":\"\",\"colMLType\":\"NUMERIC\"}]},\"projectId\":33}",
  "projectId": 33
   },
