:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../email-imap-smtp.html">Email (IMAP and SMTP)</a> › Message</p>

Move a message
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mail_tools.svg" alt="Email (IMAP and SMTP) logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Email (IMAP and SMTP)</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Moves one message from folder to another folder, with UID MOVE where the server offers it and otherwise a copy and a delete, and returns the folder it went to. The message gets a new UID there, which List messages on that folder shows.

Prerequisites
-------------

* **Connection:** Email (IMAP and SMTP) connection. See :doc:`the Email (IMAP and SMTP) prerequisites <../email-imap-smtp>`.
* The connection's account must be allowed to change this data in Email (IMAP and SMTP).

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - Description
   * - ``messageId``
     - text
     - Yes
     - The UID in the uid column of List messages or Search messages, which stays the same while the message stays in its folder. Example: 4821.
   * - ``destinationFolder``
     - text
     - Yes
     - The folder to move the message to, as List folders names it. Example: Archive.
   * - ``folder``
     - text
     - No
     - The folder the message is in now, as List folders names it; blank means INBOX.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Email, IMAP and SMTP**, connect, and tick **move** in the **Message** row. The model sees it as ``mail_tools_message_move``. Each call waits for human approval before it changes anything.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-get.html">Read a message</a><a href="message-search.html">Search messages</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to a message</a><a href="message-markread.html">Mark a message as read</a><a href="message-markunread.html">Mark a message as unread</a><a href="message-delete.html">Delete a message</a><a href="message-flag.html">Flag a message</a></div>
