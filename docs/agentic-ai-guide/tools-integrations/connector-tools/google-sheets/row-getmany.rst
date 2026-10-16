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
     <div><dt>Tool name</dt><dd><code>google_sheets_row_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Reads the cell values of a tab or A1 range and returns one row per sheet row. With headerRow match and a range that starts at row 1 the columns are named after the first row; otherwise they are A, B, C. Use it to see what a sheet contains; Get a spreadsheet and List tabs return metadata only.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-sheets>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Sheets** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Row** row, then click **Add to agent**.

The agent now sees ``google_sheets_row_getmany`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``spreadsheet``
     - text
     - Yes
     - The spreadsheet's id (the long key in its URL, between /d/ and /edit) or its exact name, which is looked up among the spreadsheets pinned on this tool and then in Google Drive. Example: 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms.
   * - ``range``
     - text
     - No
     - The tab or A1 range to read, for example Sheet1 or Sheet1!A1:D100; the tab name goes here, never in spreadsheet, and blank reads all of Sheet1.
   * - ``headerRow``
     - text
     - No
     - match names the columns after the range's first row when the range starts at row 1; none returns every row, the first included, under columns A, B, C. Default: match. One of: match, none.
   * - ``valueRenderOption``
     - text
     - No
     - FORMATTED\_VALUE (the default) returns what the cells display, UNFORMATTED\_VALUE returns plain numbers without currency or thousands formatting, and FORMULA returns the formulas themselves. One of: FORMATTED\_VALUE, UNFORMATTED\_VALUE, FORMULA.

Need it on every run?
---------------------

To run **Read rows** every time a flow reaches it, without the agent deciding, use the :doc:`Read rows App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-sheets/row-getmany>`.

Other Row tools
---------------

.. raw:: html

   <div class="tool-related"><a href="row-append.html">Append rows</a><a href="row-update.html">Update rows</a><a href="row-clear.html">Clear a range</a></div>
