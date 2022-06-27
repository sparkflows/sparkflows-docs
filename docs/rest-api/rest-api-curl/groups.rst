Group REST API
==================

Overview
--------

The Group REST APIs allow you to get all the information of group and perform create,delete operations too.

Below are the various Group REST API's available in Fire Insights.

They should be executed after you have logged into Fire Insights.

Get list of Group
-----------------------------------

::

    curl -X GET "http://localhost:8080/api/v1/groups" -H "accept: application/json" -b /tmp/cookies.txt
  

Create new Group
---------------------

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
::

  curl -X POST "http://localhost:8080/api/v1/groups" -H "accept: */*" -H "Content-Type: application/json" -d "{ \"groupProperties\": [ { \"id\": 0, \"key\": \"key1\", \"value\": \"value1\" }, { \"id\": 0, \"key\": \"key2\", \"value\": \"value2\" } ], \"hdfsLocations\": \"\", \"id\": 0, \"name\": \"Analyst\", \"users\": [ \"admin\", \"test\" ]}"  -b /tmp/cookies.txt

Get Group by id
-------------------------

* Group id :1::

    curl -X GET "http://localhost:8080/api/groups/1" -H "accept: */*" -b /tmp/cookies.txt


Delete Group
-------------------------

* Group id :1::

    curl -X DELETE "http://localhost:8080/api/v1/groups/1" -H "accept: */*" -b /tmp/cookies.txt




