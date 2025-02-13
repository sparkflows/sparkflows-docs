Bedrock Connection
----------------------

This connection can be created to interact with Amazon Bedrock APIs. The analytical apps and nodes can make use of the connection.

Amazon Bedrock is a fully managed service from AWS that lets you build and scale generative AI applications using foundation models (FMs) from leading model providers, without having to manage infrastructure or train models from scratch.

To create a bedrock connection follow the steps below:

Step 1 : Login to Fire Insights and Navigate to Connections Page
+++++

#. Login to Fire Insights by entering your **login credentials** as admin.
#. Navigate to **Administration -> Global/Group Connections**. A Connections page will open up, as shown below.

   .. figure:: ../../../_assets/installation/connection/create_connections/connections_page.png
      :alt: create_connections
      :width: 60%

Step 2 : Adding Bedrock Connection
++++++

#. Click on **Add Connection** button from the connections page and choose **Add Connections For All**. An Add Connection page will open up , as shown below.

   .. figure:: ../../../_assets/installation/connection/create_connections/add_connection.png
      :alt: create_connections
      :width: 60%

Step 3 : Configuring the Bedrock Connection
++++++
  
To configure the connection, enter the details as shown below:

   .. figure:: ../../../_assets/installation/connection/create_connections/add_connection.png
        :alt: create_connections
        :width: 60%


  * **Category Selection:** Select the category as **GenAI** because Amazon Bedrock is a generative AI service.
  * **Connection Type:** Select **Bedrock** indicating that you are configuring a connection to Amazon Bedrock.
  * **General Tab**

    * **Connection Name:** Enter a custom name for this connection.
    * **Model ID:** It represents the specific model you intend to work with on Amazon Bedrock, such as Claude, Titan, etc.

Now, click on **Next** button to access **Bedrock** tab.

   .. figure:: ../../../_assets/installation/connection/create_connections/add_bedrock_connection.png
        :alt: create_connections
        :width: 60%
    
  * **Bedrock Tab**

    * **Service Name:** It is defaulted to "bedrock-runtime," referring to the runtime service for interacting with models hosted on Bedrock.
    * **Region Name:** It specifies the AWS region, e.g., us-east-1.
    * **AWS Access Key ID / Secret Access Key:** Credentials to authenticate and authorize access to AWS services.
    * **Bedrock Embedding Model:** It specifies an embedding model like amazon.titan-embed-text-v1, often used for text embeddings (e.g., similarity searches or feature extraction).
    * **Bedrock Chat Model:** It specifies a conversational model like anthropic.claude-3-5-haiku-20241022-v1:0, suitable for chat and natural language processing tasks.

Once this connection is configured and saved, it will enable applications or pipelines to leverage Amazon Bedrock models for tasks like text generation, embeddings, and more.
