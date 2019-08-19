HIVE REST API
=============

Overview
--------

The HIVE REST API's, allow you to interact with the HIVE of the Hadoop Cluster Sparkflows is connected to.

Below are the various HIVE REST API's available in Sparkflows

They should be executed after you have logged into Sparkflows

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




