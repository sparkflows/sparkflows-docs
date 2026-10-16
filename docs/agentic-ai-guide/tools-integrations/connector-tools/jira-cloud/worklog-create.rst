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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Logs time spent on an issue and returns the new worklog with its id. The time uses Jira's duration format, such as 2h 30m or 1d.

Prerequisites
-------------

* **Connection:** Jira connection. See :doc:`the Jira Cloud prerequisites <../jira-cloud>`.
* The connection's account must be allowed to change this data in Jira Cloud.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``issueKey``
     - Issue key
     - text
     - Yes
     - The issue key, for example FIN-12.
   * - ``timeSpent``
     - Time spent
     - text
     - Yes
     - The duration in Jira's format with w, d, h and m units, for example 2h 30m.
   * - ``started``
     - Started
     - text
     - Yes
     - When the work started, as an ISO 8601 date and time; a date on its own means midnight UTC. Example: 2026-09-30T09:00:00+05:30.
   * - ``comment``
     - Note
     - text
     - No
     - A note about the work done. Example: Paired on the SSO timeout fix..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **create** in the **Worklog** row. The model sees it as ``jira_cloud_worklog_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **Log work on an issue**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Worklog tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="worklog-getmany.html">List an issue&#x27;s worklogs</a></div>
