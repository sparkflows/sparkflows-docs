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

    curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "sortPara:desc" -X GET -b /tmp/cookies.txt localhost:8080/datasetsJSON
         
         
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

Deletes a given Dataset::

    curl   -X GET --header 'Accept: application/json' --header 'id: 13' 'localhost:8080/getSelDataset' -b /tmp/cookies.txt
            
Get Datasets with given UUID
----------------------------

Returns the Datasets with the given UUID's::

    curl -X GET --header 'Accept: application/json' 'localhost:8080/listAllDatasets' -b /tmp/cookies.txt

Get  Dataset Count
------------------

Returns the count of datasets available::

    curl   -X GET --header 'Accept: application/json' http://localhost:8080/getDatasetCount -b /tmp/cookies.txt
         

Get  Latest Datasets
-------------------- 

Returns the latest updated datasets::

    curl   --X GET --header 'Accept: application/json' http://localhost:8080/getLatestDatasets -b /tmp/cookies.txt
    
         
         
            
         
