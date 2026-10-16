:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-sheets.html">Google Sheets</a> › Spreadsheet</p>

Get a spreadsheet
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Spreadsheet</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-sheets.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a spreadsheet's metadata: title, locale, time zone, URL and each tab's properties such as sheetId, title and grid size. It returns no cell values; use Read rows for the contents.

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
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Field paths from the top of the spreadsheet, for example ["properties.title", "sheets.properties.title"]; blank returns all of the metadata. Example: ["properties.title", "sheets.properties"].

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Sheets**, connect, and tick **get** in the **Spreadsheet** row. The model sees it as ``google_sheets_spreadsheet_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Sheets**, then **Get a spreadsheet**, and fill in the inputs above. It runs every time the flow reaches it.

Other Spreadsheet tools
-----------------------

.. raw:: html

   <div class="tool-related"><a href="spreadsheet-create.html">Create a spreadsheet</a></div>
