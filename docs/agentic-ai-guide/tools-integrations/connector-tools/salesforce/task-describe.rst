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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every field on the Task object, one row per field with its API name, label, type, length and whether it can be blank or updated. Use it to learn the org's exact field names, custom \_\_c fields included, before a create, update or query.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.

Parameters
----------

This tool takes no parameters.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **describe** in the **Task** row. The model sees it as ``salesforce_task_describe``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Describe task fields**, and fill in the inputs above. It runs every time the flow reaches it.

Other Task tools
----------------

.. raw:: html

   <div class="tool-related"><a href="task-get.html">Get a task</a><a href="task-getmany.html">List tasks</a><a href="task-create.html">Create a task</a><a href="task-update.html">Update a task</a><a href="task-delete.html">Delete a task</a></div>
