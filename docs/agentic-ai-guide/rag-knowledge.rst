RAG & Knowledge
=============

Retrieval-augmented generation (RAG) grounds AI responses in enterprise information rather than relying only on a model's general knowledge. Sparkflows can combine document and data processing, embeddings, vector retrieval, workflow logic, and LLM generation within a single visual flow.

A typical RAG process ingests enterprise content, prepares and chunks it, creates embeddings, stores or indexes the resulting vectors, retrieves relevant context for a user request, and supplies that context to an LLM or agent. Metadata and other business rules can be used to narrow retrieval to appropriate information.

RAG can be used directly in a conversational application or exposed as a knowledge capability to a larger agentic workflow. Sparkflows can also combine structured and unstructured sources so an agent can work across documents and enterprise data within the same business process.

Start Here
-----------------

Start by identifying the authoritative knowledge sources and how frequently they change. Build the ingestion and indexing workflow first, then create the retrieval flow and validate the context returned for representative questions before connecting it to an agent.

For production use, consider source permissions, document updates, metadata, retrieval quality, and traceability of the context used to generate each response.

Documentation Topics
-----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - RAG Overview
     - Understand retrieval-augmented generation in Sparkflows.
   * - RAG Architecture
     - Understand ingestion, indexing, retrieval, and generation components.
   * - Build a RAG Workflow
     - Create an end-to-end grounded AI workflow.
   * - Knowledge Sources
     - Connect documents, files, databases, and enterprise content.
   * - Document Ingestion & Processing
     - Load and prepare content for retrieval.
   * - Chunking & Embeddings
     - Create retrievable units and vector representations.
   * - Vector Databases
     - Connect and manage supported vector stores.
   * - Indexing
     - Create and update searchable indexes.
   * - Retrieval & Semantic Search
     - Retrieve relevant enterprise context.
   * - Metadata Filtering
     - Restrict retrieval using document and business metadata.
   * - Hybrid Search & Reranking
     - Improve retrieval where supported.
   * - Multi-RAG
     - Use multiple knowledge sources in one AI experience.
   * - Structured + Unstructured Retrieval
     - Combine database and document knowledge.
   * - RAG in Agents & Apps
     - Expose enterprise knowledge to agent workflows and applications.
   * - Review Retrieved Context
     - Inspect the context used to generate a response.
   * - Troubleshooting
     - Diagnose ingestion, indexing, and retrieval issues.
