:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Workflow</p>

Run a workflow
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Workflow</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>github_workflow_dispatch</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Starts a workflow that has a workflow\_dispatch trigger, on a branch or tag, with optional inputs. GitHub answers with no content, so the new run shows up in Workflow listRuns a few seconds later.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.
* The account behind the connection must be allowed to change this data in GitHub.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **dispatch** in the **Workflow** row, then click **Add to agent**.

The agent now sees ``github_workflow_dispatch`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``repository``
     - text
     - Yes
     - The repository as owner/name, for example octocat/hello-world.
   * - ``workflow``
     - text
     - Yes
     - The workflow's file name, for example deploy.yml, or its numeric id from Workflow getMany.
   * - ``ref``
     - text
     - Yes
     - The branch or tag to run the workflow on. Example: main.
   * - ``inputs``
     - JSON object
     - No
     - Values for the workflow's inputs, as a JSON object of input name to value. Example: {"environment": "staging"}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in GitHub.

Other Workflow tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="workflow-getmany.html">List workflows</a><a href="workflow-listruns.html">List workflow runs</a></div>
