:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Worklog</p>

List an issue's worklogs
========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Worklog</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_worklog_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the time logged on an issue, each entry with its id, author, time spent, start time and note. Use it to review or total the work done on one issue.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **list** in the **Worklog** row, then click **Add to agent**.

The agent now sees ``jira_cloud_worklog_getmany`` and calls it when a request needs it.

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
   * - ``issueKey``
     - text
     - Yes
     - The issue key, for example FIN-12.
   * - ``startedAfter``
     - whole number
     - No
     - Only worklogs started at or after this moment, as Unix time in milliseconds. Example: 1790726400000.

Need it on every run?
---------------------

To run **List an issue's worklogs** every time a flow reaches it, without the agent deciding, use the :doc:`List an issue's worklogs App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/worklog-getmany>`.

Other Worklog tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="worklog-create.html">Log work on an issue</a></div>
