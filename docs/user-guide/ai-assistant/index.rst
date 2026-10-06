AI Assistant
============

AI Assistant helps you build and refine Sparkflows workflows, pipelines,
projects, and node queries using natural language. Describe what you want;
AI Assistant generates the result for you to preview, confirm, and use.

New here? Work through the sections below in order. If you already have an
AI Assistant configured, jump to **Where to use it**.

What it is
----------

Use AI Assistant when you want to:

* Create or update a **workflow** or **pipeline** from a prompt
* Generate **node-level** queries with natural language
* Spin up a **project** (with datasets and workflows) from a description
* Optionally call external tools through an **MCP** connection

For a product overview of building workflows, agents, and apps from prompts,
see :doc:`/agentic-ai-guide/ai-assistant`. This User Guide section covers
administration, designer usage (including pipelines, nodes, and projects),
MCP, feedback, and prompt examples. It is separate from the
:doc:`/user-guide/chatbot/index`.

Prerequisites
-------------

Before you start:

1. Enable **module.enableCopilot** in configuration.
2. Configure an active **Gen AI connection** (for example OpenAI, Azure
   OpenAI, or Bedrock).

Full setup steps are in the create guide below.

Create an AI Assistant
----------------------

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/ai-assistant/copilot`

    Create and manage an AI Assistant under Administration. Choose a Gen AI
    connection and, optionally, MCP connections.

Where to use it
---------------

After an AI Assistant exists, open it from the designer or project screens
that match your task.

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/ai-assistant/copilot-wf`

    Generate and preview workflows in the Workflow Designer. Includes sample
    prompts, activities, and history.

    ---

    :doc:`/user-guide/ai-assistant/copilot-pipeline`

    Generate and preview pipelines in the Pipeline Designer. Same assistant
    features as workflows, for pipeline JSON and canvas.

    ---

    :doc:`/user-guide/ai-assistant/copilot-nodes`

    Write or refine node-level Natural Language Queries (NLQ) from a node
    dialog.

    ---

    :doc:`/user-guide/ai-assistant/copilot-project`

    Create a project from a natural-language description, including datasets
    and workflows.

MCP (optional)
--------------

Connect Model Context Protocol (MCP) tools so AI Assistant can inspect data
and return structured tool responses while generating nodes.

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/ai-assistant/mcp-copilot`

    Create an MCP connection, attach it to an AI Assistant, and run sample
    queries from the designer.

Feedback and reports
--------------------

Capture quality signal on assistant responses and route report emails to
admins.

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/ai-assistant/copilot-features`

    Submit feedback, report issues, review them in Administration, and
    configure report email recipients.

Prompt examples
---------------

Use these galleries for ready-made prompts you can copy and adapt.

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/ai-assistant/copilot-workflow-examples/index`

    Create workflows, update existing ones, and add nodes with example
    prompts.

    ---

    :doc:`/user-guide/ai-assistant/copilot-pipeline-examples/index`

    Create and update pipelines with example prompts.


.. toctree::
   :hidden:

   copilot.rst
   copilot-wf.rst
   copilot-pipeline.rst
   copilot-nodes.rst
   copilot-project.rst
   mcp-copilot.rst
   copilot-features.rst
   copilot-workflow-examples/index
   copilot-pipeline-examples/index
