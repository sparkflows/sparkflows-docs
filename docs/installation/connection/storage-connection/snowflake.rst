Snowflake Connection
=======

Sparkflows provides the capability to create "Snowflake Connection" and use the connection to access various resources.

Connections can be created at various levels:

* Global  : Everyone has access to these connections.
* Group   : Users belonging to a group will only have access to these connections.
* Project : The owner of the project and the groups with which the project has been shared with have access to these connections.

Below are the steps required to create "Snowflake Connection":

1. Login to Sparkflows web server URL.

  It can be created by the administrator under ''Administration/Global Connections''. These connections are available for everyone to use.


   .. list-table:: 
      :widths: 10 20 20
      :header-rows: 1


      * - Title
        - Description
        - Value
      * - Credential Store  
        - Select the Credential Store from drop-down
        - Choose specific Credential Store from drop-down or Select Do not use Credential Store
      * - Select Category
        - Select Category of Connection Type
        - Select Storage Connection
      * - Connection Type 
        - Select the Connection type from drop-down
        - Choose Snowflake as Connection Type
      * - Connection Name
        - Connection Name
        - Add an unique Connection Name
      * - Username 
        - Username
        - Username for Snowflake
      * - Password
        - Password
        - Password of Snowflake
      * - Title 
        - Title for selected Connection
        - Add an unique Title
      * - Description
        - Connection Description
        - Add some Connection Description
      * - Url
        - Url for Snowflake
        - Url for Snowflake

   .. figure:: ../../../_assets/installation/connection/snowflake_storage.PNG
      :alt: connection
      :width: 60%    

   .. figure:: ../../../_assets/installation/connection/snowflake_add.PNG
      :alt: connection
      :width: 60% 

2.  Test and save the connection.

  Once you save the connection, resouces can be used inside workflow editor etc. using the above connection.

Documentation
+++++

Reference guide : https://docs.sparkflows.io/en/latest/snowflake/index.html
