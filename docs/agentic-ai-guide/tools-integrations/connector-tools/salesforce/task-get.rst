:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Task</p>

Get a task
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Task</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one task by its Salesforce Id and returns all of its fields, custom fields included. Use it when the Id is known; to find tasks by name or another value use List tasks.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.

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
   * - ``taskId``
     - Task Id
     - text
     - Yes
     - The task's Salesforce Id, 15 or 18 characters starting 00T, for example 00TXX000003QrSt; List tasks returns it.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **get** in the **Task** row. The model sees it as ``salesforce_task_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Get a task**, and fill in the inputs above. It runs every time the flow reaches it.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-getmany.html">List tasks</a><a href="task-create.html">Create a task</a><a href="task-update.html">Update a task</a><a href="task-delete.html">Delete a task</a><a href="task-describe.html">Describe task fields</a></div>
