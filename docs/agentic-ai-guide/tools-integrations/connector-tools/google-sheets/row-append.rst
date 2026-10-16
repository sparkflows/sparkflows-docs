:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-sheets.html">Google Sheets</a> › Row</p>

Append rows
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

   Adds rows below the last row of the table in a tab and returns the range that was written. Each row is an object keyed by column header; with headerRow match every value lands under the header of the same name, and an empty tab gets the keys as its header row. Use Update rows to overwrite cells that already hold data.

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
   * - ``rows``
     - Rows
     - list of JSON object
     - Yes
     - The rows to add, one object per row keyed by column header, for example [{"Name": "Widget", "Qty": 7}]; a key the header lacks becomes a new column at the end. Example: [{"Name": "Widget", "Qty": 7, "Status": "In stock"}].
   * - ``range``
     - Tab
     - text
     - No
     - The tab to append to, or a cell in it, for example Sheet1 or Orders!A1; blank appends to Sheet1.
   * - ``headerRow``
     - Match the header row
     - text
     - No
     - match reads the tab's first row and writes each value under the header of the same name; none writes the values in the order the keys are given, with no header lookup. Default: match. One of: match, none.
   * - ``valueInputOption``
     - Read values as
     - text
     - No
     - USER\_ENTERED (the default) parses each value as if typed into the sheet, so numbers, dates and formulas are recognised; RAW stores it exactly as given. One of: USER\_ENTERED, RAW.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Sheets**, connect, and tick **append** in the **Row** row. The model sees it as ``google_sheets_row_append``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Sheets**, then **Append rows**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Row tools
---------------

.. raw:: html

   <div class="tool-related"><a href="row-getmany.html">Read rows</a><a href="row-update.html">Update rows</a><a href="row-clear.html">Clear a range</a></div>
