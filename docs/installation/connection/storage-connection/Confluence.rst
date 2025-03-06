Confluence
===========
Confluence is a collaboration and documentation platform that teams to create, share, and manage knowledge within a structured workspace, making it a powerful tool for project documentation and team collaboration.

To create a **Confluence Connection** in Sparkflows, follow the steps below:

Step 1 : Login to Fire Insights and Navigate to Connections Page
+++++++
#. Login to Fire Insights by entering your **login credentials** as **admin**.

#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

   .. figure:: ../../../_assets/installation/connection/create_connections/connections_page.png
      :alt: create_connections
      :width: 60%

Step 2 : Adding a Confluence Connection
+++++++
#. Click on **Add Connection** button from the connections page and choose **Add Connections For All** as shown below. An Add Connection page will open up.

   .. figure:: ../../../_assets/connections/add-global-connection.png
      :alt: connection
      :width: 60%
#. Now, select the category as **Storage** and choose **Confluence** from the dropdown in the connection type, as shown below.
   
   .. figure:: ../../../_assets/connections/choose-confluence-connection.png
      :alt: connection
      :width: 60%


Step 3 : Configuring the Confluence Connection
+++++++++
#. To configure this connection, enter the API credentials as follows and click on **Test Connection** button to validate it. 

   * **Connection Name:** Enter the relevant name of the connection like **Confluence_Connection**. 
   * **URL:** Enter the base url (e.g. :literal:`https://sparkflows\.atlassian\.net`).
   * **Username:** Enter the specific username (e.g. :literal:`test@sparkflows\.io`).
   * **Token:** Enter the required API token.
   * **Description:** Enter a relevant description. It is optional.


#. Once this connection is configured and verified, it will display a '**Successfully Connected**' message, as shown below. Then click on **Save** button.
  
   .. figure:: ../../../_assets/connections/added-confluence.png
      :alt: connection
      :width: 60%














































