:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Message</p>

Create a draft email
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_mail_message_createdraft</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves a new email in the mailbox's Drafts folder without sending it, and returns the draft with its id. Use it when a person should review the email before it goes out; Message send sends at once, and no operation here sends a saved draft.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-mail>`.
* The account behind the connection must be allowed to change this data in Outlook Mail.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Mail** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **createDraft** in the **Message** row, then click **Add to agent**.

The agent now sees ``outlook_mail_message_createdraft`` and calls it when a request needs it.

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
   * - ``mailbox``
     - text
     - Yes
     - The address of the mailbox the draft is saved in. Example: asha.rao@contoso.com.
   * - ``to``
     - list of text
     - No
     - The recipients' email addresses; a draft may have none yet. Example: ["ravi.menon@contoso.com"].
   * - ``cc``
     - list of text
     - No
     - Addresses to copy in.
   * - ``bcc``
     - list of text
     - No
     - Addresses to copy in without the other recipients seeing them.
   * - ``subject``
     - text
     - No
     - The subject line; blank leaves it empty. Example: Draft: vendor payment schedule.
   * - ``body``
     - text
     - No
     - The message as plain text.
   * - ``html``
     - text
     - No
     - The message as HTML; when given it is used instead of body.
   * - ``importance``
     - text
     - No
     - The importance the recipients will see; blank is normal. One of: low, normal, high.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Outlook Mail.

Need it on every run?
---------------------

To run **Create a draft email** every time a flow reaches it, without the agent deciding, use the :doc:`Create a draft email App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail/message-createdraft>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List emails</a><a href="message-get.html">Get an email</a><a href="message-search.html">Search emails</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to an email</a><a href="message-replyall.html">Reply to everyone on an email</a><a href="message-forward.html">Forward an email</a><a href="message-update.html">Update an email</a><a href="message-move.html">Move an email to a folder</a><a href="message-delete.html">Delete an email</a></div>
