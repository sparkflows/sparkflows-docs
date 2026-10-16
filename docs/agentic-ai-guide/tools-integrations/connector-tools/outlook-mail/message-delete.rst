:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Message</p>

Delete an email
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Delete · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-mail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes an email; Outlook moves it to the mailbox's Deleted Items folder. Use Message move to file it somewhere else instead.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Outlook Mail prerequisites <../outlook-mail>`.
* The connection's account must be allowed to change this data in Outlook Mail.

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
     - The address of the mailbox the email is in. Example: asha.rao@contoso.com.
   * - ``messageId``
     - Message id
     - text
     - Yes
     - The id of the email to delete, from the id column of Message getMany or Message search. Example: AAMkAGI2TG93AAA=.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Mail**, connect, and tick **delete** in the **Message** row. The model sees it as ``outlook_mail_message_delete``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Mail**, then **Delete an email**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List emails</a><a href="message-get.html">Get an email</a><a href="message-search.html">Search emails</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to an email</a><a href="message-replyall.html">Reply to everyone on an email</a><a href="message-forward.html">Forward an email</a><a href="message-update.html">Update an email</a><a href="message-move.html">Move an email to a folder</a><a href="message-createdraft.html">Create a draft email</a></div>
