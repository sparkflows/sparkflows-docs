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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-docs.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an empty document with the given title in the connection's Google Drive and returns its documentId and link. A new document cannot carry text, so add the content afterwards with Update a document.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Docs prerequisites <../google-docs>`.
* The connection's account must be allowed to change this data in Google Docs.

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
   * - ``title``
     - Title
     - text
     - Yes
     - The new document's title. Example: Meeting notes - 30 Sep 2026.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Docs**, connect, and tick **create** in the **Document** row. The model sees it as ``google_docs_document_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Docs**, then **Create a document**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Document tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="document-get.html">Get a document</a><a href="document-gettext.html">Read a document as text</a><a href="document-update.html">Update a document</a></div>
