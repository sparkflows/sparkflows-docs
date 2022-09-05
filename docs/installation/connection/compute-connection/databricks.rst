Databricks Connection
=======

Sparkflows enabled you to create Databricks Connection and use the connection to submit job on respective Databricks Cluster.

Connections can be at various levels:

  * Global : Everyone has access to these connections
  * Group : Users belonging to the group have access to these connections
  * Project : The owner of the project and the groups with which the Project has been shared with have access to the Project level connections

Below are steps on how to create Databricks Connection:

1. Login to Sparkflows WEB Server Url

It can be created by the Administrator under ''Administration/Global Connections''. These connections are available for everyone to use.

GENERAL Tab :

.. list-table:: 
   :widths: 10 20 20
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - CREDENTIAL STORE  
     - Select the Credential Store from drop-down
     - Choose specific Credential Store from drop-down or Select Do not use Credential Store
   * - Select Category
     - Select Category of Connection Type
     - Select Compute Connection
   * - CONNECTION TYPE 
     - Select the Connection type from drop-down
     - Choose Databricks as Connection Type
   * - CONNECTION NAME
     - Connection Name
     - Add an unique Connection Name
   * - TOKEN 
     - Token
     - Add token generated
   * - POSTBACK URL
     - Fire Insights Post Back URL
     - Add Fire Insights Post Back URL
   * - TITLE 
     - Title for selected Connection
     - Add an unique Title
   * - DESCRIPTION
     - Connection Description
     - Add some Connection Description
   * - URL
     - Jdbc url for databricks connection
     - Add Jdbc Url for Databricks Connection
     
.. figure:: /../_assets/installation/connection/databricks_general.PNG
   :alt: connection
   :width: 60%    

DATABRICKS Tab :

.. list-table:: 
   :widths: 10 20 20
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Fire core jar
     - path of Fire core jar dependencies
     - Absolute path of Fire core jar  
   * - Python file
     - path of Pyspark main file
     - Absolute path of Pyspark main file
   * - Fire pyspark libraries
     - path of Fire pyspark libraries
     - Absolute path of Fire pyspark libraries
   * - DBFS Scratch directory
     - Scratch directory on DBFS where it have Read/Write/Delete Permissions.


.. figure:: /../_assets/installation/connection/databricks_other.PNG
   :alt: connection
   :width: 60%    

2.  TEST & Save the Connection

Once you Save the Connection, it can be used for Submitting the job on specific Databricks Cluster.

Documentation
+++++

Reference guide : https://docs.sparkflows.io/en/latest/databricks-user-guide/index.html

.. note:: Make sure to add POSTBACK URL through which Jobs running on Databricks would post back results to Sparkflows using this URL or else it will take from ``app.postMessageURL``, added in configuration.
