HIVE REST API
=============

Get all Hive Databases
----------------------
 
  curl -X GET --header 'Accept: application/json' 'localhost:8080/hiveDatabases' -b /tmp/cookies.txt
  
  
  
Get Table for a given Database
------------------------------

R"db": "default",
"table": "sample_07"::

  curl  -X GET --header 'Accept: application/json' --header 'db: default' --header 'table: sample_07' 'localhost:8080/hiveTable' -b /tmp/cookies.txt


Get all Hive Tables for given db
--------------------------------

"db": "default"::
 
  curl -X GET --header 'Accept: application/json' --header 'db: default' 'localhost:8080/hiveTables' -b /tmp/cookies.txt
