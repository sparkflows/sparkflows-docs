:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-database.html">SQL Database</a> › Table</p>

Create a table
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/database.svg" alt="SQL Database logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Database</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>database_table_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a table from column names and SQL types and returns ok; it fails when the table already exists. Each type is a type name with an optional size and constraints, such as INTEGER PRIMARY KEY, VARCHAR(200) NOT NULL or NUMERIC(10, 2), and anything more (quotes, expressions, a second column in one type) is refused; DDL execute takes a full CREATE TABLE.

Before you start
----------------

* A Database connection. See :doc:`how to set one up <../sql-database>`.
* The account behind the connection must be allowed to change this data in SQL Database.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Database** under **Connectors** and connect your Database connection.
#. Tick **create** in the **Table** row, then click **Add to agent**.

The agent now sees ``database_table_create`` and calls it when a request needs it.

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
     - The new table's name, for example audit\_log, in letters, digits, underscore, dot and $ only (quoted names are refused).
   * - ``columns``
     - JSON object
     - Yes
     - The columns as one JSON object of column name to type, in the order they should appear, each type in the database's own syntax with an optional size, NOT NULL, NULL, PRIMARY KEY, UNIQUE or a DEFAULT of a number or keyword. Example: {"id": "INTEGER PRIMARY KEY", "name": "VARCHAR(200) NOT NULL", "created\_at": "TIMESTAMP DEFAULT CURRENT\_TIMESTAMP"}.
   * - ``schema``
     - text
     - No
     - The schema (a database on MySQL) that holds the table, when it is not the connection's default. Example: sales.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in SQL Database.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-get.html">Get a row by key</a><a href="table-getmany.html">List rows</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-describe.html">Describe a table</a><a href="table-count.html">Count rows</a><a href="table-sample.html">Sample rows</a><a href="table-drop.html">Drop a table</a><a href="table-truncate.html">Empty a table</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
