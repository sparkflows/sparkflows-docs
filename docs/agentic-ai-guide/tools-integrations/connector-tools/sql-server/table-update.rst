:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-server.html">SQL Server</a> › Table</p>

Update a row by key
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sqlserver.svg" alt="SQL Server logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Server</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sql-server.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sets the columns given in row on the rows whose key column equals the key value inside row, and returns how many rows changed. The key value is read from row itself, so row has to include the key column; unlike Table upsert it never inserts.

Prerequisites
-------------

* **Connection:** SQL Server connection connection. See :doc:`the SQL Server prerequisites <../sql-server>`.
* The connection's account must be allowed to change this data in SQL Server.

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
   * - ``keyColumn``
     - Key column
     - text
     - Yes
     - The column that identifies the row, for example id; row has to contain it with the key value.
   * - ``row``
     - Row
     - JSON object
     - Yes
     - One JSON object holding the key column with its value plus the columns to change; the columns depend on the table, so they come as one object rather than as separate fields, and a row without the key column changes nothing. Example: {"id": 1042, "status": "closed"}.
   * - ``schema``
     - Schema
     - text
     - No
     - The schema that holds the table, for example sales; blank uses the login's default schema, usually dbo.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SQL Server**, connect, and tick **update** in the **Table** row. The model sees it as ``sqlserver_table_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **SQL Server**, then **Update a row by key**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
