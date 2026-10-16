:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Message</p>

Search messages
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_message_search</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds messages with Gmail's search syntax and returns them as readable rows, newest first: from, to, subject, received, snippet, body text, labels, unread and attachment names. Use it whenever a request names a sender, subject, date range, label or words; Message getMany only lists the latest mail.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **search** in the **Message** row, then click **Add to agent**.

The agent now sees ``gmail_message_search`` and calls it when a request needs it.

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
   * - ``query``
     - text
     - Yes
     - Gmail search box syntax: from:, to:, subject:, is:unread, has:attachment, label:Work, after:2026/09/01, newer\_than:7d; combine terms with spaces, OR, and - to exclude. Example: from:boss@company.com newer\_than:7d.
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

To run **Search messages** every time a flow reaches it, without the agent deciding, use the :doc:`Search messages App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/message-search>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-get.html">Get a message</a><a href="message-send.html">Send an email</a><a href="message-trash.html">Move a message to trash</a><a href="message-delete.html">Delete a message permanently</a><a href="message-modify.html">Change a message&#x27;s labels</a></div>
