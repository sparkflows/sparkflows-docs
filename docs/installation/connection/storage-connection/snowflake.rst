Snowflake
=======

Sparkflows enabled you to create Snowflake Connection and use the connection to access various resources.

Connections can be at various levels:

  * Global : Everyone has access to these connections
  * Group : Users belonging to the group have access to these connections
  * Project : The owner of the project and the groups with which the Project has been shared with have access to the Project level connections

Below are steps on how to create Snowflake Connection:

1. Login to Sparkflows WEB Server Url

It can be created by the Administrator under ''Administration/Global Connections''. These connections are available for everyone to use.


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
     - Select Storage Connection
   * - CONNECTION TYPE 
     - Select the Connection type from drop-down
     - Choose Snowflake as Connection Type
   * - CONNECTION NAME
     - Connection Name
     - Add an unique Connection Name
   * - Username 
     - Username
     - Username for Snowflake
   * - Password
     - Password
     - Password of Snowflake
   * - TITLE 
     - Title for selected Connection
     - Add an unique Title
   * - DESCRIPTION
     - Connection Description
     - Add some Connection Description
   * - URL
     - Url for Snowflake
     - Url for Snowflake

.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/installation/connection/snowflake_storage.PNG
   :alt: connection
   :width: 60%    

.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/installation/connection/snowflake_add.PNG
   :alt: connection
   :width: 60% 

2.  TEST & Save the Connection

Once you Save the Connection, Resouces can be used inside workflow editor etc.

Documentation
+++++

Reference guide : https://docs.sparkflows.io/en/latest/snowflake/index.html
