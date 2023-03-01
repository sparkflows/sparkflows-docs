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
