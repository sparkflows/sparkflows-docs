:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-database.html">SQL Database</a> › Table</p>

Update a row by key
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/database.svg" alt="SQL Database logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Database</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>database_table_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sets the columns given in row on the rows whose key column equals the key value inside row, and returns how many rows changed. The key value is read from row itself, so row has to include the key column; unlike Table upsert it never inserts.

Before you start
----------------

* A Database connection. See :doc:`how to set one up <../sql-database>`.
* The account behind the connection must be allowed to change this data in SQL Database.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Database** under **Connectors** and connect your Database connection.
#. Tick **update** in the **Table** row, then click **Add to agent**.

The agent now sees ``database_table_update`` and calls it when a request needs it.

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
   * - ``table``
     - text
     - Yes
     - The table name as Table listTables returns it, for example customers or, with its schema, sales.customers, in letters, digits, underscore, dot and $ only (quoted names are refused).
   * - ``keyColumn``
     - text
     - Yes
     - The column that identifies the row, for example id; row has to contain it with the key value.
   * - ``row``
     - JSON object
     - Yes
     - One JSON object holding the key column with its value plus the columns to change; the columns depend on the table, so they come as one object rather than as separate fields, and a row without the key column changes nothing. Example: {"id": 1042, "status": "closed"}.
   * - ``schema``
     - text
     - No
     - The schema (a database on MySQL) that holds the table, when it is not the connection's default. Example: sales.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in SQL Database.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-get.html">Get a row by key</a><a href="table-getmany.html">List rows</a><a href="table-insert.html">Insert a row</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-describe.html">Describe a table</a><a href="table-count.html">Count rows</a><a href="table-sample.html">Sample rows</a><a href="table-create.html">Create a table</a><a href="table-drop.html">Drop a table</a><a href="table-truncate.html">Empty a table</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
