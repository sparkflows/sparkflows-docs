.. _connector-tools-sql-database:

.. rst-class:: agentic-tutorial

SQL Database Tools
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../_static/img/tools/database.svg" alt="SQL Database logo">
     <dl class="tool-facts">
     <div><dt>Connection</dt><dd>Database</dd></div>
     <div><dt>Tools</dt><dd>18 across 4 resources</dd></div>
     <div><dt>Reads / writes</dt><dd>8 / 10</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
     <div class="tool-chips"><span class="tool-chip is-new">New</span></div>
   </div>

.. container:: tutorial-intro

   Let an agent work with any SQL database Sparkflows can connect to: list schemas and tables, describe, read, count and sample rows, insert, update, upsert and delete rows, explain or run a query, call a stored procedure, and create, empty or drop tables. Each tool speaks the connected database's own SQL.

.. container:: tutorial-start

   **Agent tool only.** SQL Database is available in the agent tool picker. It is not offered as an :doc:`App Action </agentic-ai-guide/tools-integrations/app-actions>` node yet, so a fixed workflow step cannot call it.

.. contents:: On this page
   :local:
   :depth: 1
   :class: tool-toc

Prerequisites
-------------

* **Connection:** A database connection of one of these types: JDBC, MySQL, PostgreSQL, Oracle, Snowflake, Redshift, BigQuery, Databricks, Teradata, Trino, Synapse or SQL. The picker lists every such connection in the project, so choose the one that points at the database the agent should use.
* A database the Sparkflows server can reach.
* A database user with ``SELECT`` on the tables the agent reads. Grant ``INSERT``, ``UPDATE``, ``DELETE`` or DDL rights only where the agent may change things.
* A saved connection that passes **Test Connection**. See :doc:`/agentic-ai-guide/quick-start/model-connections`.

Add SQL Database to an agent
----------------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node on the canvas.
#. Choose **SQL Database** under **Connectors**, or type ``sql`` in the search box.
#. **Connect.** Choose your Database connection and click **Test connection**. The rest of the screen unlocks when it shows **Connected**.
#. **How the agent sees it.** Keep **A separate tool for each one**, so the agent picks each operation by name.
#. **Tick the operations.** The grid opens with the **Look things up** pack: reads only. Add each write the agent needs; every write waits for approval when it runs.
#. Click **Add to agent**. The ticked operations arrive as one SQL Database node, joined to the Agent Node by a dashed tool link.

Tools
-----

Each ticked operation becomes one tool, named ``database_<resource>_<operation>``. **Read** tools run straight away. **Write** and **Delete** tools change data in SQL Database, so each call waits for :doc:`human approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it takes effect. Click a tool to open its page with every parameter.

.. raw:: html

   <nav class="tool-jump" aria-label="Jump to a resource"><a href="#res-query">Query<span>2</span></a><a href="#res-table">Table<span>14</span></a><a href="#res-procedure">Procedure<span>1</span></a><a href="#res-ddl">DDL<span>1</span></a></nav>

.. raw:: html

   <span id="res-query" class="tool-anchor"></span>

Query
~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sql-database/query-run.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Run a SQL statement</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Runs one statement in the connected database&#x27;s own SQL and commits it: a query returns its rows up to limit, and any other statement returns rowsAffected.</span>
     </a>
     <a class="tool-op" href="sql-database/query-explain.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Explain a query</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns the database&#x27;s plan for one query without running it (EXPLAIN, or EXPLAIN PLAN FOR on Oracle, which stores the plan in PLAN_TABLE and returns only ok), and refuses an ANALYZE option or a second statement, since either would run SQL. Use it to see why a query is slow before running it; SQL Server has no EXPLAIN statement, so it fails there.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-table" class="tool-anchor"></span>

Table
~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sql-database/table-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a row by key</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Reads the one row whose key column equals the given value and returns all its columns, or no row when none matches.</span>
     </a>
     <a class="tool-op" href="sql-database/table-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List rows</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Reads rows from one table, with an optional where filter and column list, and returns the first limit rows in the order the database gives them; the limit is part of the SQL (LIMIT, or TOP on SQL Server) everywhere but Oracle.</span>
     </a>
     <a class="tool-op" href="sql-database/table-insert.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Insert a row</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Adds one row to a table and returns how many rows were written.</span>
     </a>
     <a class="tool-op" href="sql-database/table-update.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Update a row by key</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Sets the columns given in row on the rows whose key column equals the key value inside row, and returns how many rows changed.</span>
     </a>
     <a class="tool-op" href="sql-database/table-upsert.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Insert or update a row</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Updates the rows whose key column matches the key value inside row, or inserts row when none matches, and returns how many rows were updated and inserted.</span>
     </a>
     <a class="tool-op" href="sql-database/table-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete rows</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes the row whose key column equals keyValue, or every row matching where when no key value is given, and returns how many rows were deleted.</span>
     </a>
     <a class="tool-op" href="sql-database/table-describe.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Describe a table</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns each column of a table with its name, type, nullable flag and default.</span>
     </a>
     <a class="tool-op" href="sql-database/table-count.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Count rows</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Counts the rows of a table, or only those matching where, and returns the number as row_count.</span>
     </a>
     <a class="tool-op" href="sql-database/table-sample.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Sample rows</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns the first rows of a table with no filter or sort, as a quick look at its contents.</span>
     </a>
     <a class="tool-op" href="sql-database/table-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a table</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Creates a table from column names and SQL types and returns ok; it fails when the table already exists.</span>
     </a>
     <a class="tool-op" href="sql-database/table-drop.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Drop a table</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes a table with all its rows; this cannot be undone.</span>
     </a>
     <a class="tool-op" href="sql-database/table-truncate.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Empty a table</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Removes every row from a table but keeps the table and its columns (TRUNCATE TABLE, or DELETE FROM where the database has no TRUNCATE).</span>
     </a>
     <a class="tool-op" href="sql-database/table-listtables.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List tables</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the tables in one schema, one row per table with its schema and name.</span>
     </a>
     <a class="tool-op" href="sql-database/table-listschemas.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List schemas</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the schemas the connection can see, one row each (databases, on MySQL).</span>
     </a>
   </div>

.. raw:: html

   <span id="res-procedure" class="tool-anchor"></span>

Procedure
~~~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sql-database/procedure-invoke.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Call a stored procedure</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Calls a stored procedure with its arguments in order, argument1 first, as CALL name(...) or, on SQL Server, EXEC name ..., and commits.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-ddl" class="tool-anchor"></span>

DDL
~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sql-database/ddl-execute.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Run a DDL statement</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Runs one statement that returns no rows, such as CREATE, ALTER, DROP, GRANT or EXEC, commits it and returns rowsAffected.</span>
     </a>
   </div>

Good to know
------------

* **List rows** builds the limit into the SQL, so a large table is never read whole. It does not sort; use **Run a SQL statement** with ``ORDER BY`` when order matters.
* **Delete rows** refuses to run without a key value or a ``where`` filter, so a whole table cannot be emptied by accident.
* **Run a SQL statement** and **Run a DDL statement** commit whatever they run, so both are approval-gated as writes.
* **Drop a table** and **Empty a table** cannot be undone. Leave them unticked unless the agent truly needs them.
* **Explain a query** shows the plan without running the query. SQL Server has no ``EXPLAIN``, so it fails there.
* Fix ``table`` (and ``schema``) on the tools in **Fixed settings** to keep the agent on one table.

Example
-------

**Look up an order.** Fix table = orders on every tool. Then give the Agent Node instructions like these:

.. code-block:: text

   You answer questions about customer orders.
   Before any query, describe the orders table so you use real column names.
   Find orders with List rows and a where filter; never run free SQL.
   Answer with the order id, status and total. If nothing matches, say so.

Other common uses:

* Answer questions from a reporting table in Snowflake, Redshift or BigQuery.
* Look a record up by key before drafting a reply or a summary.
* Save an agent's result back to a table after approval.

Troubleshooting
---------------

**The grid stays locked after Test connection.**
   The connection could not log in or reach the server. Open the connection under **Administration → Global/Group Connections**, check the JDBC URL, user and password, and test it there first. The Sparkflows server must be able to reach the database host and port.

**The agent guesses column names and the query fails.**
   Tick **describe** and **listTables** and tell the agent to call them before reading or writing: *"Describe a table before you query it. Never guess column names."*

**A write was refused or did nothing.**
   Writes need the database user to hold INSERT, UPDATE or DELETE on that table, and every write waits for approval when it runs. An update or upsert needs the key column inside ``row``.

**The agent does not call the tool, or picks the wrong one.**
   Name the tool in the instructions and untick operations that sound alike. See :ref:`making-tools-reliable`.

FAQ
---

**SQL Database or the MySQL, PostgreSQL and SQL Server connectors?**
   Both work with their engines. SQL Database also works with the other connection types above, and adds tools to explain queries, sample rows, call stored procedures, and create, empty or drop tables.

**Is it available as an App Action?**
   Not yet. SQL Database is offered as an agent tool; its App Action is still marked Coming soon.

Related
-------

* :doc:`/agentic-ai-guide/tools-integrations/tools-connectors` - how tools work, choosing operations, and fixed settings
* :doc:`/agentic-ai-guide/tools-integrations/connector-tools/index` - every connector
* :doc:`/agentic-ai-guide/safety-guardrails/human-in-the-loop` - approving writes
