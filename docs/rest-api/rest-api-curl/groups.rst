Group REST API
==================

Overview
--------

The Group REST APIs allow you to get all the information of group and perform create, delete operations too.

Below are the various Group REST APIs available in Sparkflows.

They should be executed after you have logged into Sparkflows.

Get list of Group
-----------------------------------
The command below gets a list of all groups from the specified link

::

    curl -X GET "http://localhost:8080/api/v1/groups" -H "accept: application/json" -b /tmp/cookies.txt
  

Create new Group
---------------------

In order to create a new group
::
    
       curl -X POST "fire-server-url" -H "accept: **" -H "Content-Type: application/json" -d "AUTH_USER.json"

an example of AUTH_USER.json is shown below

JSON
++++

::

    {
        "awsRoleName": "string",
        "groupProperties": [
            {
            "id": 0,
            "propertyKey": "string",
            "propertyValue": "string"
            }],
        "hdfsLocations": "string",
         "id": 0,
        "name": "string",
        "users": [
             "string"
            ]
    }



The script below creates an Analyst group containing the Users admin and test

JSON
++++

::

    {
      "groupProperties": [
        {
          "id": 0,
          "key": "key1",
          "value": "value1"
        },
       {
          "id": 0,
          "key": "key2",
          "value": "value2"
        }
      ],
      "hdfsLocations": "",
      "id": 0,
      "name": "Analyst",
      "users": [
        "admin",
        "test"
      ]
    }
   
::

  curl -X POST "http://localhost:8080/api/v1/groups" -H "accept: */*" -H "Content-Type: application/json" -d "{ \"groupProperties\": [ { \"id\": 0, \"key\": \"key1\", \"value\": \"value1\" }, { \"id\": 0, \"key\": \"key2\", \"value\": \"value2\" } ], \"hdfsLocations\": \"\", \"id\": 0, \"name\": \"Analyst\", \"users\": [ \"admin\", \"test\" ]}"  -b /tmp/cookies.txt

Get Group by id
-------------------------

The script below gets a group based on the id
::
    curl -X GET "fire-host-url:8080/api/groups/$GROUPNUMBER' -H "accept: */*" -b /tmp/cookies.txt
    

For example if we want to get the information about group 1


* Group id :1::

    curl -X GET "http://localhost:8080/api/groups/1" -H "accept: */*" -b /tmp/cookies.txt
    
* Example response ::

    {
      "id": 1,
      "name": "DEFAULT",
      "hdfsLocations": "",
      "groupProperties": [
        {
          "id": 1,
          "key": "key",
          "value": "value"
        },
        {
          "id": 2,
          "key": "key2",
          "value": "value2"
        }
      ]
    }

Delete Group
-------------------------
The command to delete a group is 
::
    
       curl -X DELETE "fire-url-host:8080/ap/v1/groups/$GROUPNUMBER" -H "accept: */*" -b /tmp/cookies.txt 

* For example if we want to delete group1::

    curl -X DELETE "http://localhost:8080/api/v1/groups/1" -H "accept: */*" -b /tmp/cookies.txt




