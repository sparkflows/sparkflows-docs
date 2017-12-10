Datasets REST API
-----------------

Overview
-----
 
  The Dataset REST API's, allow you to manage the Datasets.

  Below are the various Dataset API's available in Sparkflows

  They should be executed after you have logged into Sparkflows
  
  
Get List of Datasets for the user
-----------------------------------------
 
  Returns the list of Datasets for the logged in user.

  **curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "sortPara:desc" -X GET -b /tmp/cookies.txt localhost:8080/datasetsJSON**
  
  
Create New Dataset / Save Dataset
---------------------------------
 
if id value is not passed, new dataset will be created.
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

 **curl-X POST --header 'Content-Type: application/json' --header 'Accept: /' -d '{"id":13,"version":0,"name":"spam","header":true,"path":"data/spam.csv","delimiter":",","schemaModel":{"schemaColList":[{"colName":"label","colType":"DOUBLE","colFormat":"","colMLType":"NUMERIC"},{"colName":"message","colType":"STRING","colFormat":"","colMLType":"TEXT"},{"colName":"id","colType":"DOUBLE","colFormat":"","colMLType":"NUMERIC"}]}}' localhost:8080/dataset/save -b /tmp/cookies.txt**
 
 Delete Dataset
 -------------------
 
  "id": "36"

   **curl   -X GET --header 'Accept: application/json' --header 'id: 13' 'localhost:8080/getSelDataset' -b /tmp/cookies.txt**
 
Get Hive sample data from given DB and Table
-----------------------------------------------
 
  "db": "default",
  "table": "sample_07"

         **curl -X GET --header 'Accept: application/json' --header 'db: default' --header 'table: sample_07' localhost:8080/hiveSampleData -b /tmp/cookies.txt**
