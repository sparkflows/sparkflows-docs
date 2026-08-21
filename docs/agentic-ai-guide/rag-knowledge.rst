RAG & Knowledge
================

Retrieval-augmented generation (RAG) grounds AI responses in enterprise information rather than relying only on a model's general knowledge. Sparkflows can combine document and data processing, embeddings, vector retrieval, workflow logic, and LLM generation within a single visual flow.

A typical RAG process ingests enterprise content, prepares and chunks it, creates embeddings, stores or indexes the resulting vectors, retrieves relevant context for a user request, and supplies that context to an LLM or agent. Metadata and other business rules can be used to narrow retrieval to appropriate information.

RAG can be used directly in a conversational application or exposed as a knowledge capability to a larger agentic workflow. Sparkflows can also combine structured and unstructured sources so an agent can work across documents and enterprise data within the same business process.

Steps to Build a RAG & Knowledge Workflow
-----------------------------------------

Build a RAG and knowledge workflow by working through the following steps.

Step 1: Identify Knowledge Sources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Identify the authoritative documents, files, databases, and enterprise content required by the agent or application.

Step 2: Ingest & Process Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load and prepare enterprise content for retrieval.

Step 3: Chunk Content & Create Embeddings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create retrievable content units and generate vector representations for the knowledge sources.

Step 4: Configure Vector Storage & Indexing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Store or index the resulting vectors using the supported vector database or search capability.

Step 5: Configure Retrieval
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve relevant enterprise context for user requests using semantic search and configured retrieval logic.

Step 6: Apply Metadata & Business Filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Restrict retrieval using document metadata and applicable business rules.

Step 7: Combine Structured & Unstructured Knowledge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combine database information and document-based knowledge within the same AI experience or business process.

Step 8: Connect RAG to Agents & Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Expose enterprise knowledge to agent workflows, conversational applications, or other AI experiences.

Step 9: Review Retrieved Context
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inspect the context returned for representative questions and validate that the retrieved information is appropriate for generating responses.

Next Step
---------

Once the RAG workflow and retrieved context have been validated, connect the knowledge capability to the agent and evaluate its grounded responses.
