:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-sheets.html">Google Sheets</a> › Spreadsheet</p>

Get a spreadsheet
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Spreadsheet</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a spreadsheet's metadata: title, locale, time zone, URL and each tab's properties such as sheetId, title and grid size.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-sheets>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Sheets**.
#. **Action:** under **Spreadsheet**, choose **Get a spreadsheet**.
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
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``id, name``.

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

Let an agent decide instead
---------------------------

To let an agent call **Get a spreadsheet** only when a request needs it, add the :doc:`Get a spreadsheet tool </agentic-ai-guide/tools-integrations/connector-tools/google-sheets/spreadsheet-get>` to an Agent Node.

Other Spreadsheet actions
-------------------------

.. raw:: html

   <div class="tool-related"><a href="spreadsheet-create.html">Create a spreadsheet</a></div>
