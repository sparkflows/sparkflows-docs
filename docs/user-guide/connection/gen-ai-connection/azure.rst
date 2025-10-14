Azure OpenAI Connection
===============
This connection can be created to interact with Azure OpenAI APIs. The analytical apps and nodes can make use of the connection.

Sparkflows supports two authentication methods for Azure OpenAI connection : **API Key/Token** and **Client Credentials**.

Step 1: Login to Fire Insights and Navigate to Connections Page
+++++

#. Login to Fire Insights by entering your **login credentials** as admin.
#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

  .. figure:: ../../../_assets/installation/connection/gen-ai/connections-page.png
      :alt: create_connections
      :width: 60%

Step 2: Adding Azure OpenAI Connection
++++++

1. Click on **Add Connection** button from the connections page and choose **Add Connections For All**. 

2. Now select the Connection Category as **GenAI** and Connection Type as **AzureOpenAI**.


 .. figure:: ../../../_assets/installation/connection/gen-ai/add-azure-openai-connection.png
     :alt: create_connections
      :width: 60%

Step 3: Configuring the Azure OpenAI Connection
++++++

1. Fill in the information as shown below. Most of the fields are self-explanatory and can be populated with values that you like.

  The fields can be populated as below based on the endpoint of the OpenAI deployment in your Azure account. 
  
  The fields which correspond to the Azure OpenAI end points are:

**Authentication Type : Token**

 * **Connection name** – Connection name
 * **URL** – The base endpoint of your Azure OpenAI resource (e.g., ``https://<resource-name>.openai.azure.com``).  
 * **Token** – The API key or bearer token used for authenticating with Azure OpenAI.  
 * **Embeddings Endpoint URL** – The Azure OpenAI endpoint dedicated to embeddings requests (e.g., ``https://<resource-    name>.openai.azure.com/openai/deployments/<deployment-name>/embeddings``).
 * **Model Name** – The name of the model deployment created in Azure OpenAI Studio.  
 * **API Version** – The API version to be used when making requests (e.g., ``2025-01-01-preview``). 
 * **Max Tokens** – The maximum number of tokens allowed in the model’s response.
 * **Project Id** – The identifier of the project or resource group linked to your deployment.  
 * **Title** – Connection Title
 * **Description** – Connection Description

  .. figure:: ../../../_assets/installation/connection/gen-ai/azure-openai-add-token.png
     :alt: connection
     :width: 60%    
  


**Authentication Type : Client Credentials** 

  * **Connection name** – Connection name
  * **URL** – The base endpoint of your Azure OpenAI resource (e.g., ``https://<resource-name>.openai.azure.com``).  
  * **Embeddings Endpoint URL** – The Azure OpenAI endpoint dedicated to embeddings requests (e.g., ``https://<resource-    name>.openai.azure.com/openai/deployments/<deployment-name>/embeddings``).
  * **Model Name** – The name of the model deployment created in Azure OpenAI Studio.  
  * **API Version** – The API version to be used when making requests (e.g., ``2025-01-01-preview``).  
  * **Client Id** – The application (client) ID registered in Azure AD for OAuth2 authentication.  
  * **Client Secret** – The secret associated with the client ID, used for secure authentication.  
  * **Token End Point URL** – The Azure AD token endpoint used to fetch access tokens.  
  * **Scope** – The scope value required for authentication (commonly the Azure resource URI).  
  * **Project Id** – The identifier of the project or resource group linked to your deployment. 
  * **Title** – Connection Title
  * **Description** – Connection Description
  * **Max Tokens** – The maximum number of tokens allowed in the model’s response.

   .. figure:: ../../../_assets/installation/connection/gen-ai/azure-openai-add-credential.png
     :alt: connection
     :width: 60%    

  
After entering the details, click the **Test Connection** button to verify the connection.

The details of the above fields can be found by logging into Azure and looking at the OpenAI deployment as per the official documentation below: 

`Azure OpenAI Documentation <https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#completions>`_

 
