:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../postgresql.html">PostgreSQL</a> › Table</p>

Insert or update a row
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/postgresql.svg" alt="PostgreSQL logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>PostgreSQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/postgresql.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Updates the rows whose key column matches the key value inside row, or inserts row when none matches, and returns how many rows were updated and inserted. Use it to sync records without checking first whether they exist; it is an UPDATE followed by an INSERT, not one atomic statement.

Prerequisites
-------------

* **Connection:** PostgreSQL connection connection. See :doc:`the PostgreSQL prerequisites <../postgresql>`.
* The connection's account must be allowed to change this data in PostgreSQL.

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
     - The table name as Table listTables returns it, for example customers or, with its schema, sales.customers, in letters, digits, underscore, dot and $ only (quoted names are refused, and PostgreSQL folds it to lower case).
   * - ``keyColumn``
     - Key column
     - text
     - Yes
     - The column that identifies the row, for example id; row has to contain it with the key value.
   * - ``row``
     - Row
     - JSON object
     - Yes
     - One JSON object holding the key column with its value plus the other columns, used for the update and inserted whole when no row matches; the columns depend on the table, so they come as one object rather than as separate fields. Example: {"id": 1042, "name": "Acme Ltd", "status": "active"}.
   * - ``schema``
     - Schema
     - text
     - No
     - The schema that holds the table, for example sales; blank uses the connection's search path, usually public.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **PostgreSQL**, connect, and tick **upsert** in the **Table** row. The model sees it as ``postgresql_table_upsert``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **PostgreSQL**, then **Insert or update a row**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
