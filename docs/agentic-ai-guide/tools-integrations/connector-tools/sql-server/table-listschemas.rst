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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sql-server.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the schemas in the database, one row each, such as dbo and the built-in ones. Use it to find where a table lives, then Table listTables.

Prerequisites
-------------

* **Connection:** SQL Server connection connection. See :doc:`the SQL Server prerequisites <../sql-server>`.

Parameters
----------

This tool takes no parameters.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SQL Server**, connect, and tick **listSchemas** in the **Table** row. The model sees it as ``sqlserver_table_listschemas``.

**As an App Action.** Drop **App Action** on the canvas, pick **SQL Server**, then **List schemas**, and fill in the inputs above. It runs every time the flow reaches it.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a></div>
