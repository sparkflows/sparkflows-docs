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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_draft_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves an email as a draft without sending it and returns the draft id with its message id. Use it when a person should check the email first; Draft send sends it later, and Message send sends straight away.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.
* The account behind the connection must be allowed to change this data in Gmail.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **create** in the **Draft** row, then click **Add to agent**.

The agent now sees ``gmail_draft_create`` and calls it when a request needs it.

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
   * - ``to``
     - list of text
     - Yes
     - Recipient addresses, for example ["asha@example.com"]; a comma-separated text works too.
   * - ``subject``
     - text
     - No
     - The subject line; blank sends (no subject). For a reply keep the original subject after Re:. Example: Invoice 1042.
   * - ``body``
     - text
     - No
     - The plain-text body of the email. Example: Hi Asha, the invoice is attached to the portal..
   * - ``cc``
     - list of text
     - No
     - Addresses to copy. Example: ravi@example.com.
   * - ``bcc``
     - list of text
     - No
     - Addresses to copy without the other recipients seeing them.
   * - ``html``
     - text
     - No
     - An HTML version of the body, shown by mail clients that display HTML; body stays the plain-text version.
   * - ``threadId``
     - text
     - No
     - The threadId of the conversation to reply in, from Message get or search. Example: 18c3f2a9b7d4e1f0.
   * - ``inReplyTo``
     - text
     - No
     - The Message-ID header of the email being answered, from the message-id column of Message get or search, so other mail clients thread the reply too. Example: <CAF1a2b3c@mail.gmail.com>.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Gmail.

Need it on every run?
---------------------

To run **Create a draft** every time a flow reaches it, without the agent deciding, use the :doc:`Create a draft App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/draft-create>`.

Other Draft tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="draft-getmany.html">List drafts</a><a href="draft-get.html">Get a draft</a><a href="draft-send.html">Send a draft</a><a href="draft-delete.html">Delete a draft</a></div>
