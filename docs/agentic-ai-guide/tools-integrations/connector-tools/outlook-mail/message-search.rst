:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Message</p>

Search emails
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_mail_message_search</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds emails with Outlook's search over sender, recipients, subject, body and attachment names, and returns them in the same columns as Message getMany. Use it to find emails by words or sender; to filter precisely by date or read state, or to sort, use Message getMany with a filter, since search results cannot be sorted.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-mail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Mail** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **search** in the **Message** row, then click **Add to agent**.

The agent now sees ``outlook_mail_message_search`` and calls it when a request needs it.

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
     - The address of the mailbox to search. Example: asha.rao@contoso.com.
   * - ``query``
     - text
     - Yes
     - Outlook's search: words, from:, to:, subject:, hasattachments:yes and received>=2026-09-01, combined with spaces; double quotes mark an exact phrase, as in from:"Asha Rao". Example: invoice from:billing@vendor.com.
   * - ``folder``
     - text
     - No
     - Search only this folder: a well-known name such as inbox or sentitems, or a folder id from Folder getMany; blank searches the whole mailbox.
   * - ``fields``
     - list of text
     - No
     - Columns to keep, from id, conversationId, from, to, cc, subject, receivedDateTime, sentDateTime, preview, body, isRead, isDraft, importance, hasAttachments, categories, webLink and folderId; blank keeps them all. Example: ["from", "subject", "receivedDateTime", "preview"].
   * - ``limit``
     - whole number
     - No
     - How many emails at most. Default: 50.

Need it on every run?
---------------------

To run **Search emails** every time a flow reaches it, without the agent deciding, use the :doc:`Search emails App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail/message-search>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List emails</a><a href="message-get.html">Get an email</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to an email</a><a href="message-replyall.html">Reply to everyone on an email</a><a href="message-forward.html">Forward an email</a><a href="message-update.html">Update an email</a><a href="message-move.html">Move an email to a folder</a><a href="message-delete.html">Delete an email</a><a href="message-createdraft.html">Create a draft email</a></div>
