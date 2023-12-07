Databricks
===========

Test connection with Databricks
-------------

Use the command below to get the list of Databricks clusters. It would test whether the Databrics end point is accessible and if the token is good:

  * curl -i https://xxxxx.azuredatabricks.net/api/2.0/clusters/get -H "Authorization: Bearer xxxxx"


Test healthcheck from Databricks Notebook
-----

Use the command below to get the status of healthcheck of Fire Insights application from databricks notebook

::

    %sh curl --location --request GET 'http://host_ip:8080/healthcheck'
    
    
.. figure:: ../_assets/operating/operations/healthcheck.PNG
   :alt: operations
   :width: 80%

.. note::  Make sure to change the host_ip to your domain name or your IP where Fire Insights is running.


Test Connection from Databricks Notebook to Endpoint service URL
----

We need to Ensure that Endpoint services being used for postback url, it should have same Available zone as ec2 instance on which Fire Insights is running, else it will show empty response when running the healthcheck as above

.. figure:: ../_assets/operating/operations/end_2.PNG
   :alt: operations
   :width: 80%
   
.. figure:: ../_assets/operating/operations/end_3.PNG
   :alt: operations
   :width: 80%   


Also you need to Ensure that Endpoint services being used for postback url, it should have Enable cross-zone load balancing used for Fire Insight application, else it will show communication error.

.. figure:: ../_assets/operating/operations/cross_zone.PNG
   :alt: operations
   :width: 80% 
