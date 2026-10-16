:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-docs.html">Google Docs</a> › Document</p>

Get a document
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_docs.svg" alt="Google Docs logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Docs</dd></div>
     <div><dt>Resource</dt><dd>Document</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>google_docs_document_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a document's full structure: title, revision id and body content with the start and end index of every paragraph, table and text run. Use it only when those indices are needed to edit at a given position; Read a document as text is far smaller for reading.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-docs>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Docs** under **Connectors** and connect your Google connection.
#. Tick **get** in the **Document** row, then click **Add to agent**.

The agent now sees ``google_docs_document_get`` and calls it when a request needs it.

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
   * - ``document``
     - text
     - Yes
     - The document's id, its full URL (https://docs.google.com/document/d/...), or its exact title, which is looked up among the documents pinned on this tool and then in Google Drive. Example: 1mXqB4f0nW8uYt2VZkqzJ3cHd9L5rPoA7sE6gTiKwUbN.

Need it on every run?
---------------------

To run **Get a document** every time a flow reaches it, without the agent deciding, use the :doc:`Get a document App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-docs/document-get>`.

Other Document tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="document-gettext.html">Read a document as text</a><a href="document-create.html">Create a document</a><a href="document-update.html">Update a document</a></div>
