:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-sheets.html">Google Sheets</a> › Spreadsheet</p>

Create a spreadsheet
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Spreadsheet</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-sheets.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a new spreadsheet in the connection's Google Drive and returns its spreadsheetId, URL and tabs. It starts with one empty tab; add data afterwards with Append rows.

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
   * - ``title``
     - Title
     - text
     - Yes
     - The new spreadsheet's name. Example: Q4 order tracker.
   * - ``timeZone``
     - Time zone
     - text
     - No
     - The spreadsheet's time zone as an IANA name, for example Asia/Kolkata; blank uses the account's.
   * - ``locale``
     - Locale
     - text
     - No
     - The locale that sets number and date formats, for example en\_GB or en\_IN; blank uses the account's.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Sheets**, connect, and tick **create** in the **Spreadsheet** row. The model sees it as ``google_sheets_spreadsheet_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Sheets**, then **Create a spreadsheet**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Spreadsheet tools
-----------------------

.. raw:: html

   <div class="tool-related"><a href="spreadsheet-get.html">Get a spreadsheet</a></div>
