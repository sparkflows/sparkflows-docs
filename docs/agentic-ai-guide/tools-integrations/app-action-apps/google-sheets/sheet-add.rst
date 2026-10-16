:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-sheets.html">Google Sheets</a> › Sheet</p>

Add a tab
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Sheet</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds a new tab to an existing spreadsheet and returns its sheetId, title and index.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-sheets>`.
* The account behind the connection must be allowed to change this data in Google Sheets.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Sheets**.
#. **Action:** under **Sheet**, choose **Add a tab**.
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

Fields to set
-------------

Each row that arrives is written to Google Sheets. When its columns already have these names, leave **Fields to set** empty. Otherwise click the chip of a field to add it, then type its value or click one under **What arrives here**.

.. list-table::
   :header-rows: 1
   :widths: 24 22 54
   :class: tool-params

   * - Field
     - Column name
     - Example or hint
   * - **Tab name**
     - ``properties.title``
     - ``Round 2``
   * - **Position**
     - ``properties.index``
     - ``0``

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

To let an agent call **Add a tab** only when a request needs it, add the :doc:`Add a tab tool </agentic-ai-guide/tools-integrations/connector-tools/google-sheets/sheet-add>` to an Agent Node.

Other Sheet actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="sheet-getmany.html">List tabs</a><a href="sheet-delete.html">Delete a tab</a></div>
