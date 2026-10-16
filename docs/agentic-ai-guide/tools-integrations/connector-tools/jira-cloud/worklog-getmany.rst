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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the time logged on an issue, each entry with its id, author, time spent, start time and note. Use it to review or total the work done on one issue.

Prerequisites
-------------

* **Connection:** Jira connection. See :doc:`the Jira Cloud prerequisites <../jira-cloud>`.

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
   * - ``startedAfter``
     - Started after
     - whole number
     - No
     - Only worklogs started at or after this moment, as Unix time in milliseconds. Example: 1790726400000.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **list** in the **Worklog** row. The model sees it as ``jira_cloud_worklog_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **List an issue's worklogs**, and fill in the inputs above. It runs every time the flow reaches it.

Other Worklog tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="worklog-create.html">Log work on an issue</a></div>
