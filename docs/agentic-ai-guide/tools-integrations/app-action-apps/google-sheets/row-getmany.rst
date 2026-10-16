:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-sheets.html">Google Sheets</a> › Row</p>

Read rows
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Row</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Reads the cell values of a tab or A1 range and returns one row per sheet row.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-sheets>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Sheets**.
#. **Action:** under **Row**, choose **Read rows**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Google Sheets** so later steps can use the columns, then **Save action**.

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
     - The sheet or A1 range to read or write, for example Sheet1 or Sheet1!A1:D100. Blank means Sheet1. For example ``Sheet1 or Sheet1!A1:D100``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``id, name``.
   * - **Use the first row as column names**
     - No
     - match: an append puts each value under the column of the same name (an empty sheet gets the names as its first row), and a read names its columns after the first row. none: values are written in the order they arrive and read back as columns A, B, C. Choices: ``match``, ``none``. Default: ``match``.

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

The records come out as rows, one per record. Click **Load the fields from Google Sheets** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Google Sheets with this action and start the flow when something new turns up. Pick **Google Sheets** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Row added**
     - Spreadsheet is the spreadsheet's URL or id, and Range the tab, for example Sheet1, in single quotes when its name has spaces. Reports each row added at the end of the sheet, with the header row's names.
   * - **Row added (by a key column)**
     - Spreadsheet is the spreadsheet's URL or id, Range the tab such as Sheet1, and Filter the header of a column with a value unique to each row, for example Order ID. Reports each row whose value in that column is new, wherever the row is inserted.
   * - **Form response received**
     - Spreadsheet is the spreadsheet's URL or id that a Google Form sends its responses to; the tab read is Form Responses 1. Reports each new response as one record with fields named after the form's questions.
   * - **Cells changed in a sheet or range**
     - Spreadsheet is the spreadsheet's URL or id, and Range the tab or cells to watch, for example Sheet1!A1:F50 or a single cell such as Summary!B2. Reports every row of the range whenever any value in it changes.

Let an agent decide instead
---------------------------

To let an agent call **Read rows** only when a request needs it, add the :doc:`Read rows tool </agentic-ai-guide/tools-integrations/connector-tools/google-sheets/row-getmany>` to an Agent Node.

Other Row actions
-----------------

.. raw:: html

   <div class="tool-related"><a href="row-append.html">Append rows</a><a href="row-update.html">Update rows</a><a href="row-clear.html">Clear a range</a></div>
