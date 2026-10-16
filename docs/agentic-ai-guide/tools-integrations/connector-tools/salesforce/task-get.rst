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
     <div><dt>Tool name</dt><dd><code>salesforce_task_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one task by its Salesforce Id and returns all of its fields, custom fields included. Use it when the Id is known; to find tasks by name or another value use List tasks.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **get** in the **Task** row, then click **Add to agent**.

The agent now sees ``salesforce_task_get`` and calls it when a request needs it.

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
     - The task's Salesforce Id, 15 or 18 characters starting 00T, for example 00TXX000003QrSt; List tasks returns it.

Need it on every run?
---------------------

To run **Get a task** every time a flow reaches it, without the agent deciding, use the :doc:`Get a task App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/task-get>`.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-getmany.html">List tasks</a><a href="task-create.html">Create a task</a><a href="task-update.html">Update a task</a><a href="task-delete.html">Delete a task</a><a href="task-describe.html">Describe task fields</a></div>
