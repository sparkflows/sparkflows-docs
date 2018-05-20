Workflows REST API
==================

The Workflow REST API's, allow you to interact with the Workflows.

Below are the various Workflow API's available in Sparkflows

They should be executed after you have logged into Sparkflows

Get List of workflows
---------------------

Returns the list of workflows for the logged in user.

* Header: sortPara:asc/desc.

::

    curl -i --header "Accept:application/json" -H "Content-Type:application/json" -H "sortPara:desc" -X GET -b /tmp/cookies.txt localhost:8080/workflowsJSON

