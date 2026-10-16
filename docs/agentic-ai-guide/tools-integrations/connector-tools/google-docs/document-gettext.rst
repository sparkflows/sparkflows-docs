:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-docs.html">Google Docs</a> › Document</p>

Read a document as text
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_docs.svg" alt="Google Docs logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Docs</dd></div>
     <div><dt>Resource</dt><dd>Document</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-docs.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a document's id, title and its whole text as one plain-text value, table cells included. Use it to read, quote or summarise a document; use Get a document only for the indices an edit needs.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Docs prerequisites <../google-docs>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``document``
     - Document
     - text
     - Yes
     - The document's id, its full URL (https://docs.google.com/document/d/...), or its exact title, which is looked up among the documents pinned on this tool and then in Google Drive. Example: 1mXqB4f0nW8uYt2VZkqzJ3cHd9L5rPoA7sE6gTiKwUbN.
   * - ``includeTabsContent``
     - Read every tab
     - true or false
     - No
     - true reads the text of every tab of a document that has tabs; false reads only the first tab. Default: True.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Docs**, connect, and tick **getText** in the **Document** row. The model sees it as ``google_docs_document_gettext``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Docs**, then **Read a document as text**, and fill in the inputs above. It runs every time the flow reaches it.

Other Document tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="document-get.html">Get a document</a><a href="document-create.html">Create a document</a><a href="document-update.html">Update a document</a></div>
