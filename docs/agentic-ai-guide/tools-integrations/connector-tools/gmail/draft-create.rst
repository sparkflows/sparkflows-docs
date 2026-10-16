:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Draft</p>

Create a draft
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Draft</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves an email as a draft without sending it and returns the draft id with its message id. Use it when a person should check the email first; Draft send sends it later, and Message send sends straight away.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Gmail prerequisites <../gmail>`.
* The connection's account must be allowed to change this data in Gmail.

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
   * - ``to``
     - To
     - list of text
     - Yes
     - Recipient addresses, for example ["asha@example.com"]; a comma-separated text works too.
   * - ``subject``
     - Subject
     - text
     - No
     - The subject line; blank sends (no subject). For a reply keep the original subject after Re:. Example: Invoice 1042.
   * - ``body``
     - Body
     - text
     - No
     - The plain-text body of the email. Example: Hi Asha, the invoice is attached to the portal..
   * - ``cc``
     - Cc
     - list of text
     - No
     - Addresses to copy. Example: ravi@example.com.
   * - ``bcc``
     - Bcc
     - list of text
     - No
     - Addresses to copy without the other recipients seeing them.
   * - ``html``
     - HTML body
     - text
     - No
     - An HTML version of the body, shown by mail clients that display HTML; body stays the plain-text version.
   * - ``threadId``
     - Reply in thread
     - text
     - No
     - The threadId of the conversation to reply in, from Message get or search. Example: 18c3f2a9b7d4e1f0.
   * - ``inReplyTo``
     - In reply to
     - text
     - No
     - The Message-ID header of the email being answered, from the message-id column of Message get or search, so other mail clients thread the reply too. Example: <CAF1a2b3c@mail.gmail.com>.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **create** in the **Draft** row. The model sees it as ``gmail_draft_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **Create a draft**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Draft tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="draft-getmany.html">List drafts</a><a href="draft-get.html">Get a draft</a><a href="draft-send.html">Send a draft</a><a href="draft-delete.html">Delete a draft</a></div>
