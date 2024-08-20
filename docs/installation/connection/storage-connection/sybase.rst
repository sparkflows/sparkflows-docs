Sybase Connection
================

Sparkflows provides the capability to create Sybase JDBC Connection and use the connection to access various resources.

Connections can be created at various levels:

* Global  : Everyone has access to these connections.
* Group   : Users belonging to a group will only have access to these connections.
* Project : The owner of the project and the groups with which the project has been shared with have access to these connections.

This document explains in detail the necessary steps required to create a Sybase JDBC Connection. 

Below are the steps required to create Sybase JDBC Connection :

Step 1 : Prerequisites
----------

Before you start setting up the Sybase Connection, ensure you have the Sybase installed and server running and make sure to:

#. Download the necessary Sybase JAR file by following this link: `Sybase JAR <https://osdn.net/projects/sfnet_id2d/downloads/jdbc%20drivers/jconn4.jar/>`_
#. Copy the JAR file into both the **fire-user-lib** and **fire-core-lib** folders located within the Sparkflows home directory.
#. Copy the JAR file into the ``/home/sparkflows/venv/lib/python3.7/site-packages/pyspark/jars/`` if using PySpark engine, it need to be updated on the basis of your python environment.
#. Start the Fire Server after you finish copying the JAR file.


Step 2 : Login to Fire Insights as Admin
-----------------

To Login :

#. Go to Fire Insights Login Page.
#. Enter your credentials.
#. Click **Sign in**. You will reach Fire Dashboard.

Step 3 : Add Connection 
--------------
To open Connections Page and add connection :

#. From the Fire Dashboard, click **ADMINISTRATION** located in the top menu-bar.
#. From the Administration Page, click **Global Connections** to reach Connections Page.

   .. figure:: ../../../_assets/postgresql/administration.png
      :alt: postgresql
      :width: 60%

#. From the Connections Page, click **Add Connection**.

   .. figure:: ../../../_assets/postgresql/add-connection.png
      :alt: postgresql
      :width: 60%

#. Choose the type of connection as per your requirement from the dropdown menu.

Step 4 : Enter Parameter Details
----------
#. In the Add Connection Window, fill in all the details as shown below.

   .. figure:: ../../../_assets/connections/sybase-storage.png
      :alt: sybase
      :width: 60%

   
   .. figure:: ../../../_assets/connections/sybase-connection.png
      :alt: sybase
      :width: 60%  

   **Note:** For more information on the details to be filled in, refer the below table.

   .. list-table:: 
      :widths: 25 25 50
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
        - Choose JDBC as Connection Type
      * - Connection Name
        - Connection Name
        - Add a unique Connection Name
      * - Username 
        - Username
        - Username for Sybase
      * - Password
        - Password
        - Password for Sybase
      * - Title 
        - Title for selected Connection
        - Add a unique Title
      * - Description
        - Connection Description
        - Add some Connection Description
      * - Url
        - Url for Sybase
        - JDBC Url for Sybase
      * - Driver Class
        - Driver Class Name for Sybase
        - com.sybase.jdbc4.jdbc.SybDriver (by default)

.. Note:: Url for Sybase: jdbc:sybase:Tds:hostname:port/database

Step 5 : Test and Save the Connection
-------

#. Once you have entered the values to the parameters, click **Test Connection**. 
#. On successful testing, click **Save** to save the connection. 

Step 6 : Create Connection
----------
After successfully completing the above steps, you can proceed to create the connection using the resources in datasets and workflows.

.. Note:: Make sure that "Sybase URL" should be accessible from Sparkflows web server URL and suitable Driver should be copied to fire lib and do select sybase jar while submitting workflow.
