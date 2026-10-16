:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../email-imap-smtp.html">Email (IMAP and SMTP)</a> › Message</p>

Search messages
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mail_tools.svg" alt="Email (IMAP and SMTP) logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Email (IMAP and SMTP)</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>mail_tools_message_search</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds the messages in a folder that match IMAP search criteria and returns them newest first, with the same columns as List messages. Reading leaves each message's read state as it was. Blank criteria match every message.

Before you start
----------------

* A Email (IMAP and SMTP) connection. See :doc:`how to set one up <../email-imap-smtp>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Email, IMAP and SMTP** under **Connectors** and connect your Email (IMAP and SMTP) connection.
#. Tick **search** in the **Message** row, then click **Add to agent**.

The agent now sees ``mail_tools_message_search`` and calls it when a request needs it.

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
   * - ``criteria``
     - text
     - No
     - IMAP SEARCH criteria, space-separated for AND, such as UNSEEN, FROM "a@b.com", SUBJECT "invoice", SINCE 01-Sep-2026 or OR FROM "a@b.com" FROM "c@d.com"; blank means ALL. Example: UNSEEN FROM "billing@vendor.com".
   * - ``folder``
     - text
     - No
     - The folder to work in, as List folders names it, for example INBOX or [Gmail]/All Mail; blank means INBOX.
   * - ``includeBody``
     - true or false
     - No
     - false leaves the body column out; the whole message is still downloaded. Default: True.
   * - ``limit``
     - whole number
     - No
     - How many messages at most, newest first. Default: 20.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-get.html">Read a message</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to a message</a><a href="message-markread.html">Mark a message as read</a><a href="message-markunread.html">Mark a message as unread</a><a href="message-move.html">Move a message</a><a href="message-delete.html">Delete a message</a><a href="message-flag.html">Flag a message</a></div>
