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
     <div><dt>Tool name</dt><dd><code>google_sheets_spreadsheet_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a spreadsheet's metadata: title, locale, time zone, URL and each tab's properties such as sheetId, title and grid size. It returns no cell values; use Read rows for the contents.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-sheets>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Sheets** under **Connectors** and connect your Google connection.
#. Tick **get** in the **Spreadsheet** row, then click **Add to agent**.

The agent now sees ``google_sheets_spreadsheet_get`` and calls it when a request needs it.

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
   * - ``fields``
     - list of text
     - No
     - Field paths from the top of the spreadsheet, for example ["properties.title", "sheets.properties.title"]; blank returns all of the metadata. Example: ["properties.title", "sheets.properties"].

Need it on every run?
---------------------

To run **Get a spreadsheet** every time a flow reaches it, without the agent deciding, use the :doc:`Get a spreadsheet App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-sheets/spreadsheet-get>`.

Other Spreadsheet tools
-----------------------

.. raw:: html

   <div class="tool-related"><a href="spreadsheet-create.html">Create a spreadsheet</a></div>
