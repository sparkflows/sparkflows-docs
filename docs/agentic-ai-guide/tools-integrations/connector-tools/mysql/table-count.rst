:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../mysql.html">MySQL</a> › Table</p>

Count rows
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mysql.svg" alt="MySQL logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>MySQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>mysql_table_count</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Counts the rows of a table, or only those matching where, and returns the number as row\_count. Use it instead of listing when only the number is needed.

Before you start
----------------

* A MySQL connection. See :doc:`how to set one up <../mysql>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **MySQL** under **Connectors** and connect your MySQL connection.
#. Tick **count** in the **Table** row, then click **Add to agent**.

The agent now sees ``mysql_table_count`` and calls it when a request needs it.

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
   * - ``where``
     - text
     - No
     - A MySQL condition without the word WHERE that picks the rows to count, used as written as one condition, so a semicolon or a comment outside quoted text is refused; blank counts every row. Example: status = 'open'.
   * - ``schema``
     - text
     - No
     - The database (MySQL's word for a schema) that holds the table, when it is not the connection's default. Example: sales.

Need it on every run?
---------------------

To run **Count rows** every time a flow reaches it, without the agent deciding, use the :doc:`Count rows App Action </agentic-ai-guide/tools-integrations/app-action-apps/mysql/table-count>`.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
