:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Message</p>

Get an email
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_mail_message_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one email by its id, with sender, recipients, subject, dates, flags and the body as plain text cut at 6000 characters. Use it when the id is already known from Message getMany or Message search.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-mail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Mail** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Message** row, then click **Add to agent**.

The agent now sees ``outlook_mail_message_get`` and calls it when a request needs it.

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
     - The address of the mailbox the email is in. Example: asha.rao@contoso.com.
   * - ``messageId``
     - text
     - Yes
     - The id of the email, from the id column of Message getMany or Message search. Example: AAMkAGI2TG93AAA=.
   * - ``fields``
     - list of text
     - No
     - Columns to keep, from id, conversationId, from, to, cc, subject, receivedDateTime, sentDateTime, preview, body, isRead, isDraft, importance, hasAttachments, categories, webLink and folderId; blank keeps them all. Example: ["from", "subject", "body"].

Need it on every run?
---------------------

To run **Get an email** every time a flow reaches it, without the agent deciding, use the :doc:`Get an email App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail/message-get>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List emails</a><a href="message-search.html">Search emails</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to an email</a><a href="message-replyall.html">Reply to everyone on an email</a><a href="message-forward.html">Forward an email</a><a href="message-update.html">Update an email</a><a href="message-move.html">Move an email to a folder</a><a href="message-delete.html">Delete an email</a><a href="message-createdraft.html">Create a draft email</a></div>
