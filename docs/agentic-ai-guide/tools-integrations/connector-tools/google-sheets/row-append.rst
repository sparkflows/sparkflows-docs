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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_sheets_row_append</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds rows below the last row of the table in a tab and returns the range that was written. Each row is an object keyed by column header; with headerRow match every value lands under the header of the same name, and an empty tab gets the keys as its header row. Use Update rows to overwrite cells that already hold data.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-sheets>`.
* The account behind the connection must be allowed to change this data in Google Sheets.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Sheets** under **Connectors** and connect your Google connection.
#. Tick **append** in the **Row** row, then click **Add to agent**.

The agent now sees ``google_sheets_row_append`` and calls it when a request needs it.

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
   * - ``rows``
     - list of JSON object
     - Yes
     - The rows to add, one object per row keyed by column header, for example [{"Name": "Widget", "Qty": 7}]; a key the header lacks becomes a new column at the end. Example: [{"Name": "Widget", "Qty": 7, "Status": "In stock"}].
   * - ``range``
     - text
     - No
     - The tab to append to, or a cell in it, for example Sheet1 or Orders!A1; blank appends to Sheet1.
   * - ``headerRow``
     - text
     - No
     - match reads the tab's first row and writes each value under the header of the same name; none writes the values in the order the keys are given, with no header lookup. Default: match. One of: match, none.
   * - ``valueInputOption``
     - text
     - No
     - USER\_ENTERED (the default) parses each value as if typed into the sheet, so numbers, dates and formulas are recognised; RAW stores it exactly as given. One of: USER\_ENTERED, RAW.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Sheets.

Need it on every run?
---------------------

To run **Append rows** every time a flow reaches it, without the agent deciding, use the :doc:`Append rows App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-sheets/row-append>`.

Other Row tools
---------------

.. raw:: html

   <div class="tool-related"><a href="row-getmany.html">Read rows</a><a href="row-update.html">Update rows</a><a href="row-clear.html">Clear a range</a></div>
