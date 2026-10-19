:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-docs.html">Google Docs</a> › Document</p>

Get a document
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_docs.svg" alt="Google Docs logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Docs</dd></div>
     <div><dt>Resource</dt><dd>Document</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a document's full structure: title, revision id and body content with the start and end index of every paragraph, table and text run.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-docs>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Docs**.
#. **Action:** under **Document**, choose **Get a document**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Google Docs** so later steps can use the columns, then **Save action**.

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
   * - **Document**
     - No
     - The document's id, or its full URL.
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

The records come out as rows, one per record. Click **Load the fields from Google Docs** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Google Docs with this action and start the flow when something new turns up. Pick **Google Docs** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Document changed**
     - Document is the document's URL or id. Reports the document each time it is edited; the connection needs edit access to it, since Google gives the revision only to editors.

Let an agent decide instead
---------------------------

To let an agent call **Get a document** only when a request needs it, add the :doc:`Get a document tool </agentic-ai-guide/tools-integrations/connector-tools/google-docs/document-get>` to an Agent Node.

Other Document actions
----------------------

.. raw:: html

   <div class="tool-related"><a href="document-gettext.html">Read a document as text</a><a href="document-create.html">Create a document</a><a href="document-update.html">Update a document</a></div>
