:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-server.html">SQL Server</a> › Table</p>

Describe a table
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sqlserver.svg" alt="SQL Server logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Server</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sqlserver_table_describe</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns each column of a table with its name, type, nullable flag and default. Use it before an insert or update to learn the column names, or to check that a table exists; Table listTables gives the table names.

Before you start
----------------

* A SQL Server connection. See :doc:`how to set one up <../sql-server>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Server** under **Connectors** and connect your SQL Server connection.
#. Tick **describe** in the **Table** row, then click **Add to agent**.

The agent now sees ``sqlserver_table_describe`` and calls it when a request needs it.

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
     - The schema that holds the table, for example sales; blank uses the login's default schema, usually dbo.

Need it on every run?
---------------------

To run **Describe a table** every time a flow reaches it, without the agent deciding, use the :doc:`Describe a table App Action </agentic-ai-guide/tools-integrations/app-action-apps/sql-server/table-describe>`.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
