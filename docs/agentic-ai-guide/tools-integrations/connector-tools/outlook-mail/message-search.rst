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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-mail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds emails with Outlook's search over sender, recipients, subject, body and attachment names, and returns them in the same columns as Message getMany. Use it to find emails by words or sender; to filter precisely by date or read state, or to sort, use Message getMany with a filter, since search results cannot be sorted.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Outlook Mail prerequisites <../outlook-mail>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``mailbox``
     - Mailbox
     - text
     - Yes
     - The address of the mailbox to search. Example: asha.rao@contoso.com.
   * - ``query``
     - Search text
     - text
     - Yes
     - Outlook's search: words, from:, to:, subject:, hasattachments:yes and received>=2026-09-01, combined with spaces; double quotes mark an exact phrase, as in from:"Asha Rao". Example: invoice from:billing@vendor.com.
   * - ``folder``
     - Folder
     - text
     - No
     - Search only this folder: a well-known name such as inbox or sentitems, or a folder id from Folder getMany; blank searches the whole mailbox.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Columns to keep, from id, conversationId, from, to, cc, subject, receivedDateTime, sentDateTime, preview, body, isRead, isDraft, importance, hasAttachments, categories, webLink and folderId; blank keeps them all. Example: ["from", "subject", "receivedDateTime", "preview"].
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many emails at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Mail**, connect, and tick **search** in the **Message** row. The model sees it as ``outlook_mail_message_search``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Mail**, then **Search emails**, and fill in the inputs above. It runs every time the flow reaches it.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List emails</a><a href="message-get.html">Get an email</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to an email</a><a href="message-replyall.html">Reply to everyone on an email</a><a href="message-forward.html">Forward an email</a><a href="message-update.html">Update an email</a><a href="message-move.html">Move an email to a folder</a><a href="message-delete.html">Delete an email</a><a href="message-createdraft.html">Create a draft email</a></div>
