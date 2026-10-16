:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../postgresql.html">PostgreSQL</a> › Table</p>

List rows
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/postgresql.svg" alt="PostgreSQL logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>PostgreSQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Reads rows from one table, with an optional where filter, sort order and column list, and returns at most limit rows; the limit is part of the SQL (LIMIT), so a large table is never read whole.

Before you start
----------------

* A PostgreSQL connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/postgresql>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **PostgreSQL**.
#. **Action:** under **Table**, choose **List rows**.
#. **Details:** choose your PostgreSQL connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from PostgreSQL** so later steps can use the columns, then **Save action**.

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
     - The table to work with, for example customers. A schema goes in its own field.
   * - **Schema (optional)**
     - No
     - The schema the table lives in, when it is not the connection's default. For example ``public``.
   * - **Where**
     - No
     - A filter in SQL, without the word WHERE, for example status = 'open'. Blank returns everything up to the limit.
   * - **Order by**
     - No
     - A column and a direction, for example created\_at desc.
   * - **Columns to return**
     - No
     - Comma-separated column names. Blank returns every column. For example ``id, name``.
   * - **Limit**
     - No
     - How many rows at most. A run from the canvas previews 20. Default: ``100``.

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
     - Some records keep a value inside another value, such as a priority inside an issue. This decides how those inner values become columns.

       * ``deep`` (default): Every inner value gets its own column, named with dots, such as ``fields.priority.name``.
       * ``oneLevel``: Only the first level is split. Anything deeper stays in one column as JSON text.
       * ``json``: Each inner value stays whole, in one column of JSON text.

       See the example below the table.

**Nested fields, by example.** Take a record ``{"id": 7, "fields": {"priority": {"name": "High"}}}``. Each choice gives you these columns:

.. list-table::
   :header-rows: 1
   :widths: 20 80
   :class: tool-table

   * - Choice
     - Columns you get
   * - ``deep``
     - ``id`` = ``7`` and ``fields.priority.name`` = ``High``
   * - ``oneLevel``
     - ``id`` = ``7`` and ``fields.priority`` = ``{"name": "High"}``
   * - ``json``
     - ``id`` = ``7`` and ``fields`` = ``{"priority": {"name": "High"}}``

Keep ``deep`` unless a later step needs the whole inner value as JSON.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from PostgreSQL** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch PostgreSQL with this action and start the flow when something new turns up. Pick **PostgreSQL** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Row added (by a date/time column)**
     - Table is the table to watch, for example orders, or sales.orders with its schema, and Filter the column that holds when a row was created, for example created\_at. Reports each row created since the last check. The column is compared with the check time in UTC.
   * - **Row changed (by an updated-at column)**
     - Table is the table to watch, for example orders, or sales.orders with its schema, and Filter the column that holds when a row was last changed, for example updated\_at. Reports each row every time it is changed. The column is compared with the check time in UTC.
   * - **Row added (by an increasing id column)**
     - Table is the table to watch, for example orders, or sales.orders with its schema, and Filter the id column, for example id. The first check records the newest 500 rows; later checks report each row with a new id.
   * - **Row starts matching a condition**
     - Table is the table to watch, for example orders, or sales.orders with its schema. Where is a SQL condition such as status = 'failed', followed by ORDER BY the key column, for example ORDER BY id DESC, when more than 500 rows can meet it; Filter is that key column, for example id. The first check records the rows that already meet the condition; later checks report each row that newly meets it, inserted or updated into it.
   * - **Values changed in chosen columns**
     - Table is the table to watch, for example orders, or sales.orders with its schema. Columns to return lists the columns to watch, for example id, status, and Order by a unique column such as id, so the rows keep their order; the first 500 rows are watched. Reports every row, with those columns, whenever a value changes or a row is added or removed.

Let an agent decide instead
---------------------------

To let an agent call **List rows** only when a request needs it, add the :doc:`List rows tool </agentic-ai-guide/tools-integrations/connector-tools/postgresql/table-getmany>` to an Agent Node.

Other Table actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
