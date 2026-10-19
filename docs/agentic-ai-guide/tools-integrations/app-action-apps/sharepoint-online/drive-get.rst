:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../sharepoint-online.html">SharePoint</a> › Drive</p>

Get a document library
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>SharePoint</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one document library by its id with its name, owner, storage quota and web address.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/sharepoint-online>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **SharePoint**.
#. **Action:** under **Drive**, choose **Get a document library**.
#. **Details:** choose your Microsoft Graph or SharePoint connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from SharePoint** so later steps can use the columns, then **Save action**.

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
   * - **File, folder, list or item**
     - No
     - A file or folder by id or path (TestData/Reports), the list for List operations, or the item id for List Item operations. For example ``TestData/Reports, or an item id``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``name, path, size, webUrl``.

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

The records come out as rows, one per record. Click **Load the fields from SharePoint** to see the columns before you save.

Let an agent decide instead
---------------------------

To let an agent call **Get a document library** only when a request needs it, add the :doc:`Get a document library tool </agentic-ai-guide/tools-integrations/connector-tools/sharepoint-online/drive-get>` to an Agent Node.

Other Drive actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="drive-getmany.html">List document libraries</a></div>
