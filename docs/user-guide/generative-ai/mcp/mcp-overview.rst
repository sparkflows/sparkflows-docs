========================
MCP Overview and Design
========================

What is MCP?
------------

MCP (Modular Command Processor) is a lightweight client-server framework designed to process structured user queries, route them through a chain of tools and language model decisions, and return informative responses. It enables orchestration of LLM calls, tool execution, and retrieval-augmented generation (RAG) seamlessly within a modular architecture.

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/mcp/mcp1.png
     :alt: data-quality-userguide
     :width: 65%


Core Components
---------------

- **MCPClient**: Handles user requests, logging, and communication with the LLM and tools.
- **Tool Plugins**: Modular Python tools invoked by the LLM based on user input (e.g., `get_docs`, `search_google`).
- **LLM Interface**: Responsible for interpreting user queries, selecting tools, and generating final responses.
- **Retriever Layer**: Uses APIs (like Serper, LangChain, etc.) to fetch relevant data/documentation.
- **Response Engine**: Assembles tool outputs and LLM completions into structured chat responses.

Workflow
--------

1. **User Query Sent** via POST to ``/query``
2. **LLM Processes Input** and may invoke tools
3. **Tools Run in Background** (e.g., documentation retrieval)
4. **Tool Results Returned** to LLM
5. **LLM Generates Final Reply**, which is returned to the user

  .. figure:: ../../../_assets/user-guide/machine-learning/generative-ai/mcp/mcp2.png
     :alt: data-quality-userguide
     :width: 65%                                  

Example
-------

A typical log sequence might look like:

.. code-block:: bash

    MCPClient - INFO - Processing query: how do I connect langchain and chromadb?
    MCPClient - INFO - Calling tool get_docs with args {...}
    MCPClient - INFO - Tool get_docs result: ...
    MCPClient - INFO - Calling LLM

This shows an end-to-end execution with a tool call and response synthesis.
