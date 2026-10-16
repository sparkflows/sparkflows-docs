:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Message</p>

Delete a message permanently
============================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_message_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes one message immediately and permanently, without going through the Trash. It needs the full https://mail.google.com/ scope; use Message trash unless permanent removal was asked for.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.
* The account behind the connection must be allowed to change this data in Gmail.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **delete** in the **Message** row, then click **Add to agent**.

The agent now sees ``gmail_message_delete`` and calls it when a request needs it.

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
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Gmail.

Need it on every run?
---------------------

To run **Delete a message permanently** every time a flow reaches it, without the agent deciding, use the :doc:`Delete a message permanently App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/message-delete>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-get.html">Get a message</a><a href="message-search.html">Search messages</a><a href="message-send.html">Send an email</a><a href="message-trash.html">Move a message to trash</a><a href="message-modify.html">Change a message&#x27;s labels</a></div>
