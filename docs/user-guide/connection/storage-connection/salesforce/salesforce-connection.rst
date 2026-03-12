Creating Salesforce Connection
======

Sparkflows provides the capability to create a **Salesforce Data Cloud** Connection at Global, Group or Project level and use it for reading from and writing to Salesforce Data Cloud using the **cdata JDBC Driver**.

To create a **Salesforce Connection** in Sparkflows, follow the steps below:

Prerequisite
-----
Before creating a Salesforce JDBC connection in Sparkflows, ensure the following:

- A Salesforce Connected App is configured with OAuth enabled and the required scopes.
- The Consumer Key and Consumer Secret are available from the Connected App.
- The Salesforce Security Token is generated.
- The OAuth Access Token is obtained for authentication.
- The Salesforce Data Cloud JDBC driver is downloaded and installed on the Sparkflows server.

For detailed steps on configuring Salesforce for JDBC access, refer to the documentation below:

https://docs.sparkflows.ai/en/latest/user-guide/connection/storage-connection/salesforce/salesforce-datacloud.html 

Step 1 : Login to Sparkflows and Navigate to Connections Page
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#. Login to Sparkflows by entering your **login credentials** as **admin**.

#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

   .. figure:: ../../../../_assets/installation/connection/create_connections/connections_page.png
      :alt: create_connections
      :width: 60%

Step 2 : Adding a JDBC Salesforce Connection
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
#. Click on **Add Connection** button from the connections page and choose **Add Connections For All** as shown below. An Add Connection page will open up.

   .. figure:: ../../../../_assets/connections/add-global-connection.png
      :alt: connection
      :width: 60%

#. Now, select the category as **Storage** and choose **JDBC** from the dropdown in the **Connection Type**, as shown below.

   .. figure:: ../../../../_assets/connections/choose-jdbc-connection.png
      :alt: connection
      :width: 60%

Step 3 : Configuring the JDBC Salesforce Connection
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
1. To configure this connection, enter the details as follows and click on **Test Connection** button to validate it. 

   .. figure:: ../../../../_assets/user-guide/salesforce/salesforce-jdbc-connection.png
      :alt: Connectors
      :width: 60%

  * **Connection Name:** Enter an Identifier for the connection in **Connection Name**.
  * **URL:** Enter Salesforce database url.
  * **Usename:** Enter login username to access the Salesforce database.
  * **Password:** Enter login password to access the Salesforce database.
  * **Title:** Enter a title for the Salesforce connection.
  * **Description:** Enter a description for the Salesforce connection.
  * **Driver Class:** Enter the Salesforce driver class name.

2. Once the connection is configured and verified, it will display a '**Successfully Connected**' message. Then click on **Save** button to save the connection.

   Now, you are ready to start using the Connection in workflows.

.. Note:: Make sure that salesforce datacloud URL should be accessible from Sparkflows web server URL.






