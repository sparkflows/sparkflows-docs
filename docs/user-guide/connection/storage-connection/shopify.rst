Shopify Connection
============

Shopify is a cloud-based e-commerce platform that allows businesses to create, manage, and scale online stores. It provides tools for product management, order processing, payments, and integrations with external systems.


Prerequisite
---------------

Before creating a Shopify Connection in Sparkflows, ensure that you have created a Shopify Admin API access token using a Custom App.

For detailed steps on **how to create the Shopify Admin API access token**, refer to the following document: :ref:`Shopify Token Creation<Shopify Token Creation>`.


To create a Shopify Connection in Sparkflows, follow the steps below:



Step 1 : Login to Sparkflows and Navigate to Connections Page
------------
#. Login to Sparkflows by entering your **login credentials** as **admin**.

#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

  .. figure:: ../../../_assets/connections/shopify-connections-page.png
      :alt: connection
      :width: 60%

Step 2 : Adding a Shopify Connection
-------------
#. Click on **Add Connection** button from the connections page and choose **Add Connections For All** as shown below. An Add Connection page will open up.

   .. figure:: ../../../_assets/connections/shopify-add-global-connections.png
      :alt: connection
      :width: 60%

#. Now, select the category as **Storage** and choose **Shopify** from the dropdown in the connection type. Then, enter a unique connection name.
   
   .. figure:: ../../../_assets/connections/shopify-select-connection.png
      :alt: connection
      :width: 60%

Step 3 : Configuring the Shopify Connection
--------------------

1. To configure this connection, enter the details as follows and click on **Test Connection** button to validate. 

 * **Shop Name:** Enter your shop name (E.g. sparkflows-dev.myshopify.com).

 * **Access Token:** Enter the Shopify Admin API access token generated from your Shopify store (E.g. shpat_xxxxxxxxxxxx).

  .. figure:: ../../../_assets/connections/shopify-connection-config.PNG
      :alt: connection
      :width: 60%

2. If the connection is successful, click **Save** to save the connection.

   Now, you are ready to start using the Connection in Read Shopify node to run the workflows/pipelines.
  














