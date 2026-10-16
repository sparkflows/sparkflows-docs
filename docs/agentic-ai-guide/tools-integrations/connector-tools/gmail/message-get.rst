:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Message</p>

Get a message
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one message as a readable row: from, to, cc, subject, date, received, body text (cut at 6,000 characters), labels, unread, attachment names and its Message-ID header (message-id), which a reply names in inReplyTo. The id comes from Message search or getMany; to read the whole conversation use Thread get.

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
   * - ``messageId``
     - Message
     - text
     - Yes
     - The message id, from Message search or getMany. Example: 18c3f2a9b7d4e1f0.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Columns to keep: id, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments, message-id; blank keeps them all. Example: from,subject,received,snippet.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **get** in the **Message** row. The model sees it as ``gmail_message_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **Get a message**, and fill in the inputs above. It runs every time the flow reaches it.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-search.html">Search messages</a><a href="message-send.html">Send an email</a><a href="message-trash.html">Move a message to trash</a><a href="message-delete.html">Delete a message permanently</a><a href="message-modify.html">Change a message&#x27;s labels</a></div>
