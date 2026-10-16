:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-docs.html">Google Docs</a> › Document</p>

Create a document
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_docs.svg" alt="Google Docs logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Docs</dd></div>
     <div><dt>Resource</dt><dd>Document</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_docs_document_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an empty document with the given title in the connection's Google Drive and returns its documentId and link. A new document cannot carry text, so add the content afterwards with Update a document.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-docs>`.
* The account behind the connection must be allowed to change this data in Google Docs.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Docs** under **Connectors** and connect your Google connection.
#. Tick **create** in the **Document** row, then click **Add to agent**.

The agent now sees ``google_docs_document_create`` and calls it when a request needs it.

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
     - The new document's title. Example: Meeting notes - 30 Sep 2026.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Docs.

Need it on every run?
---------------------

To run **Create a document** every time a flow reaches it, without the agent deciding, use the :doc:`Create a document App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-docs/document-create>`.

Other Document tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="document-get.html">Get a document</a><a href="document-gettext.html">Read a document as text</a><a href="document-update.html">Update a document</a></div>
