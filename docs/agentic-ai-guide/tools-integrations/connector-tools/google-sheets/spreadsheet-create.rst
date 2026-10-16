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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_sheets_spreadsheet_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a new spreadsheet in the connection's Google Drive and returns its spreadsheetId, URL and tabs. It starts with one empty tab; add data afterwards with Append rows.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-sheets>`.
* The account behind the connection must be allowed to change this data in Google Sheets.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Sheets** under **Connectors** and connect your Google connection.
#. Tick **create** in the **Spreadsheet** row, then click **Add to agent**.

The agent now sees ``google_sheets_spreadsheet_create`` and calls it when a request needs it.

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
   * - ``title``
     - text
     - Yes
     - The new spreadsheet's name. Example: Q4 order tracker.
   * - ``timeZone``
     - text
     - No
     - The spreadsheet's time zone as an IANA name, for example Asia/Kolkata; blank uses the account's.
   * - ``locale``
     - text
     - No
     - The locale that sets number and date formats, for example en\_GB or en\_IN; blank uses the account's.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Sheets.

Need it on every run?
---------------------

To run **Create a spreadsheet** every time a flow reaches it, without the agent deciding, use the :doc:`Create a spreadsheet App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-sheets/spreadsheet-create>`.

Other Spreadsheet tools
-----------------------

.. raw:: html

   <div class="tool-related"><a href="spreadsheet-get.html">Get a spreadsheet</a></div>
