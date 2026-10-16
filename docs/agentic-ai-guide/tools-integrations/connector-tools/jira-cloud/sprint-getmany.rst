:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Sprint</p>

List a board's sprints
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Sprint</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_sprint_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the sprints of a Scrum board, each with its id, name, state, goal and dates, following Jira's paging up to the limit. Filter on state active to find the current sprint; the board id comes from Board getMany.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **list** in the **Sprint** row, then click **Add to agent**.

The agent now sees ``jira_cloud_sprint_getmany`` and calls it when a request needs it.

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
   * - ``boardId``
     - text
     - Yes
     - The Scrum board's numeric id, from Board getMany. Example: 12.
   * - ``state``
     - text
     - No
     - future, active or closed, or several comma-separated such as active,future; blank returns every sprint.
   * - ``limit``
     - whole number
     - No
     - How many sprints at most. Default: 50.

Need it on every run?
---------------------

To run **List a board's sprints** every time a flow reaches it, without the agent deciding, use the :doc:`List a board's sprints App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/sprint-getmany>`.

Other Sprint tools
------------------

.. raw:: html

   <div class="tool-related"><a href="sprint-get.html">Get a sprint</a></div>
