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

It can also be created by any user with their Application. In this case, it is only available to the Application and its users.

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
     - Select Databricks
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
     


.. note:: Make sure to add POSTBACK URL through which Jobs running on Databricks would post back results to Fire Insights using this URL or else it will take from ``app.postMessageURL``, added in configuration.
