:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../sql-server.html">SQL Server</a> › Query</p>

Run a SQL statement
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sqlserver.svg" alt="SQL Server logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>SQL Server</dd></div>
     <div><dt>Resource</dt><dd>Query</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs one SQL Server statement and commits it: a SELECT or WITH query returns its rows up to limit, and any other statement returns rowsAffected.

Before you start
----------------

* A SQL Server connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/sql-server>`.
* The account behind the connection must be allowed to change this data in SQL Server.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **SQL Server**.
#. **Action:** under **Query**, choose **Run a SQL statement**.
#. **Details:** choose your SQL Server connection, click **Test**, then fill in the boxes below.
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
   * - **SQL**
     - No
     - The statement to run, for example SELECT id, name FROM customers WHERE city = 'Pune'. For example ``SELECT id, name FROM customers``.
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
     - The id SQL Server gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch SQL Server with this action and start the flow when something new turns up. Pick **SQL Server** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Query result changed**
     - SQL is one SELECT statement in this database's own dialect, ending in ORDER BY, without values that change by themselves such as NOW(); only the first 500 rows are compared. The first check records the result; later checks report all of its rows whenever any value in it differs. A statement that writes is refused.
   * - **New row in a query result**
     - SQL is one SELECT statement, joins allowed, kept to recent rows with ORDER BY and LIMIT or TOP, and Filter the result column that identifies a row, for example id. The first check records the rows already returned; later checks report each row with a new value in that column. A statement that writes is refused.

Let an agent decide instead
---------------------------

To let an agent call **Run a SQL statement** only when a request needs it, add the :doc:`Run a SQL statement tool </agentic-ai-guide/tools-integrations/connector-tools/sql-server/query-run>` to an Agent Node.
