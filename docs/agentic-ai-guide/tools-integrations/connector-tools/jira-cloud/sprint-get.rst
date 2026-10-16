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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one sprint by its id and returns its name, state (future, active or closed), goal, board and start, end and completion dates. Sprint ids come from Sprint getMany.

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
   * - ``sprintId``
     - Sprint id
     - text
     - Yes
     - The sprint's numeric id, from Sprint getMany. Example: 37.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **get** in the **Sprint** row. The model sees it as ``jira_cloud_sprint_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **Get a sprint**, and fill in the inputs above. It runs every time the flow reaches it.

Other Sprint tools
------------------

.. raw:: html

   <div class="tool-related"><a href="sprint-getmany.html">List a board&#x27;s sprints</a></div>
