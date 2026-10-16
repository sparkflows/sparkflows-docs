:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Task</p>

Create a task
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Task</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a task (a to-do or a logged activity) from the given fields and returns its new Id. Link it to a contact or lead with whoId and to an account, opportunity or case with whatId.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.
* The connection's account must be allowed to change this data in Salesforce.

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
   * - ``subject``
     - Subject
     - text
     - No
     - What the task is. Example: Call back about the renewal.
   * - ``activityDate``
     - Due date
     - text
     - No
     - The due date as YYYY-MM-DD. Example: 2026-10-03.
   * - ``status``
     - Status
     - text
     - No
     - The task status from the org's picklist, for example Not Started, In Progress or Completed.
   * - ``priority``
     - Priority
     - text
     - No
     - The task priority, for example High, Normal or Low.
   * - ``whoId``
     - Contact or lead Id
     - text
     - No
     - The contact (an Id starting 003) or lead (00Q) the task is about. Example: 003XX000004TmiQ.
   * - ``whatId``
     - Related record Id
     - text
     - No
     - The account, opportunity, case or other record the task relates to. Example: 006XX000002kLmN.
   * - ``ownerId``
     - Assigned to
     - text
     - No
     - The Id of the user the task is assigned to, starting 005. Example: 005XX000001Sv6e.
   * - ``description``
     - Comments
     - text
     - No
     - Notes on the task. Example: Ask whether they want the three-year term..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **create** in the **Task** row. The model sees it as ``salesforce_task_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Create a task**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-get.html">Get a task</a><a href="task-getmany.html">List tasks</a><a href="task-update.html">Update a task</a><a href="task-delete.html">Delete a task</a><a href="task-describe.html">Describe task fields</a></div>
