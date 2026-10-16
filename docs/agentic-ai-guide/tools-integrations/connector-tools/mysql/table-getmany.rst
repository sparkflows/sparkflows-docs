:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../mysql.html">MySQL</a> › Table</p>

List rows
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mysql.svg" alt="MySQL logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>MySQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>mysql_table_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Reads rows from one table, with an optional where filter, sort order and column list, and returns at most limit rows; the limit is part of the SQL (LIMIT), so a large table is never read whole. Use it to browse or filter one table; use Table get for one row by key and Query run for joins or grouping.

Before you start
----------------

* A MySQL connection. See :doc:`how to set one up <../mysql>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **MySQL** under **Connectors** and connect your MySQL connection.
#. Tick **list** in the **Table** row, then click **Add to agent**.

The agent now sees ``mysql_table_getmany`` and calls it when a request needs it.

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
     - The database (MySQL's word for a schema) that holds the table, when it is not the connection's default. Example: sales.
   * - ``where``
     - text
     - No
     - A MySQL condition without the word WHERE, used as written as one condition, so a semicolon or a comment outside quoted text is refused, for example status = 'open' AND created\_at >= NOW() - INTERVAL 7 DAY.
   * - ``orderBy``
     - text
     - No
     - Columns to sort by, separated by commas, each optionally followed by asc or desc. Example: created\_at desc.
   * - ``fields``
     - list of text
     - No
     - Column names to return; blank returns every column. Example: ["id", "name", "email"].
   * - ``limit``
     - whole number
     - No
     - How many rows at most. Default: 50.

Need it on every run?
---------------------

To run **List rows** every time a flow reaches it, without the agent deciding, use the :doc:`List rows App Action </agentic-ai-guide/tools-integrations/app-action-apps/mysql/table-getmany>`.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
