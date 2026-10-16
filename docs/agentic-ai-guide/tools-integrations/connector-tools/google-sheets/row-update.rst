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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_sheets_row_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Overwrites the cells of an exact range and returns the range and the number of cells updated. The values fill the range left to right from its first cell in the order the keys are given; headers are not matched. Read rows first to find the row number, then name its range, such as Sheet1!A4:D4.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-sheets>`.
* The account behind the connection must be allowed to change this data in Google Sheets.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Sheets** under **Connectors** and connect your Google connection.
#. Tick **update** in the **Row** row, then click **Add to agent**.

The agent now sees ``google_sheets_row_update`` and calls it when a request needs it.

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
     - Yes
     - The exact cells to overwrite, for example Sheet1!A4:D4 for row 4 of columns A to D; without it the write would start at Sheet1!A1, the header row.
   * - ``rows``
     - list of JSON object
     - Yes
     - The new values, one object per sheet row, for example [{"Name": "Widget", "Qty": 9}]; the keys only label the values, which are written left to right in key order. Example: [{"Name": "Widget", "Qty": 9, "Status": "Shipped"}].
   * - ``valueInputOption``
     - text
     - No
     - USER\_ENTERED (the default) parses each value as if typed into the sheet, so numbers, dates and formulas are recognised; RAW stores it exactly as given. One of: USER\_ENTERED, RAW.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Sheets.

Need it on every run?
---------------------

To run **Update rows** every time a flow reaches it, without the agent deciding, use the :doc:`Update rows App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-sheets/row-update>`.

Other Row tools
---------------

.. raw:: html

   <div class="tool-related"><a href="row-getmany.html">Read rows</a><a href="row-append.html">Append rows</a><a href="row-clear.html">Clear a range</a></div>
