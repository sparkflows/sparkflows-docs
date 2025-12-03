SharePoint Connection
============
SharePoint is a web-based collaboration and document management platform by Microsoft. It is widely used for enterprise content management, team collaboration, and secure document storage.


To create a **SharePoint Connection** in Sparkflows, follow the steps below:

Step 1 : Login to Sparkflows and Navigate to Connections Page
+++++++
#. Login to Sparkflows by entering your **login credentials** as **admin**.

#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

   .. figure:: ../../../_assets/installation/connection/create_connections/connections_page.png
      :alt: create_connections
      :width: 60%

Step 2 : Adding a SharePoint Connection
+++++++
#. Click on **Add Connection** button from the connections page and choose **Add Connections For All** as shown below. An Add Connection page will open up.

   .. figure:: ../../../_assets/connections/add-global-connection.png
      :alt: connection
      :width: 60%
#. Now, select the category as **Storage** and choose **SharePoint** from the dropdown in the connection type, as shown below.
   
   .. figure:: ../../../_assets/connections/choose-sharepoint-connection.png
      :alt: connection
      :width: 60%


Step 3 : Configuring the SharePoint Connection
+++++++++
#. To configure this connection, enter the API credentials as follows and click on **Test Connection** button to validate it. 

   * **Connection Name:** Enter a relevant name like **Share_Point_Connection**.

   * **Path:** Enter the path as **C:\Users\ABCD-9RX0L93\Downloads**.

   * **Tenant ID:** Enter the specific tenant id (e.g. c7b1ee50-0626-4563-bdfa-d98640ca5d15).

   * **Client ID:** Enter the specific client id (e.g. c3dfdaf8-23ed-4f2b-958d-9bd0bc5ed5f4)

   * **Client Secret:** Enter the secret key.

   * **Site URL:** (e.g. sparkflowsai.sharepoint.com:/sites/SparkflowsProject/)

#. Once this connection is configured and verified, it will display a '**Successfully Connected**' message, as shown below. Then click on **Save** button.
  
   .. figure:: ../../../_assets/connections/added-sharepoint.png
      :alt: connection
      :width: 60%






