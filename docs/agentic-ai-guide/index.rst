Agentic AI Guide
================

Build, orchestrate, govern and deploy enterprise AI agents in Sparkflows -
agents that reason over your data, call your systems, run your workflows, and
pause for a human when the decision warrants it.

New here? Work through **Quick start** in order to build your first tool-using
agent. Then choose only the guides needed for your next task.

Quick start
-----------

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/concepts`

    How agents work in Sparkflows, the five words you need, and how to choose
    between Agent Studio and Agent Orchestration.

    ---

    :doc:`/agentic-ai-guide/connections`

    Step 1 - create the connection for your model-powered agent. A flow
    made only of fixed App Actions and data steps does not need a model.

    ---

    :doc:`/agentic-ai-guide/quickstart`

    Step 2 - build a working, tool-using agent in about ten minutes.

    ---

    :doc:`/agentic-ai-guide/chat`

    Step 3 - turn that agent into a chatbot your colleagues can use.

Where you build
---------------

Choose a starting point, then open the reference for the step you need.

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/agent-studio`

    **One agent, one form.** Every field on the Agent Studio screen, in the
    order it appears.

    ---

    :doc:`/agentic-ai-guide/multi-agent-orchestration`

    **A process on a canvas.** Several steps, branches and approvals wired
    together.

    ---

    :doc:`/agentic-ai-guide/agent-node`

    **One model-powered step.** Give it a clear task, choose text or JSON,
    and validate its answer before the flow changes another system.

    ---

    :doc:`/agentic-ai-guide/ai-assistant`

    **Describe it and let it build.** Workflows, agents and analytics apps from
    plain-English instructions.

Automate with apps and data
---------------------------

Choose how a run starts, inspect its data, and shape records with explicit
rules. The separate App Actions section covers connected-system reads and writes.

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/triggers`

    How a run starts - by hand, on a schedule, when something happens in an
    app, when a file arrives, or from another system.

    ---

    :doc:`/agentic-ai-guide/passing-data`

    See what reaches each step and use earlier values with a click.

    ---

    :doc:`/agentic-ai-guide/data-steps`

    Filter, Sort, Limit, Set Fields, Remove Duplicates, Summarize, Split Out,
    Merge and Loop Over Items.

    ---

    :doc:`/agentic-ai-guide/files`

    Read and write CSV, Excel, JSON, PDFs, images and zips, on disk or in the
    cloud.

    ---

    :doc:`/agentic-ai-guide/code-node`

    Your own logic in Python or JavaScript, with one-click translation.

App Actions: setup and reference
--------------------------------

Use this section independently of the tutorials. Start with the shared
read → map → test pattern, then open only the app family you need.

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/app-actions`

    Choose a fixed action, map its inputs, check its results and handle
    failures. No model decides whether the configured action runs.

    ---

    :doc:`/agentic-ai-guide/app-setup`

    Pick your app, set up its connection and verify one small read. Includes
    Google Workspace, Microsoft 365, business apps, databases and web search.

    ---

    :doc:`/agentic-ai-guide/database-connectors-setup`

    PostgreSQL, MySQL and SQL Server: connection setup, all eleven row/query
    actions, keys, results and safe retries.

    ---

    :doc:`/agentic-ai-guide/app-action-catalogue`

    Find an individual action, its required inputs and whether it reads or
    changes data. Keep this lookup handy; you do not need to read it in order.

Build a complete example
-------------------------

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/end-to-end-examples/index`

    Eight business tasks, one page per flow. Start with a manual test, connect
    the nodes, inspect the result, then add automation when it works.

Give agents something to do
---------------------------

Tools let an agent read information and take actions beyond generating an
answer. Choose only the capabilities your task needs.

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/tools-actions`

    The tool picker: connectors, built-in tools, and how to choose operations
    safely.

    ---

    :doc:`/agentic-ai-guide/workflows-as-tools`

    Let an agent run a saved workflow - the right home for exact, repeatable
    logic.

    ---

    :doc:`/agentic-ai-guide/mcp-servers`

    Connect a Model Context Protocol server and pick which of its tools the
    agent may use.

    ---

    :doc:`/agentic-ai-guide/rag-knowledge`

    Ground answers in your own documents with retrieval and vector databases.

Shape how agents behave
-----------------------

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/models-prompts`

    Model connections, generation settings, and writing instructions that hold
    up.

    ---

    :doc:`/agentic-ai-guide/skills`

    Reusable ``.md`` instruction files shared across agents in a project.

    ---

    :doc:`/agentic-ai-guide/context-agents-md`

    ``AGENTS.md`` - the standing context every agent should know.

    ---

    :doc:`/agentic-ai-guide/security-guardrails`

    Guardrails, access control, and limiting what agents may reach.

Build real processes
--------------------

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/node-reference`

    Every node on the canvas, how to configure it, and what people get wrong.

    ---

    :doc:`/agentic-ai-guide/control-flow`

    Condition, Router and Guardrails - the nodes that decide where a run goes.

    ---

    :doc:`/agentic-ai-guide/human-in-the-loop`

    Human Approval and Human Input: pausing a run for a real decision.

Run and operate
---------------

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/evaluate-agents`

    Run agents, inspect traces, compare results, and judge whether they are
    good enough.

    ---

    :doc:`/agentic-ai-guide/deploy-agents`

    The ways an agent gets invoked once it works.

    ---

    :doc:`/agentic-ai-guide/schedule-agents`

    Run an agent on a timetable, and decide who hears about failures.

    ---

    :doc:`/agentic-ai-guide/monitor-govern`

    Runs, traces, logs, approvals and production behaviour.

For developers
--------------

.. panels::
    :container: container-lg pb-3

    :doc:`/agentic-ai-guide/developer-api`

    Run, resume and monitor agents from your own systems over the REST API.

.. toctree::
   :hidden:
   :caption: Quick start

   concepts.rst
   connections.rst
   quickstart.rst
   chat.rst

.. toctree::
   :hidden:
   :caption: Where you build

   agent-studio.rst
   multi-agent-orchestration.rst
   agent-node.rst
   ai-assistant.rst

.. toctree::
   :hidden:
   :caption: Automate with apps and data

   triggers.rst
   passing-data.rst
   data-steps.rst
   files.rst
   code-node.rst

.. toctree::
   :hidden:
   :caption: App Actions

   app-actions.rst

.. toctree::
   :hidden:
   :caption: Give agents tools and data

   tools-actions.rst
   workflows-as-tools.rst
   mcp-servers.rst
   rag-knowledge.rst

.. toctree::
   :hidden:
   :caption: Shape how agents behave

   models-prompts.rst
   skills.rst
   context-agents-md.rst
   security-guardrails.rst

.. toctree::
   :hidden:
   :caption: Build real processes

   node-reference.rst
   control-flow.rst
   human-in-the-loop.rst

.. toctree::
   :hidden:
   :caption: Run and operate

   evaluate-agents.rst
   deploy-agents.rst
   schedule-agents.rst
   monitor-govern.rst

.. toctree::
   :hidden:
   :caption: For developers

   developer-api.rst
