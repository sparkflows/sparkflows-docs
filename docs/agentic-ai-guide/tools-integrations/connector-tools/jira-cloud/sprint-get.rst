:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Sprint</p>

Get a sprint
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Sprint</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_sprint_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one sprint by its id and returns its name, state (future, active or closed), goal, board and start, end and completion dates. Sprint ids come from Sprint getMany.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **get** in the **Sprint** row, then click **Add to agent**.

The agent now sees ``jira_cloud_sprint_get`` and calls it when a request needs it.

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
   * - ``sprintId``
     - text
     - Yes
     - The sprint's numeric id, from Sprint getMany. Example: 37.

Need it on every run?
---------------------

To run **Get a sprint** every time a flow reaches it, without the agent deciding, use the :doc:`Get a sprint App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/sprint-get>`.

Other Sprint tools
------------------

.. raw:: html

   <div class="tool-related"><a href="sprint-getmany.html">List a board&#x27;s sprints</a></div>
