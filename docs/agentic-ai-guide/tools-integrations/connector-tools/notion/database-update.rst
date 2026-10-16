:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Database</p>

Update a database
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Database</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes a database's title, description or columns and returns the updated database. Rows are changed with Page update instead.

Prerequisites
-------------

* **Connection:** Notion connection. See :doc:`the Notion prerequisites <../notion>`.
* The connection's account must be allowed to change this data in Notion.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - Description
   * - ``databaseId``
     - text
     - Yes
     - The database to change, from Search run or the database's URL. Example: d9824bdc-8445-4327-be8b-5b47500af6ce.
   * - ``title``
     - list of JSON object
     - No
     - The new title as Notion rich text. Example: [{"type": "text", "text": {"content": "Vendor tasks 2026"}}].
   * - ``description``
     - list of JSON object
     - No
     - The new description as Notion rich text. Example: [{"type": "text", "text": {"content": "Open vendor actions, one row each."}}].
   * - ``properties``
     - JSON object
     - No
     - Columns to change by name: a definition adds or changes one, {"name": "New name"} renames one and null removes one. Example: {"Owner": {"people": {}}, "Old column": null}.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Notion**, connect, and tick **update** in the **Database** row. The model sees it as ``notion_database_update``. Each call waits for human approval before it changes anything.

Other Database tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="database-get.html">Get a database</a><a href="database-query.html">Query a database</a><a href="database-create.html">Create a database</a></div>
