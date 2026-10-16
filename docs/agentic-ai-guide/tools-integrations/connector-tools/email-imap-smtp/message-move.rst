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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>mail_tools_message_move</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Moves one message from folder to another folder, with UID MOVE where the server offers it and otherwise a copy and a delete, and returns the folder it went to. The message gets a new UID there, which List messages on that folder shows.

Before you start
----------------

* A Email (IMAP and SMTP) connection. See :doc:`how to set one up <../email-imap-smtp>`.
* The account behind the connection must be allowed to change this data in the mailbox.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Email, IMAP and SMTP** under **Connectors** and connect your Email (IMAP and SMTP) connection.
#. Tick **move** in the **Message** row, then click **Add to agent**.

The agent now sees ``mail_tools_message_move`` and calls it when a request needs it.

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

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in the mailbox.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-get.html">Read a message</a><a href="message-search.html">Search messages</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to a message</a><a href="message-markread.html">Mark a message as read</a><a href="message-markunread.html">Mark a message as unread</a><a href="message-delete.html">Delete a message</a><a href="message-flag.html">Flag a message</a></div>
