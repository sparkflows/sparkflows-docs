:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../mysql.html">MySQL</a> › Table</p>

Delete rows
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mysql.svg" alt="MySQL logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>MySQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Delete · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/mysql.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes the row whose key column equals keyValue, or every row matching where when no key value is given, and returns how many rows were deleted. It refuses to run with neither, so a whole table is never emptied by accident.

Prerequisites
-------------

* **Connection:** MySQL connection connection. See :doc:`the MySQL prerequisites <../mysql>`.
* The connection's account must be allowed to change this data in MySQL.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``table``
     - Table
     - text
     - Yes
     - The table name as Table listTables returns it, for example customers or, with its schema, sales.customers, in letters, digits, underscore, dot and $ only (quoted names are refused).
   * - ``keyValue``
     - Row key value
     - text
     - No
     - The key value of the row to delete; when set, where is not used. Example: 1042.
   * - ``keyColumn``
     - Key column
     - text
     - No
     - The column that holds the key; blank means id. Example: customer\_id.
   * - ``where``
     - Where
     - text
     - No
     - A MySQL condition without the word WHERE, used when keyValue is blank as one condition, so a semicolon or a comment outside quoted text is refused; every matching row is deleted, for example status = 'cancelled' AND created\_at < NOW() - INTERVAL 90 DAY.
   * - ``schema``
     - Schema
     - text
     - No
     - The database (MySQL's word for a schema) that holds the table, when it is not the connection's default. Example: sales.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **MySQL**, connect, and tick **delete** in the **Table** row. The model sees it as ``mysql_table_delete``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **MySQL**, then **Delete rows**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Table tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
