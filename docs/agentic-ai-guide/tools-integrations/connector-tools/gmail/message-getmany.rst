:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Message</p>

List messages
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_message_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the latest messages in the mailbox, newest first, as readable rows: id, threadId, from, to, subject, received, snippet, body text (cut at 6,000 characters), labels, unread and attachment names. Use labelIds for one folder such as INBOX; when a request names a sender, subject, date or words use Message search instead.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Message** row, then click **Add to agent**.

The agent now sees ``gmail_message_getmany`` and calls it when a request needs it.

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
   * - ``labelIds``
     - list of text
     - No
     - Only messages that carry all of these label ids, for example ["INBOX"] or ["INBOX", "UNREAD"]; Label getMany lists user label ids.
   * - ``fields``
     - list of text
     - No
     - Columns to keep: id, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments, message-id; blank keeps them all. Example: from,subject,received,snippet.
   * - ``limit``
     - whole number
     - No
     - How many messages at most; each one is read in full, so keep it small. Default: 10.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Need it on every run?
---------------------

To run **List messages** every time a flow reaches it, without the agent deciding, use the :doc:`List messages App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/message-getmany>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-get.html">Get a message</a><a href="message-search.html">Search messages</a><a href="message-send.html">Send an email</a><a href="message-trash.html">Move a message to trash</a><a href="message-delete.html">Delete a message permanently</a><a href="message-modify.html">Change a message&#x27;s labels</a></div>
