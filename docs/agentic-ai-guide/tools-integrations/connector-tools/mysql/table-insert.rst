:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../mysql.html">MySQL</a> › Table</p>

Insert a row
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mysql.svg" alt="MySQL logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>MySQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/mysql.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds one row to a table and returns how many rows were written. Use Table update to change an existing row, or Table upsert when the row may already exist.

Prerequisites
-------------

* **Connection:** MySQL connection connection. See :doc:`the MySQL prerequisites <../mysql>`.
* The connection's account must be allowed to change this data in MySQL.

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
   * - ``table``
     - Table
     - text
     - Yes
     - The table name as Table listTables returns it, for example customers or, with its schema, sales.customers, in letters, digits, underscore, dot and $ only (quoted names are refused).
   * - ``row``
     - Row
     - JSON object
     - Yes
     - The new row as one JSON object of column name to value, columns left out taking their default; the columns depend on the table, so they come as one object rather than as separate fields, and Table describe lists them. Example: {"name": "Acme Ltd", "city": "Pune", "status": "active"}.
   * - ``schema``
     - Schema
     - text
     - No
     - The database (MySQL's word for a schema) that holds the table, when it is not the connection's default. Example: sales.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **MySQL**, connect, and tick **insert** in the **Table** row. The model sees it as ``mysql_table_insert``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **MySQL**, then **Insert a row**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
