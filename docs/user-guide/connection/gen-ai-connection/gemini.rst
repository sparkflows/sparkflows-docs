Gemini Connection
====
This connection can be created to interact with Gemini APIs. The analytical apps and nodes can make use of the connection.

To create a gemini connection follow the steps below:

Step 1: Login to Fire Insights and Navigate to Connections Page
+++++

#. Login to Fire Insights by entering your **login credentials** as admin.
#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

  .. figure:: ../../../_assets/installation/connection/gen-ai/connections-page.png
      :alt: create_connections
      :width: 60%


Step 2: Adding Gemini Connection
++++++

1. Click on **Add Connection** button from the connections page and choose **Add Connections For All**. 

2. Now select the Connection Category as **GenAI** and Connection Type as **Gemini**.


 .. figure:: ../../../_assets/installation/connection/gen-ai/add-gemini-connection.png
     :alt: create_connections
      :width: 60%

Step 3: Configuring the Gemini Connection
++++++
1. Fill in the information as shown below. Most of the fields are self-explanatory and can be populated with values that you like.

  .. figure:: ../../../_assets/installation/connection/gen-ai/configure-gemini-connection.png
    :alt: create_connections
    :width: 60%

  * **Connection Name:** Enter a custom name for this connection.
  * **Host URL:** Enter the base address of the Gemini API service (e.g., https://generativelanguage.googleapis.com).
  * **Google Api Key:** Enter unique authentication token from Google Cloud that lets you access the API.
  * **Gemini Chat Model:** Enter the specific Gemini model you want to use for generating responses (e.g., "gemini-1.5-flash" or "gemini-1.5-pro").
  * **Max Tokens:** The maximum number of output tokens supported by that particular gemini model (e.g. Output token limit for gemini-2.5-pro is 65,536).


2. Once you have entered the connection details, click on **Test Connection** button to test the connection. If the connection is successful, click on **Save** button to save the connection.

   Now, you are ready to start using the Connection in apps and nodes.














