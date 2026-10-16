:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../mysql.html">MySQL</a> › Table</p>

Insert or update a row
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mysql.svg" alt="MySQL logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>MySQL</dd></div>
     <div><dt>Resource</dt><dd>Table</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Updates the rows whose key column matches the key value inside row, or inserts row when none matches, and returns how many rows were updated and inserted.

Before you start
----------------

* A MySQL connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/mysql>`.
* The account behind the connection must be allowed to change this data in MySQL.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **MySQL**.
#. **Action:** under **Table**, choose **Insert or update a row**.
#. **Details:** choose your MySQL connection, click **Test**, then fill in the boxes below.
#. Click **Save action**.

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
   * - **If a row is rejected**
     - No
     - stop fails the run at the first rejected row. continue writes the rest and marks that row failed in result\_status and result\_error. Choices: ``stop``, ``continue``. Default: ``stop``.

What it passes on
-----------------

Every row comes out with three columns added, so the next step can route on them:

.. list-table::
   :header-rows: 1
   :widths: 26 74
   :class: tool-table

   * - Column
     - Value
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``
   * - ``result_id``
     - The id MySQL gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Insert or update a row** only when a request needs it, add the :doc:`Insert or update a row tool </agentic-ai-guide/tools-integrations/connector-tools/mysql/table-upsert>` to an Agent Node.

Other Table actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="table-getmany.html">List rows</a><a href="table-get.html">Get a row by key</a><a href="table-count.html">Count rows</a><a href="table-describe.html">Describe a table</a><a href="table-insert.html">Insert a row</a><a href="table-update.html">Update a row by key</a><a href="table-delete.html">Delete rows</a><a href="table-listtables.html">List tables</a><a href="table-listschemas.html">List schemas</a></div>
