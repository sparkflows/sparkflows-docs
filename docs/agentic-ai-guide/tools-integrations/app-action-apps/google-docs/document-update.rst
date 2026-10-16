:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-docs.html">Google Docs</a> › Document</p>

Update a document
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_docs.svg" alt="Google Docs logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Docs</dd></div>
     <div><dt>Resource</dt><dd>Document</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Edits a document through the Docs batchUpdate API and returns the document id and its new revision.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-docs>`.
* The account behind the connection must be allowed to change this data in Google Docs.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Docs**.
#. **Action:** under **Document**, choose **Update a document**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Save action**.

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

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **If a row is rejected**
     - No
     - stop fails the run at the first rejected row. continue writes the rest and marks that row failed in result\_status and result\_error. Choices: ``stop``, ``continue``. Default: ``stop``.

Fields to set
-------------

Each row that arrives is written to Google Docs. When its columns already have these names, leave **Fields to set** empty. Otherwise click the chip of a field to add it, then type its value or click one under **What arrives here**.

.. list-table::
   :header-rows: 1
   :widths: 24 22 54
   :class: tool-params

   * - Field
     - Column name
     - Example or hint
   * - **Text to insert**
     - ``insertText.text``
     - ``Action items Asha to send the revised quote by Friday.``
   * - **Insert at index**
     - ``insertText.location.index``
     - ``1``

What it passes on
-----------------

Every row comes out with three columns added, so the next step can route on them:

.. list-table::
   :header-rows: 1
   :widths: 26 74
   :class: tool-table

   * - Column
     - Value
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``
   * - ``result_id``
     - The id Google Docs gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Update a document** only when a request needs it, add the :doc:`Update a document tool </agentic-ai-guide/tools-integrations/connector-tools/google-docs/document-update>` to an Agent Node.

Other Document actions
----------------------

.. raw:: html

   <div class="tool-related"><a href="document-get.html">Get a document</a><a href="document-gettext.html">Read a document as text</a><a href="document-create.html">Create a document</a></div>
