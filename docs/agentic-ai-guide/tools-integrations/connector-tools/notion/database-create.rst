:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Database</p>

Create a database
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

   Creates a database under a page with the columns given and returns it with its id. Page create with that id as databaseId then adds rows.

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
   * - ``parentPageId``
     - text
     - Yes
     - The page the database goes under. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.
   * - ``properties``
     - JSON object
     - Yes
     - The columns as Notion property definitions keyed by name, with exactly one title property. Example: {"Name": {"title": {}}, "Status": {"select": {"options": [{"name": "Open"}, {"name": "Done"}]}}, "Due": {"date": {}}}.
   * - ``title``
     - list of JSON object
     - No
     - The database title as Notion rich text. Example: [{"type": "text", "text": {"content": "Vendor tasks"}}].
   * - ``isInline``
     - true or false
     - No
     - true shows the database inside the parent page rather than as a page of its own.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Notion**, connect, and tick **create** in the **Database** row. The model sees it as ``notion_database_create``. Each call waits for human approval before it changes anything.

Other Database tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="database-get.html">Get a database</a><a href="database-query.html">Query a database</a><a href="database-update.html">Update a database</a></div>
