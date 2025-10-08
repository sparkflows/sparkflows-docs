OpenAI Connection
============
This connection can be created to interact with OpenAI APIs. The analytical apps and nodes can make use of the connection.

Fill in the information as shown below. Most of the fields are self-explanatory and can be populated with values that you like.

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



   .. figure:: ../../../_assets/installation/connection/gen-ai/open-ai1.png
      :alt: connection
      :width: 40%    

After entering the details, click the Test Connection button to verify the connection.
