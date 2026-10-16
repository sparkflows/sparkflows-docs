:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-sheets.html">Google Sheets</a> › Sheet</p>

List tabs
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Sheet</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-sheets.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the tabs of a spreadsheet with each tab's sheetId, title, index and grid size. Use it to find a tab's name for a range or its numeric sheetId for Delete a tab; it returns no cell values.

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

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Sheets**, connect, and tick **list** in the **Sheet** row. The model sees it as ``google_sheets_sheet_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Sheets**, then **List tabs**, and fill in the inputs above. It runs every time the flow reaches it.

Other Sheet tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="sheet-add.html">Add a tab</a><a href="sheet-delete.html">Delete a tab</a></div>
