:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../onedrive.html">OneDrive</a> › Drive</p>

Get a user's OneDrive
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a user's OneDrive with its id, owner, web address and storage quota (total, used and remaining).

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/onedrive>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **OneDrive**.
#. **Action:** under **Drive**, choose **Get a user's OneDrive**.
#. **Details:** choose your Microsoft Graph connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from OneDrive** so later steps can use the columns, then **Save action**.

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
   * - **User**
     - No
     - The address whose OneDrive this is, for example someone@company.com.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``name, size, webUrl``.

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
     - Some records keep a value inside another value, such as a priority inside an issue. This decides how those inner values become columns.

       * ``deep`` (default): Every inner value gets its own column, named with dots, such as ``fields.priority.name``.
       * ``oneLevel``: Only the first level is split. Anything deeper stays in one column as JSON text.
       * ``json``: Each inner value stays whole, in one column of JSON text.

       See the example below the table.

**Nested fields, by example.** Take a record ``{"id": 7, "fields": {"priority": {"name": "High"}}}``. Each choice gives you these columns:

.. list-table::
   :header-rows: 1
   :widths: 20 80
   :class: tool-table

   * - Choice
     - Columns you get
   * - ``deep``
     - ``id`` = ``7`` and ``fields.priority.name`` = ``High``
   * - ``oneLevel``
     - ``id`` = ``7`` and ``fields.priority`` = ``{"name": "High"}``
   * - ``json``
     - ``id`` = ``7`` and ``fields`` = ``{"priority": {"name": "High"}}``

Keep ``deep`` unless a later step needs the whole inner value as JSON.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from OneDrive** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch OneDrive with this action and start the flow when something new turns up. Pick **OneDrive** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Storage state changed**
     - User is the OneDrive owner's address. Reports the drive whenever its storage state changes, for example from normal to nearing or critical.

Let an agent decide instead
---------------------------

To let an agent call **Get a user's OneDrive** only when a request needs it, add the :doc:`Get a user's OneDrive tool </agentic-ai-guide/tools-integrations/connector-tools/onedrive/drive-get>` to an Agent Node.

Other Drive actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="drive-getmany.html">List drives</a></div>
