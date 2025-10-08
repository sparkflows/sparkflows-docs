Vertex Palm API Connection
============
This connection can be created to interact with Vertex Palm APIs. The analytical apps and nodes can make use of the connection.

Fill in the information as shown below. Most of the fields are self-explanatory and can be populated with values that you like.

The fields which corresponds to the Vertex Palm API end points are:

 * **Connection Name :** Enter a unique name for this connection.

 * **Token :** This is the google cloud token which you can generate by logging into your google cloud account.

 * **Host URL :** This is the Vertex Palm API endpoint URL containing Project ID and Model Name :

   `https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/${MODEL_ID}:predict`

      .. figure:: ../../../_assets/installation/connection/gen-ai/palm-api1.png
         :alt: connection
         :width: 40%    

After entering the details, click the Test Connection button to verify the connection.
