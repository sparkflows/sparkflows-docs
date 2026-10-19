:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-sheets.html">Google Sheets</a> › Row</p>

Append rows
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Row</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds rows below the last row of the table in a tab and returns the range that was written.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-sheets>`.
* The account behind the connection must be allowed to change this data in Google Sheets.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Sheets**.
#. **Action:** under **Row**, choose **Append rows**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
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
   * - **Spreadsheet**
     - No
     - The spreadsheet's id, or its full URL.
   * - **Range**
     - No
     - The sheet or A1 range to read or write, for example Sheet1 or Sheet1!A1:D100. Blank means Sheet1.
   * - **Use the first row as column names**
     - No
     - How the first row of the sheet is used.

       * ``match`` (default): Each value goes under the column with the same name, and a read names its columns after the first row. An empty sheet gets the names as its first row.
       * ``none``: Values are written in the order they arrive, and read back as columns A, B, C.

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
     - What happens when a row cannot be written.

       * ``stop`` (default): The run stops at the first row that fails.
       * ``continue``: The other rows are still written. The failed row is marked ``failed`` in ``result_status``, with the reason in ``result_error``.

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
     - The id Google Sheets gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Append rows** only when a request needs it, add the :doc:`Append rows tool </agentic-ai-guide/tools-integrations/connector-tools/google-sheets/row-append>` to an Agent Node.

Other Row actions
-----------------

.. raw:: html

   <div class="tool-related"><a href="row-getmany.html">Read rows</a><a href="row-update.html">Update rows</a><a href="row-clear.html">Clear a range</a></div>
