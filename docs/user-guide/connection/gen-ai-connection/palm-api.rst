Vertex Palm API Connection
============
This connection can be created to interact with Vertex Palm APIs. The analytical apps and nodes can make use of the connection.

To create a VertexPalmAPI connection follow the steps below:

Step 1: Login to Fire Insights and Navigate to Connections Page
+++++

#. Login to Fire Insights by entering your **login credentials** as admin.
#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

  .. figure:: ../../../_assets/installation/connection/gen-ai/connections-page.png
      :alt: create_connections
      :width: 60%

Step 2: Adding VertexPalmAPI Connection
++++++

1. Click on **Add Connection** button from the connections page and choose **Add Connections For All**. 

2. Now select the Connection Category as **GenAI** and Connection Type as **VertexPalmAPI**.


 .. figure:: ../../../_assets/installation/connection/gen-ai/add-palm-api.png
     :alt: create_connections
      :width: 60%

Step 3: Configuring the VertexPalmAPI Connection
++++++

1. Fill in the information as shown below. Most of the fields are self-explanatory and can be populated with values that you like.

 * **Connection Name :** Enter a unique name for this connection.

 * **Token :** This is the google cloud token which you can generate by logging into your google cloud account.

 * **Host URL :** This is the Vertex Palm API endpoint URL containing Project ID and Model Name :

   `https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/${MODEL_ID}:predict`

      .. figure:: ../../../_assets/installation/connection/gen-ai/configure-palm-api.png
         :alt: connection
         :width: 60%    

2. Once you have entered the connection details, click on **Test Connection** button to test the connection. If the connection is successful, click on **Save** button to save the connection.

   Now, you are ready to start using the Connection in apps and nodes.
