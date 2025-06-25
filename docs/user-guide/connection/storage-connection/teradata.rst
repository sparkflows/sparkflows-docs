TeraData Connection
================

Fire Insights provides the capability to create a TeraData connection and use the connection to read from and write to TeraData. Below are the steps for creating a TeraData connection in Fire Insights:

  * Download TeraData JDBC Driver
  * Install the JDBC Driver
  * Restart Fire Insights
  * Create the TeraData Connection

Download TeraData JDBC Driver
-------------

- The TeraData JDBC Driver can be downloaded from:https://downloads.teradata.com/download/connectivity/jdbc-driver.
- Use the JAR file for installation in the Fire.

Install the JDBC Driver
--------

In order to install the JDBC driver, copy the driver jdbc jar file into **fire-user-lib** and **fire-server-lib** directories under the Fire installation home directory.

Restart Fire Server
------------

* Once you have copied the JDBC driver into the required folder, **restart** the Fire server with ``./run-fire-server.sh restart`` for it to register the new driver.
  This will restart the Fire services **automatically**.

* Else, you can wait for 60 minutes and the JDBC driver will be automatically registered with Fire Insights.

Create the TeraData Connection
-----

You can ceate the TeraData Connection at **Global**, **Group** or **Project** level. Follow the steps below:

* Login to **Fire Insights**.
* Navigate to **Administration -> Global/Group Connections**.
* From the Connections page, click on **Add Connection** button and choose connection level. An Add Connection dialog box will open.
* Now select connection category as **Storage** and connection type as **TeraData**, as shown below.

  .. figure:: ../../../_assets/installation/connection/teradata_connection.png
     :alt: connection
     :width: 60%

Connection Details
++++

Enter the other configuration details with the help of table given below:


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
     - Choose TeraData as Connection Type
   * - Connection Name
     - Connection Name
     - Add a unique Connection Name
   * - Username 
     - Username
     - Username for TeraData
   * - Password
     - Password
     - Password of TeraData
   * - Title 
     - Title for selected Connection
     - Add a unique Title
   * - Description
     - Connection Description
     - Add a relevant Connection Description
   * - Url
     - Url for TeraData
     - JDBC Url for TeraData
   * - Driver Class
     - Driver Class Name for TeraData
     - com.teradata.jdbc.TeraDriver (by default)
                  
Test & Save the Connection
+++++

* Once you have entered the connection details, click on **Test Connection** button. 
* If the connection is successful,  click on **Save** button to save the connection. Now, you are ready to start using the connection in workflows.


.. Note:: Make sure that the TeraData URL should be accessible from Sparkflows web server URL.



Run Workflows using TeraData JDBC JAR
-----------------

When running workflows, select the **checkbox** for the TeraData JAR file in the Workflow Execution Page.


