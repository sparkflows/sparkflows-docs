OpenAI Connection
============
This connection can be created to interact with OpenAI APIs. The analytical apps and nodes can make use of the connection.

To create a OpenAI connection follow the steps below:

Step 1: Login to Sparkflows and Navigate to Connections Page
+++++

#. Login to Sparkflows by entering your **login credentials** as admin.
#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

  .. figure:: ../../../_assets/installation/connection/gen-ai/connections-page.png
      :alt: create_connections
      :width: 60%


Step 2: Adding OpenAI Connection
++++++

1. Click on **Add Connection** button from the connections page and choose **Add Connections For All**. 

2. Now select the Connection Category as **GenAI** and Connection Type as **OpenAI**.


 .. figure:: ../../../_assets/installation/connection/gen-ai/add-openai-connection.png
     :alt: create_connections
      :width: 60%

Step 3: Configuring the OpenAI Connection
++++++

1. Fill in the information as shown below. Most of the fields are self-explanatory and can be populated with values that you like.

The fields which corresponds to the OpenAI end points are:

 * **Api Key :**  This is the OpenAI token which you can generate by logging into your OpenAI account and following the steps as listed here:

   `Generate OpenAI Access Token <https://platform.openai.com/api-keys>`_

 * **URL :**  This is the OpenAI endpoint URL which can be found in the official docs here: `OpenAI Endpoint URL <https://platform.openai.com/docs/api-reference/chat/create>`_
 * **Chat Model :** The chat model (e.g., gpt-4.1) used for generating responses.
 * **Embedding Model :** The embedding model used to convert text into vector representations.
 * **Embedding Url :** The API endpoint for accessing the embedding service.
 * **Max Retries :** Maximum number of retry attempts if a request fails.
 * **Embedding Context Length :** The maximum input size supported by the embedding model.
 * **Max Tokens :** Maximun tokens for the response
 * **Chat ID :** Identifier for the specific chat session with OpenAI
 * **Assistant Id :** Unique identifier for the assistant instance handling requests



   .. figure:: ../../../_assets/installation/connection/gen-ai/configure-openai-connection.png
      :alt: connection
      :width: 60%    

2. Once you have entered the connection details, click on **Test Connection** button to test the connection. If the connection is successful, click on **Save** button to save the connection.

   Now, you are ready to start using the Connection in apps and nodes.
