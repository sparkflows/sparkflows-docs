Pinecone Connection
=======================
This document provides a guide on establishing a Pinecone connection in Sparkflows.

Overview
++++++++++++

Pinecone is a managed vector database used for high-speed similarity search and retrieval-augmented generation (RAG) applications. It is often used in combination with embedding models (like those from Amazon Bedrock) to store and search vector representations of data (e.g., text, images, or other unstructured data).

It is commonly used in following AI applications:

• Semantic search (finding similar content based on meaning, not just keywords)
• RAG for LLMs (enhancing generative AI with external knowledge)
• Recommendation systems

Setting up Pinecone Connection
+++++++++++++++++++++++++++++

To create a pinecone connection, follow the steps below:

**Step 1 : Login to Fire Insights and Navigate to Add Connection Page**
----------------------------------------------------------------------------

#. Login to Fire Insights by entering your sign in credentials as an Admin. 
#. From the Dashboard page, navigate to **Administration -> Global/Group Connections**.
#. From the Connections page, click on **Add Connection** button and choose **Add Connection for All**. An 'Add Connection' page will open up as shown below:

   .. figure:: ../../../_assets/installation/connection/add-pinecone-connection1.png
      :alt: connection
      :width: 60%

**Step 2 : Configuring the Connection for Pinecone**
-----------------------------------------------------

#. Enter the general details for the connection, as shown below and click on **Next** button.


   .. figure:: ../../../_assets/installation/connection/add-pinecone-connection1.png
     :alt: connection
     :width: 60%

   * **Select Category:** Choose **Vector DB** in the category. It is used for vector databases like Pinecone, Faiss, etc.
   * **Connection Type:** Select **Pinecone** from the dropdown as the vector database provider.

   **GENERAL Tab**

    * **Connection Name:** Define the connection name as **Pinecone-API**.
    * **URL:** Enter the required url.


#. Now, enter the pinecone details for the connection and click on **Save** button.

   .. figure:: ../../../_assets/installation/connection/add-pinecone-connection2.png
     :alt: connection
     :width: 60%

     
   **PINECONE Tab**

     * **Pinecone API Key:** Enter the required key to authenticate with Pinecone. Obtain this from your Pinecone account.
     * **Index Name:** Enter the name of the index where your vector embeddings will be stored. Example: document-index.
     * **Index Namespace:** It is optional. It helps segment data within the same index. Example: document-namespace.
     * **Metric:** This is a similarity measure used for comparing vectors:

                      - cosine (most common for text embeddings)
                      - dotproduct
                      - euclidean





























