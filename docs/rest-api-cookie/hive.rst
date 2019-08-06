HIVE REST API
=============

Get all Hive Databases
----------------------

::

  curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/hive/databases' -b /tmp/cookies.txt
  
Get Table for a given Database
------------------------------

* "db": "default",
* "table": "sample_07"

::

    curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/hive/tables?db=default&table=sample_07' -b /tmp/cookies.txt
  
Get all Hive Databases
----------------------

::

  * curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/hive/databases' -b /tmp/cookies.txt




