User REST API
==================

Overview
---------

The User REST APIs allow you to get all the information about user and perform create,delete operations too.

Below are the various User APIs available in Fire Insights.

They should be executed after you have logged into Fire Insights.

Get List of Users
-----------------------------------

Returns the list of User.

::

    curl -X GET "http://localhost:8080/api/v1/users" -H "accept: application/json" -b /tmp/cookies.txt
  
Create User
---------------------

::

   curl -X POST "http://localhost:8080/api/v1/users" -H "accept: */*" -H "Content-Type: application/json"  -d "{ \"active\": true, \"email\": \"test@gmail.com\", \"firstName\": \"Testing\", \"groups\": [ 1 ], \"id\": 0, \"isSuperuser\": true, \"lastName\": \"User\", \"password\": \"testUser\", \"roles\": [ 1 ], \"superuser\": true, \"username\": \"Testing\"}" -b /tmp/cookies.txt"

Get User by Id
-------------------

* userId :1(Url Parameter)

::

   curl -X GET "http://localhost:8080/api/v1/users/1" -H "accept: */*" -b /tmp/cookies.txt


Delete User
----------------

* userId : 1

::
 
    curl -X DELETE "http://localhost:8080/api/v1/users/1" -H "accept: */*"  -b /tmp/cookies.txt



