Vector Databases
================

Vector databases (Vector DBs) are specialized database systems designed to efficiently store, index, and query high-dimensional vectors. These vectors often represent complex data types such as images, audio, text embeddings, and other forms of unstructured data, making them ideal for tasks like similarity search, recommendation systems, and generative AI applications.

Key Features
------------

- **Efficient Indexing**: Uses HNSW, IVF, and PQ for quick retrieval.
- **Fast Search**: Employs cosine similarity, Euclidean distance, and dot product to find the most relevant results.
- **Scalability**: Handles billions of vectors with low latency.
- **AI Integration**: Works with deep learning models for embeddings.
- **ANN Support**: Enables rapid Approximate Nearest Neighbor (ANN) search of similar vectors even in large-scale datasets.

Use Cases
---------

- **Recommendations**: Matches user preferences with content.
- **Semantic Search**: Enhances search beyond keyword matching by understanding the meaning behind queries.
- **Anomaly Detection**: Identifies unusual patterns.
- **Generative AI**: Supports retrieval-augmented generation (RAG) by providing relevant context for LLMs.

For a step-by-step guide on setting up a vector database, check out our tutorial on Pinecone:


.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    :doc:`/user-guide/generative-ai/vector-db/pinecone`

    Pinecone Tutorial

    ---

    :doc:`/user-guide/generative-ai/vector-db/milvus`

    ---

    Milvus Tutorial

    
.. toctree::
   :hidden:

   pinecone.rst
   milvus.rst


