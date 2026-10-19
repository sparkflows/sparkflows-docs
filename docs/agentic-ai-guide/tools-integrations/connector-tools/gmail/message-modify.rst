:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Message</p>

Change a message's labels
=========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_message_modify</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Adds or removes labels on one message and returns its new labelIds. Removing UNREAD marks it read, adding UNREAD marks it unread, removing INBOX archives it and adding STARRED stars it.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.
* The account behind the connection must be allowed to change this data in Gmail.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **modify** in the **Message** row, then click **Add to agent**.

The agent now sees ``gmail_message_modify`` and calls it when a request needs it.

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
     - The message id, from Message search or getMany. Example: 18c3f2a9b7d4e1f0.
   * - ``addLabelIds``
     - list of text
     - No
     - Label ids to add, for example ["STARRED"] or a user label id such as Label\_3 from Label getMany.
   * - ``removeLabelIds``
     - list of text
     - No
     - Label ids to remove, for example ["UNREAD"] to mark it read or ["INBOX"] to archive it.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Gmail.

Need it on every run?
---------------------

To run **Change a message's labels** every time a flow reaches it, without the agent deciding, use the :doc:`Change a message's labels App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/message-modify>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-get.html">Get a message</a><a href="message-search.html">Search messages</a><a href="message-send.html">Send an email</a><a href="message-trash.html">Move a message to trash</a><a href="message-delete.html">Delete a message permanently</a></div>
