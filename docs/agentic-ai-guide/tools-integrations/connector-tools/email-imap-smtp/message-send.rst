:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../email-imap-smtp.html">Email (IMAP and SMTP)</a> › Message</p>

Send an email
=============

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

   Sends one plain-text email over SMTP to every address in to and returns sent. All recipients share one To line; there is no Cc, Bcc, HTML or attachment support.

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
   * - ``to``
     - text
     - Yes
     - One or more recipient addresses, separated by commas or semicolons. Example: asha@acme.com, ravi@acme.com.
   * - ``body``
     - text
     - Yes
     - The message text, sent as plain text. Example: Hi Asha,

       The September invoice is attached in the portal.

       Thanks,
       Ravi.
   * - ``subject``
     - text
     - No
     - The subject line; blank sends (no subject). Example: September invoice.
   * - ``fromAddress``
     - text
     - No
     - The From address, which the SMTP server may refuse unless it is the mailbox's own; blank uses the mailbox's login. Example: finance@acme.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Email, IMAP and SMTP**, connect, and tick **send** in the **Message** row. The model sees it as ``mail_tools_message_send``. Each call waits for human approval before it changes anything.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-get.html">Read a message</a><a href="message-search.html">Search messages</a><a href="message-reply.html">Reply to a message</a><a href="message-markread.html">Mark a message as read</a><a href="message-markunread.html">Mark a message as unread</a><a href="message-move.html">Move a message</a><a href="message-delete.html">Delete a message</a><a href="message-flag.html">Flag a message</a></div>
