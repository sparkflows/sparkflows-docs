.. _connector-tools-outlook-mail:

.. rst-class:: agentic-tutorial

Outlook Mail Tools
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connection</dt><dd>Microsoft Graph</dd></div>
     <div><dt>Tools</dt><dd>18 across 3 resources</dd></div>
     <div><dt>Reads / writes</dt><dd>8 / 10</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · App Action</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Let an agent work with Microsoft 365 mailboxes: list, search and read email, reply, reply all, forward, draft, move and flag messages, and read or save attachments.

.. contents:: On this page
   :local:
   :depth: 1
   :class: tool-toc

Prerequisites
-------------

* **Connection:** A **Microsoft Graph** connection: an Entra ID app registration with its tenant ID, client ID and client secret, and the Microsoft Graph **application** permissions below granted with admin consent.
* ``Mail.Read`` to read and ``Mail.ReadWrite`` to draft, move, flag or delete; ``Mail.Send`` to send, reply and forward.
* Every tool takes a ``mailbox`` (a user's address). With application permissions the app can reach any mailbox in the tenant unless an Exchange application access policy limits it; fix ``mailbox`` in **Fixed settings** to keep the agent on one.

Add Outlook Mail to an agent
----------------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node on the canvas.
#. Choose **Outlook Mail** under **Connectors**, or type ``outlook`` in the search box.
#. **Connect.** Choose your Microsoft Graph connection and click **Test connection**. The rest of the screen unlocks when it shows **Connected**.
#. **How the agent sees it.** Keep **A separate tool for each one**, so the agent picks each operation by name.
#. **Tick the operations.** The grid opens with the **Look things up** pack: reads only. Add each write the agent needs; every write waits for approval when it runs.
#. Click **Add to agent**. The ticked operations arrive as one Outlook Mail node, joined to the Agent Node by a dashed tool link.

.. figure:: ../../../_assets/agentic-ai-guide/tools/connectors/outlook-mail-connected.png
   :alt: Outlook Mail connected, with the connector card and its tool count
   :width: 100%

   Connected: the tested connection, the Outlook Mail card with how many tools are ticked.

.. figure:: ../../../_assets/agentic-ai-guide/tools/connectors/outlook-mail-tools.png
   :alt: The Outlook Mail operations grid
   :width: 100%

   What the agent may do in Outlook Mail. Blue ticks are the **Look things up** pack; dashed boxes are writes, and a red dot marks an action that writes.

Tools
-----

Each ticked operation becomes one tool, named ``outlook_mail_<resource>_<operation>``. **Read** tools run straight away. **Write** and **Delete** tools change data in Outlook Mail, so each call waits for :doc:`human approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it takes effect. Click a tool to open its page with every parameter.

.. raw:: html

   <nav class="tool-jump" aria-label="Jump to a resource"><a href="#res-message">Message<span>11</span></a><a href="#res-folder">Folder<span>5</span></a><a href="#res-attachment">Attachment<span>2</span></a></nav>

.. raw:: html

   <span id="res-message" class="tool-anchor"></span>

Message
~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="outlook-mail/message-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List emails</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the emails in a mailbox or in one of its folders, with sender, recipients, subject, dates, read state and the body as plain text cut at 6000 characters.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get an email</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one email by its id, with sender, recipients, subject, dates, flags and the body as plain text cut at 6000 characters.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-search.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Search emails</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Finds emails with Outlook&#x27;s search over sender, recipients, subject, body and attachment names, and returns them in the same columns as Message getMany.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-send.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Send an email</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Sends a new email from the mailbox and keeps a copy in its Sent Items.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-reply.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Reply to an email</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Replies to the sender of an email in the same conversation, with the reply text above the quoted original.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-replyall.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Reply to everyone on an email</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Replies to the sender and every other recipient of an email in the same conversation, with the reply text above the quoted original.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-forward.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Forward an email</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Forwards an email, attachments included, to other people with an optional note above it.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-update.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Update an email</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Changes an email&#x27;s read state, importance, categories or follow-up flag and returns the updated email.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-move.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Move an email to a folder</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Moves an email to another folder and returns it; the moved email has a new id.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete an email</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes an email; Outlook moves it to the mailbox&#x27;s Deleted Items folder.</span>
     </a>
     <a class="tool-op" href="outlook-mail/message-createdraft.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a draft email</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Saves a new email in the mailbox&#x27;s Drafts folder without sending it, and returns the draft with its id.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-folder" class="tool-anchor"></span>

Folder
~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="outlook-mail/folder-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List mail folders</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the top-level mail folders of a mailbox with their ids, names and unread and total counts; child folders are not included.</span>
     </a>
     <a class="tool-op" href="outlook-mail/folder-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a mail folder</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one mail folder with its id, name, parent and unread, total and child folder counts.</span>
     </a>
     <a class="tool-op" href="outlook-mail/folder-getmessages.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List the emails in a folder</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the emails inside one mail folder, named by a well-known name or its id, as Microsoft Graph returns them: subject, sender, recipients, dates, read state and a preview.</span>
     </a>
     <a class="tool-op" href="outlook-mail/folder-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a mail folder</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Creates a mail folder at the top level of the mailbox and returns it with its id.</span>
     </a>
     <a class="tool-op" href="outlook-mail/folder-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a mail folder</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes a mail folder together with the emails in it.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-attachment" class="tool-anchor"></span>

Attachment
~~~~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="outlook-mail/attachment-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Read email attachments</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Saves the attachments of one or more emails to the engine&#x27;s disk and returns one row per file: the email it came in, the file name, type and size, the saved path, and with extractText the file&#x27;s text, text_status and text_source.</span>
     </a>
     <a class="tool-op" href="outlook-mail/attachment-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Read one email attachment</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Saves one attachment to the engine&#x27;s disk and returns it as one row with its email, name, type, size, saved path and, with extractText, its text, text_status and text_source, read the same way Attachment getMany reads them.</span>
     </a>
   </div>

Use Outlook Mail as an App Action
---------------------------------

Outlook Mail also has 19 App Actions, fixed workflow steps for the same work. Drop **App Action** on the canvas, pick **Outlook Mail**, choose the action and fill in its details. It runs every time the flow reaches it, exactly as set; no model decides. Use it for the steps that must always happen, such as saving an approved result, and keep the agent tool for what the model should choose. See :doc:`Outlook Mail App Actions </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail>` for every action, its inputs and the trigger events.

Good to know
------------

* Bodies come back as plain text cut at 6,000 characters.
* **Search emails** uses Outlook search over sender, recipients, subject, body and attachment names; **List emails** takes an OData filter for exact dates, read state or sender.
* **Create a draft email** leaves the email in Drafts for a person to send; no tool here sends a saved draft.
* **Delete an email** moves it to Deleted Items. A moved email gets a new id.

Example
-------

**Triage a shared mailbox.** Fix mailbox = support@contoso.com; tick reads, Update an email and Create a draft email. Then give the Agent Node instructions like these:

.. code-block:: text

   List unread emails in the Inbox from the last 24 hours.
   For each, decide billing, technical or other and mark it with that category.
   Create a draft reply for billing emails only. Never send.

Other common uses:

* Triage a shared support mailbox into categories.
* Draft replies for a person to review in Outlook.
* Save invoice attachments for downstream processing.

Troubleshooting
---------------

***Access is denied* or HTTP 403.**
   The app registration lacks the Graph permission for that tool, or admin consent was not granted after adding it.

***The mailbox is either inactive, soft-deleted, or is hosted on-premise*.**
   The ``mailbox`` address has no Exchange Online mailbox. Use the user's primary SMTP address.

**The agent does not call the tool, or picks the wrong one.**
   Name the tool in the instructions and untick operations that sound alike. See :ref:`making-tools-reliable`.

FAQ
---

**Can I use an IMAP mailbox instead?**
   Yes, with the :doc:`Email (IMAP and SMTP) <email-imap-smtp>` connector. For Microsoft 365 mailboxes, Outlook Mail is the better fit.

Related
-------

* :doc:`/agentic-ai-guide/tools-integrations/tools-connectors` - how tools work, choosing operations, and fixed settings
* :doc:`/agentic-ai-guide/tools-integrations/connector-tools/index` - every connector
* :doc:`/agentic-ai-guide/safety-guardrails/human-in-the-loop` - approving writes
* :doc:`/agentic-ai-guide/tools-integrations/app-actions` - the same operations as fixed workflow steps
