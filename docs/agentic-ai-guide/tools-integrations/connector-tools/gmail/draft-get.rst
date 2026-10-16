:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Draft</p>

Get a draft
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Draft</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one draft as a readable row: the draft id, messageId, to, cc, subject and body text. Draft ids come from Draft getMany or Draft create.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Gmail prerequisites <../gmail>`.

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
   * - ``draftId``
     - Draft
     - text
     - Yes
     - The draft id, from Draft getMany or Draft create. Example: r-5843521846237418962.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Columns to keep: id, messageId, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments, message-id; blank keeps them all. Example: from,subject,received,snippet.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **get** in the **Draft** row. The model sees it as ``gmail_draft_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **Get a draft**, and fill in the inputs above. It runs every time the flow reaches it.

Other Draft tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="draft-getmany.html">List drafts</a><a href="draft-create.html">Create a draft</a><a href="draft-send.html">Send a draft</a><a href="draft-delete.html">Delete a draft</a></div>
