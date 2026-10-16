:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../postgresql.html">PostgreSQL</a> › Table</p>

Get a row by key
================

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

   Reads the one row whose key column equals the given value and returns all its columns, or no row when none matches.

Before you start
----------------

* A PostgreSQL connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/postgresql>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **PostgreSQL**.
#. **Action:** under **Table**, choose **Get a row by key**.
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
     - The table to work with, for example customers. A schema goes in its own field. For example ``customers``.
   * - **Row key value**
     - No
     - The value of the key column that identifies the row, for example 1042. For example ``1042``.
   * - **Schema (optional)**
     - No
     - The schema the table lives in, when it is not the connection's default. For example ``public``.
   * - **Key column**
     - No
     - The column that identifies a row, for example id. Update, upsert and delete match on it; get reads the row whose key equals the row key value. For example ``id``.

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

The records come out as rows, one per record. Click **Load the fields from PostgreSQL** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch PostgreSQL with this action and start the flow when something new turns up. Pick **PostgreSQL** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Specific row changed**
     - Table is the table to watch, for example orders, or sales.orders with its schema, and Key column and Row key value the one row to watch, for example order\_id and 1042; the key column must be unique. Reports the row whenever any of its values changes.

Let an agent decide instead
---------------------------

To let an agent call **Get a row by key** only when a request needs it, add the :doc:`Get a row by key tool </agentic-ai-guide/tools-integrations/connector-tools/postgresql/table-get>` to an Agent Node.

Other Table actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-upsert.html">Insert or update a row</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
