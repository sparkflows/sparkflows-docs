:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-sheets.html">Google Sheets</a> › Row</p>

Update rows
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Row</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-sheets.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Overwrites the cells of an exact range and returns the range and the number of cells updated. The values fill the range left to right from its first cell in the order the keys are given; headers are not matched. Read rows first to find the row number, then name its range, such as Sheet1!A4:D4.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Sheets prerequisites <../google-sheets>`.
* The connection's account must be allowed to change this data in Google Sheets.

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
     - Yes
     - The exact cells to overwrite, for example Sheet1!A4:D4 for row 4 of columns A to D; without it the write would start at Sheet1!A1, the header row.
   * - ``rows``
     - New values
     - list of JSON object
     - Yes
     - The new values, one object per sheet row, for example [{"Name": "Widget", "Qty": 9}]; the keys only label the values, which are written left to right in key order. Example: [{"Name": "Widget", "Qty": 9, "Status": "Shipped"}].
   * - ``valueInputOption``
     - Read values as
     - text
     - No
     - USER\_ENTERED (the default) parses each value as if typed into the sheet, so numbers, dates and formulas are recognised; RAW stores it exactly as given. One of: USER\_ENTERED, RAW.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Sheets**, connect, and tick **update** in the **Row** row. The model sees it as ``google_sheets_row_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Sheets**, then **Update rows**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Row tools
---------------

.. raw:: html

   <div class="tool-related"><a href="row-getmany.html">Read rows</a><a href="row-append.html">Append rows</a><a href="row-clear.html">Clear a range</a></div>
