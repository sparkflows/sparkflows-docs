:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-sheets.html">Google Sheets</a> › Row</p>

Clear a range
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Row</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_sheets_row_clear</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Empties the values in a range and returns the range that was cleared; formatting and the rows themselves stay. Use Delete a tab to remove a whole tab instead.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-sheets>`.
* The account behind the connection must be allowed to change this data in Google Sheets.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Sheets** under **Connectors** and connect your Google connection.
#. Tick **clear** in the **Row** row, then click **Add to agent**.

The agent now sees ``google_sheets_row_clear`` and calls it when a request needs it.

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
     - The cells to empty, for example Sheet1!A2:D100, or a tab name to empty the whole tab; without it the whole of Sheet1 would be cleared.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Sheets.

Need it on every run?
---------------------

To run **Clear a range** every time a flow reaches it, without the agent deciding, use the :doc:`Clear a range App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-sheets/row-clear>`.

Other Row tools
---------------

.. raw:: html

   <div class="tool-related"><a href="row-getmany.html">Read rows</a><a href="row-append.html">Append rows</a><a href="row-update.html">Update rows</a></div>
