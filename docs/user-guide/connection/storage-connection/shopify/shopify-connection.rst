Creating Shopify Connection
============

Shopify is a cloud-based e-commerce platform that allows businesses to create, manage, and scale online stores. It provides tools for product management, order processing, payments, and integrations with external systems.


Prerequisite
---------------

Before creating a Shopify connection in Sparkflows, ensure the following:

* A **Shopify Admin API Access Token** has been generated using a **Custom App**, if using **Token Authentication**.
* A **Client Id** and **Client Secret** have been generated while creating the app in the Shopify store, if using **Client Credentials Authentication**.

For detailed steps on **how to generate the token and client credentials**, refer to the following document: :ref:`Creating Shopify Token<Installing Shopify App and Creating Token>`

To create a Shopify Connection in Sparkflows, follow the steps below:


Step 1 : Login to Sparkflows and Navigate to Connections Page
------------
#. Login to Sparkflows by entering your **login credentials** as **admin**.

#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

   .. figure:: ../../../../_assets/connections/shopify-connections-page.png
      :alt: connection
      :width: 60%

Step 2 : Adding a Shopify Connection
-------------
#. Click on **Add Connection** button from the connections page and choose **Add Connections For All** as shown below. An Add Connection page will open up.

   .. figure:: ../../../../_assets/connections/shopify-add-global-connections.png
      :alt: connection
      :width: 60%

#. Now, select the category as **Storage** and choose **Shopify** from the dropdown in the connection type. 
   
   .. figure:: ../../../../_assets/connections/shopify-select-connection.png
      :alt: connection
      :width: 60%

Step 3 : Configuring the Shopify Connection
--------------------

1. To configure this connection, enter the details in the following fields. Sparkflows supports two authentication methods for Shopify connections: **Token Authentication** and **Client Credentials Authentication** 

   Select the appropriate Authentication Type and provide the required details.

   **Token Authentication**

   * **Group:** Select the group where the connection will be created.
   * **Connection Name:** Give a name of the Shopify connection.
   * **Shop URL:** Enter your shop url (E.g. sparkflows-dev.myshopify.com).
   * **Access Token:** Enter the Shopify Admin API access token generated from your Shopify store (E.g. shpat_xxxxxxxxxxxx).
   * **Title (Optional):** Give a unique title for the connection.
   * **Description (Optional):** Provide a description for the connection.

   .. figure:: ../../../../_assets/connections/shopify-connection-config-1.png
       :alt: connection
       :width: 60%

   **Client Credentials Authentication**

   * **Group:** Select the group where the connection will be created.
   * **Connection Name:** Give a name of the Shopify connection.
   * **Shop Url:** Enter the Shopify store URL.
   * **Client Id:** Enter the client Id generated when creating the Shopify app.
   * **Client Secret:** Enter the client secret associated with the Shopify app.
   * **Title (Optional):** Give a unique title for the connection.
   * **Description (Optional):** Provide a description for the connection.

   .. figure:: ../../../../_assets/connections/shopify-connection-config-2.png
       :alt: connection
       :width: 60%

2. Next, click on **Test Connection** button to validate. If the connection is successful, click **Save** to save the connection.

   Now, you are ready to start using the Connection in Read Shopify node to run the workflows/pipelines.
  














