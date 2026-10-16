.. _connector-tools-gmail:

.. rst-class:: agentic-tutorial

Gmail Tools
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connection</dt><dd>Google</dd></div>
     <div><dt>Tools</dt><dd>22 across 5 resources</dd></div>
     <div><dt>Reads / writes</dt><dd>11 / 11</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · App Action</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Let an agent read, search and send email in a Gmail mailbox: list and search messages with Gmail's search syntax, read whole threads, draft or send replies, manage labels, and save attachments for other tools to read.

.. contents:: On this page
   :local:
   :depth: 1
   :class: tool-toc

Prerequisites
-------------

* **Connection:** A **Google** connection: a client ID, client secret and refresh token from a Google Cloud OAuth client. One Google connection serves Gmail, Calendar, Docs, Drive and Sheets; the scopes on its refresh token decide which of them it can reach.
* The **Gmail API** enabled in the Google Cloud project behind the connection.
* A refresh token with ``https://www.googleapis.com/auth/gmail.readonly`` for the read tools, or ``gmail.modify`` plus ``gmail.send`` to draft, send, label and trash. **Delete a message permanently** needs the full ``https://mail.google.com/`` scope.

Add Gmail to an agent
---------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node on the canvas.
#. Choose **Gmail** under **Connectors**, or type ``gmail`` in the search box.
#. **Connect.** Choose your Google connection and click **Test connection**. The rest of the screen unlocks when it shows **Connected**.
#. **How the agent sees it.** Keep **A separate tool for each one**, so the agent picks each operation by name.
#. **Tick the operations.** The grid opens with the **Look things up** pack: reads only. Add each write the agent needs; every write waits for approval when it runs.
#. Click **Add to agent**. The ticked operations arrive as one Gmail node, joined to the Agent Node by a dashed tool link.

.. figure:: ../../../_assets/agentic-ai-guide/tools/connectors/gmail-connected.png
   :alt: Gmail connected, with the connector card and its tool count
   :width: 100%

   Connected: the tested connection, the Gmail card with how many tools are ticked.

.. figure:: ../../../_assets/agentic-ai-guide/tools/connectors/gmail-tools.png
   :alt: The Gmail operations grid
   :width: 100%

   What the agent may do in Gmail. Blue ticks are the **Look things up** pack; dashed boxes are writes, and a red dot marks an action that writes.

Tools
-----

Each ticked operation becomes one tool, named ``gmail_<resource>_<operation>``. **Read** tools run straight away. **Write** and **Delete** tools change data in Gmail, so each call waits for :doc:`human approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it takes effect. Click a tool to open its page with every parameter.

.. raw:: html

   <nav class="tool-jump" aria-label="Jump to a resource"><a href="#res-message">Message<span>7</span></a><a href="#res-draft">Draft<span>5</span></a><a href="#res-label">Label<span>5</span></a><a href="#res-attachment">Attachment<span>2</span></a><a href="#res-thread">Thread<span>3</span></a></nav>

.. raw:: html

   <span id="res-message" class="tool-anchor"></span>

Message
~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="gmail/message-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List messages</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the latest messages in the mailbox, newest first, as readable rows: id, threadId, from, to, subject, received, snippet, body text (cut at 6,000 characters), labels, unread and attachment names.</span>
     </a>
     <a class="tool-op" href="gmail/message-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a message</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one message as a readable row: from, to, cc, subject, date, received, body text (cut at 6,000 characters), labels, unread, attachment names and its Message-ID header (message-id), which a reply names in inReplyTo.</span>
     </a>
     <a class="tool-op" href="gmail/message-search.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Search messages</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Finds messages with Gmail&#x27;s search syntax and returns them as readable rows, newest first: from, to, subject, received, snippet, body text, labels, unread and attachment names.</span>
     </a>
     <a class="tool-op" href="gmail/message-send.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Send an email</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Sends an email from the mailbox and returns the sent message&#x27;s id, threadId and labelIds.</span>
     </a>
     <a class="tool-op" href="gmail/message-trash.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Move a message to trash</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Moves one message to the Trash, where Gmail deletes it for good after 30 days, and returns it with its new labelIds.</span>
     </a>
     <a class="tool-op" href="gmail/message-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a message permanently</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes one message immediately and permanently, without going through the Trash.</span>
     </a>
     <a class="tool-op" href="gmail/message-modify.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Change a message&#x27;s labels</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Adds or removes labels on one message and returns its new labelIds.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-draft" class="tool-anchor"></span>

Draft
~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="gmail/draft-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List drafts</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the drafts in the mailbox as readable rows: the draft id, messageId, to, cc, subject, snippet and body text.</span>
     </a>
     <a class="tool-op" href="gmail/draft-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a draft</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one draft as a readable row: the draft id, messageId, to, cc, subject and body text.</span>
     </a>
     <a class="tool-op" href="gmail/draft-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a draft</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Saves an email as a draft without sending it and returns the draft id with its message id.</span>
     </a>
     <a class="tool-op" href="gmail/draft-send.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Send a draft</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Sends a saved draft as it stands and returns the sent message&#x27;s id, threadId and labelIds; the draft itself is removed.</span>
     </a>
     <a class="tool-op" href="gmail/draft-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a draft</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes a draft immediately and permanently; it does not go to the Trash.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-label" class="tool-anchor"></span>

Label
~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="gmail/label-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List labels</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the mailbox&#x27;s labels with id, name and type (system or user), without any message counts.</span>
     </a>
     <a class="tool-op" href="gmail/label-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a label with counts</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one label with exact counts: messagesTotal, messagesUnread, threadsTotal and threadsUnread.</span>
     </a>
     <a class="tool-op" href="gmail/label-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a label</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Creates a user label and returns it with its id (Label_...).</span>
     </a>
     <a class="tool-op" href="gmail/label-update.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Update a label</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Renames a user label or changes its visibility or colors, and returns the updated label.</span>
     </a>
     <a class="tool-op" href="gmail/label-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a label</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes a user label for good and removes it from every message and thread that carries it; the messages themselves stay.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-attachment" class="tool-anchor"></span>

Attachment
~~~~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="gmail/attachment-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Read attachments</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Saves the attachments of one or more emails to the engine&#x27;s disk and returns one row per file: messageId, from, subject, received, filename, extension, mimeType, size, path and, with extractText, the file&#x27;s text, text_status and text_source.</span>
     </a>
     <a class="tool-op" href="gmail/attachment-download.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Download attachments</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Saves the attachments of one or more emails into a folder on the engine&#x27;s disk, without reading them, and returns one row per file: messageId, from, subject, received, filename, extension, mimeType, size, path (where the file was saved) and save_status (saved, or skipped when the file was already there).</span>
     </a>
   </div>

.. raw:: html

   <span id="res-thread" class="tool-anchor"></span>

Thread
~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="gmail/thread-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List threads</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists conversation threads, newest first, with each thread&#x27;s id and a snippet of its latest message.</span>
     </a>
     <a class="tool-op" href="gmail/thread-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a thread</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns every message of one conversation as readable rows, oldest first: from, to, subject, received, body text, labels and attachment names.</span>
     </a>
     <a class="tool-op" href="gmail/thread-trash.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Move a thread to trash</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Moves every message of one conversation to the Trash, where Gmail deletes them for good after 30 days, and returns the thread.</span>
     </a>
   </div>

Use Gmail as an App Action
--------------------------

The same 22 operations are also a fixed workflow step. Drop **App Action** on the canvas, pick **Gmail**, choose the action and fill in its details. It runs every time the flow reaches it, exactly as set; no model decides. Use it for the steps that must always happen, such as saving an approved result, and keep the agent tool for what the model should choose. See :doc:`Gmail App Actions </agentic-ai-guide/tools-integrations/app-action-apps/gmail>` for every action, its inputs and the trigger events.

Good to know
------------

* Message rows are already readable: sender, subject, received time, body text (cut at 6,000 characters), labels, unread flag and attachment names.
* Prefer **Move a message to trash**; Gmail empties the Trash after 30 days, while **Delete a message permanently** cannot be undone.
* **Create a draft** is the safe way to let a person check an email before it goes; **Send a draft** sends it later.
* **Read attachments** saves files to the engine's disk and can extract their text. The folder it saves to is set in the tool settings, never by the model.
* **Get a label with counts** gives exact unread and total counts; message lists stop at their limit and are not a count.

Example
-------

**Draft replies for review.** Tick the Look things up pack plus Draft create. Then give the Agent Node instructions like these:

.. code-block:: text

   You help the support team with their Gmail inbox.
   Search for unread messages from the last day with the label Support.
   For each one, read the whole thread, then create a draft reply in the same thread.
   Never send email yourself; a person reviews every draft.

Other common uses:

* Summarise the unread email from one customer domain each morning.
* Draft replies to support emails for a person to review and send.
* Save invoice attachments and hand their text to a Sheets or database tool.

Troubleshooting
---------------

***Request had insufficient authentication scopes*.**
   The refresh token was issued without the scope that tool needs. Generate a new refresh token with the extra scope and update the Google connection.

**Search finds nothing that you can see in Gmail.**
   Check the query in Gmail's own search box first. The tool uses the same syntax, for example ``from:billing@acme.com newer_than:7d has:attachment``.

**The agent sends instead of drafting.**
   Untick **Send an email** and **Send a draft**. An agent cannot call a tool it was never given.

**The agent does not call the tool, or picks the wrong one.**
   Name the tool in the instructions and untick operations that sound alike. See :ref:`making-tools-reliable`.

FAQ
---

**Which mailbox does it read?**
   The Google account that issued the refresh token. Use one connection per mailbox.

**Can it read attachments?**
   Yes. **Read attachments** saves the files and extracts their text; **Download attachments** only saves them, for a later tool such as Google Drive **Upload a file**.

Related
-------

* :doc:`/agentic-ai-guide/tools-integrations/tools-connectors` - how tools work, choosing operations, and fixed settings
* :doc:`/agentic-ai-guide/tools-integrations/connector-tools/index` - every connector
* :doc:`/agentic-ai-guide/safety-guardrails/human-in-the-loop` - approving writes
* :doc:`/agentic-ai-guide/tools-integrations/app-actions` - the same operations as fixed workflow steps
