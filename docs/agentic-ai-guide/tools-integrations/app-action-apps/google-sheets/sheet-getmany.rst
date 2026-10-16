:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-sheets.html">Google Sheets</a> › Sheet</p>

List tabs
=========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_sheets.svg" alt="Google Sheets logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Sheets</dd></div>
     <div><dt>Resource</dt><dd>Sheet</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the tabs of a spreadsheet with each tab's sheetId, title, index and grid size.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-sheets>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Sheets**.
#. **Action:** under **Sheet**, choose **List tabs**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Google Sheets** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Spreadsheet**
     - No
     - The spreadsheet's id, or its full URL.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``id, name``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Google Sheets** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Google Sheets with this action and start the flow when something new turns up. Pick **Google Sheets** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Tab added**
     - Spreadsheet is the spreadsheet's URL or id. The first check records its tabs; later checks report each new tab, with its title in properties.title.

Let an agent decide instead
---------------------------

To let an agent call **List tabs** only when a request needs it, add the :doc:`List tabs tool </agentic-ai-guide/tools-integrations/connector-tools/google-sheets/sheet-getmany>` to an Agent Node.

Other Sheet actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="sheet-add.html">Add a tab</a><a href="sheet-delete.html">Delete a tab</a></div>
