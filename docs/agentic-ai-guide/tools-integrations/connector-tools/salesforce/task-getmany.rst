:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Task</p>

List tasks
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Task</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_task_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries tasks with an optional SOQL condition and returns up to limit rows. Only standard fields come back unless fields names them, so list custom (\_\_c) and relationship fields such as Who.Name explicitly. Use Run a SOQL query for aggregates, subqueries or several objects at once.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **list** in the **Task** row, then click **Add to agent**.

The agent now sees ``salesforce_task_getmany`` and calls it when a request needs it.

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
   * - ``where``
     - text
     - No
     - A SOQL condition without the word WHERE, such as IsClosed = false AND ActivityDate <= TODAY, with text in single quotes and dates unquoted; it may end with ORDER BY but not LIMIT, and blank returns every task up to the limit.
   * - ``fields``
     - list of text
     - No
     - Field API names to return, such as ["Id", "Subject", "Status", "ActivityDate", "Who.Name"]; blank returns the standard fields only.
   * - ``limit``
     - whole number
     - No
     - How many tasks at most. Example: 50. Default: 50.

Need it on every run?
---------------------

To run **List tasks** every time a flow reaches it, without the agent deciding, use the :doc:`List tasks App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/task-getmany>`.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-get.html">Get a task</a><a href="task-create.html">Create a task</a><a href="task-update.html">Update a task</a><a href="task-delete.html">Delete a task</a><a href="task-describe.html">Describe task fields</a></div>
