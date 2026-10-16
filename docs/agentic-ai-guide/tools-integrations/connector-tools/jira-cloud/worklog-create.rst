:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Worklog</p>

Log work on an issue
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Worklog</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_worklog_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Logs time spent on an issue and returns the new worklog with its id. The time uses Jira's duration format, such as 2h 30m or 1d.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.
* The account behind the connection must be allowed to change this data in Jira Cloud.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **create** in the **Worklog** row, then click **Add to agent**.

The agent now sees ``jira_cloud_worklog_create`` and calls it when a request needs it.

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
   * - ``timeSpent``
     - text
     - Yes
     - The duration in Jira's format with w, d, h and m units, for example 2h 30m.
   * - ``started``
     - text
     - Yes
     - When the work started, as an ISO 8601 date and time; a date on its own means midnight UTC. Example: 2026-09-30T09:00:00+05:30.
   * - ``comment``
     - text
     - No
     - A note about the work done. Example: Paired on the SSO timeout fix..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Jira Cloud.

Need it on every run?
---------------------

To run **Log work on an issue** every time a flow reaches it, without the agent deciding, use the :doc:`Log work on an issue App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/worklog-create>`.

Other Worklog tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="worklog-getmany.html">List an issue&#x27;s worklogs</a></div>
