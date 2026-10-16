:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-docs.html">Google Docs</a> › Document</p>

Read a document as text
=======================

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

   Returns a document's id, title and its whole text as one plain-text value, table cells included.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-docs>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Docs**.
#. **Action:** under **Document**, choose **Read a document as text**.
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
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

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
   * - **Document text changed**
     - Document is the document's URL or id. Reports the document with its whole text each time its text or title changes, in any tab; formatting-only edits are not reported.
   * - **Text appears in a document**
     - Document is the document's URL or id, and Filter the word or phrase to watch for, for example Approved. Reports the document when the phrase appears in text that did not hold it at the previous check.

Let an agent decide instead
---------------------------

To let an agent call **Read a document as text** only when a request needs it, add the :doc:`Read a document as text tool </agentic-ai-guide/tools-integrations/connector-tools/google-docs/document-gettext>` to an Agent Node.

Other Document actions
----------------------

.. raw:: html

   <div class="tool-related"><a href="document-get.html">Get a document</a><a href="document-create.html">Create a document</a><a href="document-update.html">Update a document</a></div>
