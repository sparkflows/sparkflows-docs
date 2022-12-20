MySQL Connection
================

Sparkflows provides the capability to create MySQL Connection and use the connection to access various resources.

Connections can be at various levels:

* Global : Everyone has access to these connections
* Group : Users belonging to a group will only have access to these connections
* Project : The owner of the project and the groups with which the project has been shared with have access to these connections

Below are steps on how to create MySQL Connection:

1. Login to Sparkflows as an ``Admin``. Click on ``Administrator`` tab from main menu. Click on  ``Global Connections`` and then click on ``Add Connection`` and fill in the details as shown below to create the connection.


      .. figure:: ../../../_assets/aws/livy/administration.PNG
         :alt: livy
         :width: 60%

      .. figure:: ../../../_assets/installation/connection/mysql_storage.PNG
         :alt: connection
         :width: 60%

      .. figure:: ../../../_assets/installation/connection/mysql_connections.PNG
         :alt: connection
         :width: 60%  

      .. list-table:: 
         :widths: 10 20 20
         :header-rows: 1

         * - Credential Store  
           - Select the Credential Store from drop-down
           - Choose specific Credential Store from drop-down or Select Do not use Credential Store
         * - Select Category
           - Select Category of Connection Type
           - Select Storage Connection
         * - Connection Type 
           - Select the Connection type from drop-down
           - Choose MySQL as Connection Type
         * - Connection Name
           - Connection Name
           - Add an unique Connection Name
         * - Username 
           - Username
           - Username for MySQL
         * - Password
           - Password
           - Password of MySQL
         * - Title 
           - Title for selected Connection
           - Add an unique Title
         * - Description
           - Connection Description
           - Add some Connection Description
         * - Url
           - Url for MySQL
           - JDBC Url for MySQL
         * - Driver Class
           - Driver Class Name for MySQL
           - com.mysql.jdbc.Driver (by default)
      

2. Test Connection and Save

    Once you have entered the values to the parameters, click on ``Test Connection``. If the Connection is Successful, ``Save`` the connection.

    Now you can created connection use the resources in datasets and workflows.

.. Note:: Make sure that MySQL URL should be accessible from Sparkflows webserver URL.
