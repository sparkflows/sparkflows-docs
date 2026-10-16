:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-docs.html">Google Docs</a> › Document</p>

Update a document
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

   Edits a document through the Docs batchUpdate API and returns the document id and its new revision. Give text, and optionally index, to insert text; give requests for any other edit, such as appending at the end, replacing placeholder text, formatting or deleting a range.

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
   * - ``document``
     - Document
     - text
     - Yes
     - The document's id, its full URL (https://docs.google.com/document/d/...), or its exact title, which is looked up among the documents pinned on this tool and then in Google Drive. Example: 1mXqB4f0nW8uYt2VZkqzJ3cHd9L5rPoA7sE6gTiKwUbN.
   * - ``text``
     - Text to insert
     - text
     - No
     - The text to insert at index, with a newline character wherever a new paragraph should start. Example: Action items
       Asha to send the revised quote by Friday.
       .
   * - ``index``
     - Insert at index
     - whole number
     - No
     - The position to insert text at: 1 is the very start of the body, and other positions are the startIndex values Get a document returns. Default: 1.
   * - ``requests``
     - Docs API requests
     - JSON object
     - No
     - One Docs API request, or {"requests": [...]} for several applied in order, such as {"replaceAllText": {"containsText": {"text": "{{client}}", "matchCase": true}, "replaceText": "Acme"}}; when it is given, text and index are ignored. Example: {"insertText": {"endOfSegmentLocation": {}, "text": "\\nNext review on 14 Oct."}}.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Docs**, connect, and tick **update** in the **Document** row. The model sees it as ``google_docs_document_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Docs**, then **Update a document**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Document tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="document-get.html">Get a document</a><a href="document-gettext.html">Read a document as text</a><a href="document-create.html">Create a document</a></div>
