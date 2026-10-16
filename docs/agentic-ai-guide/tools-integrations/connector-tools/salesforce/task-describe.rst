:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Task</p>

Describe task fields
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Task</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_task_describe</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every field on the Task object, one row per field with its API name, label, type, length and whether it can be blank or updated. Use it to learn the org's exact field names, custom \_\_c fields included, before a create, update or query.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **describe** in the **Task** row, then click **Add to agent**.

The agent now sees ``salesforce_task_describe`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **Describe task fields** every time a flow reaches it, without the agent deciding, use the :doc:`Describe task fields App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/task-describe>`.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-get.html">Get a task</a><a href="task-getmany.html">List tasks</a><a href="task-create.html">Create a task</a><a href="task-update.html">Update a task</a><a href="task-delete.html">Delete a task</a></div>
