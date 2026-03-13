MongoDB Connection
=========================
Sparkflows provides the capability to create MongoDB connection and use the connection for reading from and writing to MongoDB tables. Below are the steps for creating MongoDB connection in Sparkflows. The connection can be setup Globally at application level and can also be setup locally for a Project.


To create a **MongoDB Connection** in Sparkflows, follow the steps below:


Step 1 : Login to Sparkflows and Navigate to Connections Page
+++++++
#. Login to Sparkflows by entering your **login credentials** as **admin**.

#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

   .. figure:: ../../../_assets/installation/connection/create_connections/connections_page.png
      :alt: create_connections
      :width: 60%

Step 2 : Adding a MongoDB Connection
+++++++
#. Click on **Add Connection** button from the connections page and choose **Add Connections For All** as shown below. An Add Connection page will open up.

   .. figure:: ../../../_assets/connections/add-global-connection.png
      :alt: connection
      :width: 60%

#. Now, select the category as **Storage** and choose **MongoDB** from the dropdown in the connection type, as shown below.
   
   .. figure:: ../../../_assets/tutorials/mongodb/choose-mongodb.png
      :alt: connection
      :width: 60%


Step 3 : Configuring the MongoDB Connection
+++++++++
#. To configure this connection, enter the details as follows and click on **Test Connection** button to validate it. 

   .. figure:: ../../../_assets/tutorials/mongodb/mongodb-connection.png
      :alt: connection
      :width: 60%

* **Connection Type:** Select **MongoDB** in the **Connection Type** dropdown.
* **Connection Name:** Enter a Identifier for the connection in **Connection Name**.
* **URL:** Enter MongoDB database url.
* **Usename:** Enter login username to access the MongoDB database.
* **Password:** Enter login password to access the MongoDB database.
* **Title:** Enter a Title for the MongoDB connection.
* **Description:** Enter a Description for the MongoDB connection.
* **Driver Class:** Enter the MongoDB driver class name.

#. Once this connection is configured and verified, click on **Save** button to save the connection.
  



