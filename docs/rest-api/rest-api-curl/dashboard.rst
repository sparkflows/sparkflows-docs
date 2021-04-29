Dashboard REST API
==================

Overview
---------

The Dashboards REST API's, allow you to interact with the Dashboards.

Below are the various Dashboard API's available in Sparkflows

They should be executed after you have logged into Sparkflows

Get List of Dashboards for the user
-----------------------------------

Returns the list of dashboards for the logged in user.

* Header: sortPara:asc/desc.

::

    curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "sortPara:desc" -X GET -b /tmp/cookies.txt localhost:8080/dashboardsJSON
  
Create New Dashboard / Save Dashboard
-------------------------------------

Set dashboardId value null to create new dashboard::

  curl - X POST --header 'Content-Type: application/json' --header 'Accept: text/plain' --header 'dashboardId: null' -d '{"category": "string", "description": "string","name": "string","sheets": [{"description": "string","idx": "string","items": [ {"description": "string","id": 0,"name": "string","nodeId": "string","type": "string", "workflowId": "string","workflowName": "string","x": "string","y": "string"}],"name":"string","type": "string"}],"uuid": "string"}' 'http://localhost:8080/saveDashboard' -b /tmp/cookies.txt
  
Get Dashboard by Id
-------------------

* id:1(Url Parameter)

::

    curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/dashboards?sortPara=dsc&projectId=1' -b /tmp/cookies.txt

Get dashboard results
---------------------

* dashboardId:1
* sheetId:0

::

    curl -X GET --header 'Accept: application/json' 'http://localhost:8080/api/v1/dashboards/results?dashboardId=1&sheetId=0' -b /tmp/cookies.txt

update dashboard
-----------------

* dashboardContent: abcd,
* dashboardId: 1,

::

   curl -X PUT --header 'Content-Type: application/json' --header 'Accept: */*' -d 'abcd' 'http://localhost:8080/api/v1/dashboards/1'

Delete Dashboard
----------------

* dashboardId: 1,
* projectId: 1,

::
 
    curl -X DELETE --header 'Accept: text/plain' 'http://localhost:8080/api/v1/dashboards/1?projectId=1' -b /tmp/cookies.txt



