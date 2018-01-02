Datasets REST API
=================

Overview
--------
 
  The Dataset REST API's, allow you to manage the Datasets.

  Below are the various Dataset API's available in Sparkflows

  They should be executed after you have logged into Sparkflows
  
  
Get List of Datasets for the user
---------------------------------
 
Returns the list of Datasets for the logged in user::

    curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "sortPara:desc" -X GET -b /tmp/cookies.txt localhost:8080/datasetsJSON
  
  
Create New Dataset / Save Dataset
---------------------------------
 
The below creates a New Dataset::

if id value is not passed, new dataset will be created::

    {
    "id":13,
    "version":0,
    "name":"spam",
    "header":true,
    "path":"data/spam.csv",
            "delimiter":",",
        "schemaModel":{
    "schemaColList":[
    {
    "colName":"label",
    "colType":"DOUBLE",
    "colFormat":"",
    "colMLType":"NUMERIC"
    },
    {
    "colName":"message",
    "colType":"STRING",
    "colFormat":"",
    "colMLType":"TEXT"
    },
    {
    "colName":"id",
    "colType":"DOUBLE",
    "colFormat":"",
    "colMLType":"NUMERIC"
    }
    ]
    }
    }

     curl-X POST --header 'Content-Type: application/json' --header 'Accept: /' -d     '{"id":13,"version":0,"name":"spam","header":true,"path":"data/spam.csv","delimiter":",","schemaModel":{"schemaColList":    [{"colName":"label","colType":"DOUBLE","colFormat":"","colMLType":"NUMERIC"},{"colName":"message","colType":"STRING","colFormat":"","colMLType":"TEXT"},{"colName":"id","colType":"DOUBLE","colFormat":"","colMLType":"NUMERIC"}]}}' localhost:8080/dataset/save -b /tmp/cookies.txt
 
 
Delete Dataset
--------------
 
Delete Dataset with id = 13::

    curl   -X GET --header 'Accept: application/json' --header 'id: 13' 'localhost:8080/getSelDataset' -b /tmp/cookies.txt
 
Get Hive sample data from given DB and Table
-----------------------------------------------
 
  "db": "default",
  "table": "sample_07"

   **curl -X GET --header 'Accept: application/json' --header 'db: default' --header 'table: sample_07' localhost:8080/hiveSampleData -b /tmp/cookies.txt**
   
 Get Datasets with UUID
 --------------------------
 
**curl -X GET --header 'Accept: application/json' 'localhost:8080/listAllDatasets' -b /tmp/cookies.txt**

Returns sample data
----------------------------
 
  Rdelimiter and header are optional values
  path: data/spam.csv
  schema: {"colNames":["0.0","this is not a spam","3.0"],"colTypes":
  ["DOUBLE","STRING","DOUBLE"],"colFormats":["","",""],"colMLTypes":["NUMERIC","TEXT","NUMERIC"]}


   **curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'path: data/spam.csv' -d '{"colNames":["0.0","this is not a spam","3.0"],"colTypes":["DOUBLE","STRING","DOUBLE"],"colFormats":["","",""],"colMLTypes":["NUMERIC","TEXT","NUMERIC"]}' localhost:8080/sampleData -b /tmp/cookies.txt**

Returns schema of the files in the given path using the given delimiter
-----------------------------------------------------------------------------

  delimiter and header are optional values

  path:data/spam.csv
  schema: {"colNames":["0.0","this is not a spam","3.0"],"colTypes":
  ["DOUBLE","STRING","DOUBLE"],"colFormats":["","",""],"colMLTypes":["NUMERIC","TEXT","NUMERIC"]}


  **curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'path: data/spam.csv' -d '{"colNames":["0.0","this is not a spam","3.0"],"colTypes":["DOUBLE","STRING","DOUBLE"],"colFormats":["","",""],"colMLTypes":["NUMERIC","TEXT","NUMERIC"]}' localhost:8080/schemaForPathJSON -b /tmp/cookies.txt**
  
  
Get Dataset by Id
-----------------------

Get the details of a given dataset::

    "id": "13"

    curl   -X GET --header 'Accept: application/json' --header 'id: 13'   localhost:8080/getSelDataset   -b /tmp/cookies.txt
  
  
Get the list of files/directories in the given path
---------------------------------------------------
 
Gets the list of files in the given path::

    path:data/transaction.csv
         
    curl   -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' -d 'data/transaction.csv' http://localhost:8080/filesInPathJSON -b /tmp/cookies.txt

Get  Dataset Count
----------------------

Returns the count of datasets available::

    curl   -X GET --header 'Accept: application/json' http://localhost:8080/getDatasetCount -b /tmp/cookies.txt
  
Get  Latest Datasets
------------------------------
 
Returns the latest updated datasets::

    curl   --X GET --header 'Accept: application/json' http://localhost:8080/getLatestDatasets -b /tmp/cookies.txt
  
  
 
   
