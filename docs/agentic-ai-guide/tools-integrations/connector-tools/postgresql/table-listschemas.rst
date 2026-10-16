:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../postgresql.html">PostgreSQL</a> › Table</p>

List schemas
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/postgresql.svg" alt="PostgreSQL logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>PostgreSQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>postgresql_table_listschemas</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the schemas in the database, one row each, including system schemas such as information\_schema. Use it to find where a table lives, then Table listTables.

Before you start
----------------

* A PostgreSQL connection. See :doc:`how to set one up <../postgresql>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **PostgreSQL** under **Connectors** and connect your PostgreSQL connection.
#. Tick **listSchemas** in the **Table** row, then click **Add to agent**.

The agent now sees ``postgresql_table_listschemas`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **List schemas** every time a flow reaches it, without the agent deciding, use the :doc:`List schemas App Action </agentic-ai-guide/tools-integrations/app-action-apps/postgresql/table-listschemas>`.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a></div>
