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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_docs_document_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Edits a document through the Docs batchUpdate API and returns the document id and its new revision. Give text, and optionally index, to insert text; give requests for any other edit, such as appending at the end, replacing placeholder text, formatting or deleting a range.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-docs>`.
* The account behind the connection must be allowed to change this data in Google Docs.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Docs** under **Connectors** and connect your Google connection.
#. Tick **update** in the **Document** row, then click **Add to agent**.

The agent now sees ``google_docs_document_update`` and calls it when a request needs it.

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
   * - ``text``
     - text
     - No
     - The text to insert at index, with a newline character wherever a new paragraph should start. Example: Action items
       Asha to send the revised quote by Friday.
       .
   * - ``index``
     - whole number
     - No
     - The position to insert text at: 1 is the very start of the body, and other positions are the startIndex values Get a document returns. Default: 1.
   * - ``requests``
     - JSON object
     - No
     - One Docs API request, or {"requests": [...]} for several applied in order, such as {"replaceAllText": {"containsText": {"text": "{{client}}", "matchCase": true}, "replaceText": "Acme"}}; when it is given, text and index are ignored. Example: {"insertText": {"endOfSegmentLocation": {}, "text": "\\nNext review on 14 Oct."}}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Docs.

Need it on every run?
---------------------

To run **Update a document** every time a flow reaches it, without the agent deciding, use the :doc:`Update a document App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-docs/document-update>`.

Other Document tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="document-get.html">Get a document</a><a href="document-gettext.html">Read a document as text</a><a href="document-create.html">Create a document</a></div>
