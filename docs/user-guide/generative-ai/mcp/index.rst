Model Context Protocol (MCP)
=================

The Model Context Protocol (MCP) is a lightweight client-server framework that connects language models and tools in a structured, programmable workflow. It enables dynamic tool invocation, document retrieval, and response synthesis via a plugin architecture.

Key Highlights
--------------

- **Tool-Oriented Design:** Integrates Python functions directly callable by LLMs.
- **Extensible:** Add your own prompt templates, resource definitions, and tools.
- **Modular Backend:** Uses components like FastAPI, LangChain, and ChromaDB.
- **Reproducible Environment:** Compatible with `uv` for faster, lock-based dependency management.

.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    :doc:`/user-guide/generative-ai/mcp/mcp-overview`

    MCP Overview

    ---

    :doc:`/user-guide/generative-ai/mcp/mcp-installation`

    MCP Installation and Setup

.. toctree::
   :hidden:

   mcp-overview.rst
   mcp-installation.rst
