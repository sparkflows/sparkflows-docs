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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries tasks with an optional SOQL condition and returns up to limit rows. Only standard fields come back unless fields names them, so list custom (\_\_c) and relationship fields such as Who.Name explicitly. Use Run a SOQL query for aggregates, subqueries or several objects at once.

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
   * - ``where``
     - Where
     - text
     - No
     - A SOQL condition without the word WHERE, such as IsClosed = false AND ActivityDate <= TODAY, with text in single quotes and dates unquoted; it may end with ORDER BY but not LIMIT, and blank returns every task up to the limit.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Field API names to return, such as ["Id", "Subject", "Status", "ActivityDate", "Who.Name"]; blank returns the standard fields only.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many tasks at most. Example: 50. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **list** in the **Task** row. The model sees it as ``salesforce_task_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **List tasks**, and fill in the inputs above. It runs every time the flow reaches it.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-get.html">Get a task</a><a href="task-create.html">Create a task</a><a href="task-update.html">Update a task</a><a href="task-delete.html">Delete a task</a><a href="task-describe.html">Describe task fields</a></div>
