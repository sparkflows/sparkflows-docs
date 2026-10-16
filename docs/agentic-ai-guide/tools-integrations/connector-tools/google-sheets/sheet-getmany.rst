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
     <div><dt>Tool name</dt><dd><code>google_sheets_sheet_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the tabs of a spreadsheet with each tab's sheetId, title, index and grid size. Use it to find a tab's name for a range or its numeric sheetId for Delete a tab; it returns no cell values.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-sheets>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Sheets** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Sheet** row, then click **Add to agent**.

The agent now sees ``google_sheets_sheet_getmany`` and calls it when a request needs it.

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

Need it on every run?
---------------------

To run **List tabs** every time a flow reaches it, without the agent deciding, use the :doc:`List tabs App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-sheets/sheet-getmany>`.

Other Sheet tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="sheet-add.html">Add a tab</a><a href="sheet-delete.html">Delete a tab</a></div>
