:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-sheets.html">Google Sheets</a> › Row</p>

Read rows
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Row</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-sheets.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Reads the cell values of a tab or A1 range and returns one row per sheet row. With headerRow match and a range that starts at row 1 the columns are named after the first row; otherwise they are A, B, C. Use it to see what a sheet contains; Get a spreadsheet and List tabs return metadata only.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Sheets prerequisites <../google-sheets>`.

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
   * - ``spreadsheet``
     - Spreadsheet
     - text
     - Yes
     - The spreadsheet's id (the long key in its URL, between /d/ and /edit) or its exact name, which is looked up among the spreadsheets pinned on this tool and then in Google Drive. Example: 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms.
   * - ``range``
     - Range
     - text
     - No
     - The tab or A1 range to read, for example Sheet1 or Sheet1!A1:D100; the tab name goes here, never in spreadsheet, and blank reads all of Sheet1.
   * - ``headerRow``
     - First row is the header
     - text
     - No
     - match names the columns after the range's first row when the range starts at row 1; none returns every row, the first included, under columns A, B, C. Default: match. One of: match, none.
   * - ``valueRenderOption``
     - Values as
     - text
     - No
     - FORMATTED\_VALUE (the default) returns what the cells display, UNFORMATTED\_VALUE returns plain numbers without currency or thousands formatting, and FORMULA returns the formulas themselves. One of: FORMATTED\_VALUE, UNFORMATTED\_VALUE, FORMULA.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Sheets**, connect, and tick **list** in the **Row** row. The model sees it as ``google_sheets_row_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Sheets**, then **Read rows**, and fill in the inputs above. It runs every time the flow reaches it.

Other Row tools
---------------

.. raw:: html

   <div class="tool-related"><a href="row-append.html">Append rows</a><a href="row-update.html">Update rows</a><a href="row-clear.html">Clear a range</a></div>
