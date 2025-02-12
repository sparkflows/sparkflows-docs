Pinecone Vector Database
=======================

Pinecone is a managed vector database designed for fast and scalable similarity search. It provides efficient storage, indexing, and querying of high-dimensional vector embeddings, making it a great choice for AI-driven applications like semantic search, recommendation systems, and anomaly detection.

Sparkflows Features with Pinecone
---------------------------------

Fire Insights integrates with Pinecone to accelerate generative AI workflows and manages high-dimensional data effortlessly. Fire Insights handles NLP embeddings, computer vision outputs, and recommendation models with enterprise-grade scalability.

- Real-time Retrieval
- Semantic Search
- Anomaly Detection
- Hyper-personalized Recommendations


Setting Up Pinecone
-------------------

To set up and use Pinecone in your project, follow the steps below:

**Step 1 : Installing Dependencies**
++++++++++++++++++++++++++++++++++++

Install the required libraries using pip:

    .. code-block:: bash

        !pip install pinecone langchain langchain_pinecone langchain-openai langchain-community pypdf python-dotenv


**Step 2 : Install the Pinecone Client**

   Ensure you have Python installed, then install the Pinecone client using pip:

   .. code-block:: bash

      pip install pinecone-client

2. **Create a Pinecone Account**

   Sign up at `Pinecone <https://www.pinecone.io/>`_ and retrieve your API key from the dashboard.

3. **Initialize Pinecone**

   Set up your Pinecone environment using the API key:

   .. code-block:: python

      import pinecone
      
      pinecone.init(api_key="your-api-key", environment="us-west1-gcp")

4. **Create a Vector Index**

   Create an index to store your vector embeddings:

   .. code-block:: python

      pinecone.create_index("example-index", dimension=128, metric="cosine")

5. **Insert and Query Vectors**

   Insert vectors into your index:

   .. code-block:: python

      index = pinecone.Index("example-index")
      
      vectors = [("id1", [0.1, 0.2, 0.3, ...]), ("id2", [0.4, 0.5, 0.6, ...])]
      index.upsert(vectors)

   Query the nearest vectors:

   .. code-block:: python

      query_result = index.query([0.1, 0.2, 0.3, ...], top_k=5, include_metadata=True)
      print(query_result)

6. **Delete the Index (If Needed)**

   Remove an index when it's no longer required:

   .. code-block:: python

      pinecone.delete_index("example-index")

Conclusion
----------

Fire Insights along with Pinecone provides a seamless way to integrate vector search into AI applications with minimal setup and high efficiency. Whether for recommendations, search, or AI-driven insights, it simplifies vector database management for scalable and real-time querying.

