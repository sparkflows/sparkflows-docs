Test API
----

How can I Test API of Fire Insights?
===========

You can run below curl command:
::

    curl --location --request POST 'http://localhost:8090/messageFromSparkJob' --header 'Content-Type: application/json' --data-raw '{"jobId": "256", "message": "this is test message"}'
    
Expected response of API:
::

    {
    "details": "Fire Exception",
    "message": "Job Id doesn't exist. Please input valid jobId"
    }

.. note::  Make sure to change the localhost to your domain name or your IP where Fire Insights is running.

