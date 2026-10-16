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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_task_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a task (a to-do or a logged activity) from the given fields and returns its new Id. Link it to a contact or lead with whoId and to an account, opportunity or case with whatId.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **create** in the **Task** row, then click **Add to agent**.

The agent now sees ``salesforce_task_create`` and calls it when a request needs it.

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
   * - ``subject``
     - text
     - No
     - What the task is. Example: Call back about the renewal.
   * - ``activityDate``
     - text
     - No
     - The due date as YYYY-MM-DD. Example: 2026-10-03.
   * - ``status``
     - text
     - No
     - The task status from the org's picklist, for example Not Started, In Progress or Completed.
   * - ``priority``
     - text
     - No
     - The task priority, for example High, Normal or Low.
   * - ``whoId``
     - text
     - No
     - The contact (an Id starting 003) or lead (00Q) the task is about. Example: 003XX000004TmiQ.
   * - ``whatId``
     - text
     - No
     - The account, opportunity, case or other record the task relates to. Example: 006XX000002kLmN.
   * - ``ownerId``
     - text
     - No
     - The Id of the user the task is assigned to, starting 005. Example: 005XX000001Sv6e.
   * - ``description``
     - text
     - No
     - Notes on the task. Example: Ask whether they want the three-year term..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create a task** every time a flow reaches it, without the agent deciding, use the :doc:`Create a task App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/task-create>`.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-get.html">Get a task</a><a href="task-getmany.html">List tasks</a><a href="task-update.html">Update a task</a><a href="task-delete.html">Delete a task</a><a href="task-describe.html">Describe task fields</a></div>
