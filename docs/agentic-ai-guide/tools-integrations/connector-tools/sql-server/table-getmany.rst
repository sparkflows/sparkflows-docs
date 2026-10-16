:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-server.html">SQL Server</a> › Table</p>

List rows
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sqlserver.svg" alt="SQL Server logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Server</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sql-server.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Reads rows from one table, with an optional where filter, sort order and column list, and returns at most limit rows; the limit is part of the SQL (TOP), so a large table is never read whole. Use it to browse or filter one table; use Table get for one row by key and Query run for joins or grouping.

Prerequisites
-------------

* **Connection:** SQL Server connection connection. See :doc:`the SQL Server prerequisites <../sql-server>`.

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
   * - ``schema``
     - Schema
     - text
     - No
     - The schema that holds the table, for example sales; blank uses the login's default schema, usually dbo.
   * - ``where``
     - Where
     - text
     - No
     - A T-SQL condition without the word WHERE, used as written as one condition, so a semicolon or a comment outside quoted text is refused, for example status = 'open' AND created\_at >= DATEADD(day, -7, GETDATE()).
   * - ``orderBy``
     - Order by
     - text
     - No
     - Columns to sort by, separated by commas, each optionally followed by asc or desc. Example: created\_at desc.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Column names to return; blank returns every column. Example: ["id", "name", "email"].
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many rows at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SQL Server**, connect, and tick **list** in the **Table** row. The model sees it as ``sqlserver_table_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **SQL Server**, then **List rows**, and fill in the inputs above. It runs every time the flow reaches it.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
