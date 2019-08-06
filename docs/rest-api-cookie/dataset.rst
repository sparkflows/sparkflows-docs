Datasets REST API
=================

Overview
--------

The Dataset REST API's, allow you to manage the Datasets.

Below are the various Dataset API's available in Sparkflows

They should be executed after you have logged into Sparkflows
    
    
Get List of Datasets
--------------------

Returns the list of Datasets for the logged in user::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/datasets?sortPara=dsc&projectId=1'
         
         
Create / Update Dataset
-----------------------

If id value is not passed, new dataset will be created::

JSON
++++

::

    {
      "id": 13,
      "version": 0,
      "name": "spam",
      "header": true,
      "path": "data\/spam.csv",
      "delimiter": ",",
      "schemaModel": {
        "schemaColList": [
          {
            "colName": "label",
            "colType": "DOUBLE",
            "colFormat": "",
            "colMLType": "NUMERIC"
          },
          {
            "colName": "message",
            "colType": "STRING",
            "colFormat": "",
            "colMLType": "TEXT"
          },
          {
            "colName": "id",
            "colType": "DOUBLE",
            "colFormat": "",
            "colMLType": "NUMERIC"
          }
        ]
      }
    }


Curl
++++

::

    curl-X POST --header 'Content-Type: application/json' --header 'Accept: /' -d     '{"id":13,"version":0,"name":"spam","header":true,"path":"data/spam.csv","delimiter":",","schemaModel":{"schemaColList":[{"colName":"label","colType":"DOUBLE","colFormat":"","colMLType":"NUMERIC"},{"colName":"message","colType":"STRING","colFormat":"","colMLType":"TEXT"},{"colName":"id","colType":"DOUBLE","colFormat":"","colMLType":"NUMERIC"}]}}' localhost:8080/dataset/save -b /tmp/cookies.txt
       
       
Delete Dataset
--------------------
* "datasetId": "13"
* "projectId": "13"
::

Deletes a given Dataset::

    curl -X DELETE --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/datasets/1?projectId=1'
    
Get Dataset by Id
-----------------

* "id": "13"
* "projectId": "13"

::

        curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/datasets/13?projectId=1'
         
         
Get  Dataset Count
------------------

Returns the count of datasets available::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/v1/datasets/count'
         

Get sample data
------------------ 

Delimiter and header are optional values

* path: data/spam.csv
* schema: {"colNames":["0.0","this is not a spam","3.0"],"colTypes":["DOUBLE","STRING","DOUBLE"],"colFormats":["","",""],"colMLTypes":["NUMERIC","TEXT","NUMERIC"]}

CURL::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d
    '{"colNames":["0.0","this is not a spam","3.0"],"colTypes":["DOUBLE","STRING","DOUBLE"],"colFormats":["","",""],"colMLTypes":["NUMERIC","TEXT","NUMERIC"]}' http://localhost:8080/api/v1/datasets/sample-data


Returns schema of the files in the given path using the given delimiter
-----------------------------------------------

* delimiter and header are optional values
* path:data/spam.csv
* schema: {"colNames":["0.0","this is not a spam","3.0"],"colTypes":["DOUBLE","STRING","DOUBLE"],"colFormats":["","",""],"colMLTypes":["NUMERIC","TEXT","NUMERIC"]}


CURL::

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header 'api_key: cookies' -d 
    '{"colNames":["0.0","this is not a spam","3.0"],"colTypes":["DOUBLE","STRING","DOUBLE"],"colFormats":["","",""],"colMLTypes":["NUMERIC","TEXT","NUMERIC"]}' http://localhost:8080/api/v1/datasets/schema
         
         
Get  Latest Datasets
-------------------- 

Returns the latest updated datasets::

    curl -X GET --header 'Accept: application/json' --header 'api_key: cookies' 'http://localhost:8080/api/datasets/latest'
    
         
         
Get the list of files/directories in the given path
--------------------------------------------------- 

* path:data/transaction.csv
  
CURL::

    curl   -X GET --header 'Content-Type: application/json' --header 'Accept: application/json' -d 'data/transaction.csv' 'http://localhost:8080/filesInPathJSON -b /tmp/cookies.txt'
    
    

            
         
