:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-database.html">SQL Database</a> › Table</p>

List rows
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/database.svg" alt="SQL Database logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Database</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>database_table_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Reads rows from one table, with an optional where filter and column list, and returns the first limit rows in the order the database gives them; the limit is part of the SQL (LIMIT, or TOP on SQL Server) everywhere but Oracle. There is no sort here, so Query run with ORDER BY sorts; Table get fetches one row by key.

Before you start
----------------

* A Database connection. See :doc:`how to set one up <../sql-database>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Database** under **Connectors** and connect your Database connection.
#. Tick **list** in the **Table** row, then click **Add to agent**.

The agent now sees ``database_table_getmany`` and calls it when a request needs it.

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
   * - ``schema``
     - text
     - No
     - The schema (a database on MySQL) that holds the table, when it is not the connection's default. Example: sales.
   * - ``where``
     - text
     - No
     - A condition in the database's own SQL without the word WHERE, used as written as one condition, so a semicolon or a comment outside quoted text is refused, for example status = 'open' AND total > 100.
   * - ``fields``
     - list of text
     - No
     - Column names to return; blank returns every column. Example: ["id", "name", "email"].
   * - ``limit``
     - whole number
     - No
     - How many rows at most. Default: 50.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-get.html">Get a row by key</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-describe.html">Describe a table</a><a href="table-count.html">Count rows</a><a href="table-sample.html">Sample rows</a><a href="table-create.html">Create a table</a><a href="table-drop.html">Drop a table</a><a href="table-truncate.html">Empty a table</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
