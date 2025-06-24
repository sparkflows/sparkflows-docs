SAP HANA Connection
=====
Fire Insights provides the capability to create a SAP HANA connection and use the connection to read from and write to SAP HANA. Below are the steps for creating a SAP HANA connection in Fire Insights:

* Download SAP HANA JDBC Driver
* Install the SAP HANA JDBC Driver
* Restart Fire Insights
* Create the SAP HANA Connection

Download SAP HANA JDBC Driver
----
**(A) Download SAP HANA JDBC Driver from MVN Repository**

  The SAP HANA JDBC Driver can be downloaded from the link given below:

  https://mvnrepository.com/artifact/com.sap.cloud.db.jdbc/ngdbc

**(B) Download SAP HANA JDBC Driver from SAP Service Marketplace**

  * Go to the SAP Service Marketplace through the link provided here: http://service.sap.com/connectors
  * You will need SAP credentials to access the Service Marketplace.
  * Download the **ngdbc.jar** file and install it on the Fire Insights machine.

Install the SAP HANA JDBC Driver
----
In order to install the JDBC driver, copy the driver jdbc jar file (``ngdbc.jar``) into **fire-user-lib** and **fire-server-lib** directories under the Fire installation home directory.

Restart Fire Insights
----
* To register the new driver, run the following command in the terminal to automatically restart Fire Insights application.
  ::
     ./run-fire-server.sh restart


* Or else you can wait for 60 minutes, and Fire Insights will auto-register the JDBC driver.


Create the SAP HANA Connection
----
You can create the connection at **Global**, **Group**, or **Project level**.

To create SAP HANA connection in Fire Insights, follow the steps below:

* Login to **Fire Insights**.
* Navigate to **Administration -> Global/Group Connections**.
* From the Connections page, click on **Add Connection** button and choose connection level. An Add Connection dialog box will open.
* Now select connection category as **Storage** and connection type as **SAP HANA**, as shown below.

  .. figure:: ../../../_assets/installation/connection/sap-add-connection.png
     :alt: connection
     :width: 60%


* Enter the other configuration details with the help of table given below:


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
       - Choose SAP HANA as Connection Type
     * - Connection Name
       - Connection Name
       - Add a unique Connection Name
     * - Username 
       - Username
       - Username for SAP HANA
     * - Password
       - Password
       - Password of SAP HANA
     * - Title 
       - Title for selected Connection
       - Add a unique Title
     * - Description
       - Connection Description
       - Add relevant Connection Description
     * - Url
       - Url for SAP HANA
       - JDBC Url for SAP HANA
     * - Driver Class
       - Driver Class Name for SAP HANA
       - com.sap.db.jdbc.Driver (by default)

  .. figure:: ../../../_assets/installation/connection/sap-connection-details.png
       :alt: connection
       :width: 60%



* Once you have entered the connection details, click on **Test Connection** button. If the connection is successful, click on **Save** button to save the connection.

* Now, you are ready to start using the Connection in workflows. When running workflows, select the **checkbox** for the **SAP HANA JAR file** in the Workflow Execution Page.

.. note:: Make sure that the SAP HANA URL should be accessible from the Sparkflows web server URL.































