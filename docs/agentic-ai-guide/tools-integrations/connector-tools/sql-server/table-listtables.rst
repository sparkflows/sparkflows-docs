:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-server.html">SQL Server</a> › Table</p>

List tables
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sqlserver.svg" alt="SQL Server logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Server</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sqlserver_table_listtables</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the tables in one schema, one row per table with its schema and name. Use it to find what the database holds; Table describe then gives a table's columns.

Before you start
----------------

* A SQL Server connection. See :doc:`how to set one up <../sql-server>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Server** under **Connectors** and connect your SQL Server connection.
#. Tick **listTables** in the **Table** row, then click **Add to agent**.

The agent now sees ``sqlserver_table_listtables`` and calls it when a request needs it.

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
   * - ``schema``
     - text
     - No
     - The schema to list, for example sales; blank lists the login's default schema, usually dbo.

Need it on every run?
---------------------

To run **List tables** every time a flow reaches it, without the agent deciding, use the :doc:`List tables App Action </agentic-ai-guide/tools-integrations/app-action-apps/sql-server/table-listtables>`.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listschemas.html">List schemas</a></div>
