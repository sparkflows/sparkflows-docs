:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../sql-server.html">SQL Server</a> › Table</p>

Count rows
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sqlserver.svg" alt="SQL Server logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>SQL Server</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Counts the rows of a table, or only those matching where, and returns the number as row\_count.

Before you start
----------------

* A SQL Server connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/sql-server>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **SQL Server**.
#. **Action:** under **Table**, choose **Count rows**.
#. **Details:** choose your SQL Server connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from SQL Server** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Table**
     - No
     - The table to work with, for example customers. A schema goes in its own field. For example ``customers``.
   * - **Schema (optional)**
     - No
     - The schema the table lives in, when it is not the connection's default. For example ``public``.
   * - **Where**
     - No
     - A filter in SQL, without the word WHERE, for example status = 'open'. Blank returns everything up to the limit. For example ``status = 'open'``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from SQL Server** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch SQL Server with this action and start the flow when something new turns up. Pick **SQL Server** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Row count changed**
     - Table is the table to watch, for example orders, or sales.orders with its schema. The first check records the number of rows; later checks report the new number as row\_count whenever it differs, rows added or removed.
   * - **Count of matching rows changed**
     - Table is the table to watch, for example orders, or sales.orders with its schema, and Where a SQL condition such as status = 'open', without ORDER BY. The first check records how many rows meet it; later checks report the new number as row\_count whenever it differs.

Let an agent decide instead
---------------------------

To let an agent call **Count rows** only when a request needs it, add the :doc:`Count rows tool </agentic-ai-guide/tools-integrations/connector-tools/sql-server/table-count>` to an Agent Node.

Other Table actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
