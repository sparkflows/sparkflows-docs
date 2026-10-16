:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Task</p>

Update a task
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Task</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_task_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes the given fields on an existing task and leaves the others as they are; returns the task's Id. The task is named by its Salesforce Id, which List tasks returns.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **update** in the **Task** row, then click **Add to agent**.

The agent now sees ``salesforce_task_update`` and calls it when a request needs it.

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
   * - ``taskId``
     - text
     - Yes
     - The Salesforce Id of the task to change, starting 00T, for example 00TXX000003QrSt; List tasks returns it.
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

To run **Update a task** every time a flow reaches it, without the agent deciding, use the :doc:`Update a task App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/task-update>`.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-get.html">Get a task</a><a href="task-getmany.html">List tasks</a><a href="task-create.html">Create a task</a><a href="task-delete.html">Delete a task</a><a href="task-describe.html">Describe task fields</a></div>
