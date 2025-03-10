Vertex Palm API Connection
============
This connection can be created to interact with Vertex Palm APIs. The analytical apps and nodes can make use of the connection.

Fill in the information as shown below. Most of the fields are self-explanatory and can be populated with values that you like.

The two fields which corresponds to the Vertex Palm API end points are:

 * **Token :** 

   This is the google cloud token which you can generate by logging into your google cloud account.

 * **URL :** 

   This is the Vertex Palm API endpoint URL containing Project ID and Model Name :

   `https://us-central1-aiplatform.googleapis.com/v1/projects/${PROJECT_ID}/locations/us-central1/publishers/google/models/${MODEL_ID}:predict`

      .. figure:: ../../../_assets/installation/connection/gen-ai/palm-api.png
         :alt: connection
         :width: 40%    
