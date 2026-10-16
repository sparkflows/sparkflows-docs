:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sql-server.html">SQL Server</a> › Table</p>

List schemas
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sqlserver.svg" alt="SQL Server logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SQL Server</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sqlserver_table_listschemas</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the schemas in the database, one row each, such as dbo and the built-in ones. Use it to find where a table lives, then Table listTables.

Before you start
----------------

* A SQL Server connection. See :doc:`how to set one up <../sql-server>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SQL Server** under **Connectors** and connect your SQL Server connection.
#. Tick **listSchemas** in the **Table** row, then click **Add to agent**.

The agent now sees ``sqlserver_table_listschemas`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **List schemas** every time a flow reaches it, without the agent deciding, use the :doc:`List schemas App Action </agentic-ai-guide/tools-integrations/app-action-apps/sql-server/table-listschemas>`.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a></div>
