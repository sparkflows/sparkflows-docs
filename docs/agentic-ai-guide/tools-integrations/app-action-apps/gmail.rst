.. _app-action-gmail:

.. rst-class:: agentic-tutorial

Gmail App Actions
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Node</dt><dd>App Action</dd></div>
     <div><dt>Actions</dt><dd>22 across 5 resources</dd></div>
     <div><dt>Reads / changes data</dt><dd>11 / 11</dd></div>
     <div><dt>Connection</dt><dd>Google</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Gmail as a fixed workflow step: search, read and label email, draft or send replies, and save attachments. An App Action runs every time the flow reaches it, exactly as you set it; no model decides. To let an agent choose instead, use the :doc:`Gmail agent tools </agentic-ai-guide/tools-integrations/connector-tools/gmail>`.

.. contents:: On this page
   :local:
   :depth: 1
   :class: tool-toc

Prerequisites
-------------

* **Connection:** A **Google** connection: a client ID, client secret and refresh token from a Google Cloud OAuth client. One Google connection serves Gmail, Calendar, Docs, Drive and Sheets; the scopes on its refresh token decide which of them it can reach.
* The **Gmail API** enabled in the Google Cloud project behind the connection.
* A refresh token with ``https://www.googleapis.com/auth/gmail.readonly`` for the read tools, or ``gmail.modify`` plus ``gmail.send`` to draft, send, label and trash. **Delete a message permanently** needs the full ``https://mail.google.com/`` scope.
* How to create the connection: :ref:`connector-tools-gmail`.

Add a Gmail App Action
----------------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs in the flow.
#. **App:** choose **Gmail**, or type ``gmail`` in **Search apps**.
#. **Action:** pick one of the 22 actions below. Each is marked **reads** or **changes data**.
#. **Details:** choose the Google connection and click **Test**, then fill in the inputs. Click a field under **What arrives here** to insert a value from an earlier step.
#. For a read, click **Load the fields** so later steps can use the columns it returns. Then click **Save action**.

.. figure:: ../../../_assets/agentic-ai-guide/tools/app-actions/gmail-actions.png
   :alt: The Gmail actions in the App Action Action step
   :width: 560px

   Step 2, **Action**, for Gmail.

.. tip::

   A canvas run skips actions that change data unless **Write when run from the canvas** is on; full and scheduled runs always perform them. Every write hands on ``result_status``, ``result_id`` and ``result_error`` for each row. See :doc:`/agentic-ai-guide/tools-integrations/app-actions`.

Actions
-------

The inputs are the boxes on the **Details** step, by their label. Any input can take a value from an earlier step with a ``${...}`` reference.

Message
~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="../connector-tools/gmail/message-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List messages</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists the latest messages in the mailbox, newest first, as readable rows: id, threadId, from, to, subject, received, snippet, body text (cut at 6,000 characters), labels, unread and attachment names.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/message-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a message</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns one message as a readable row: from, to, cc, subject, date, received, body text (cut at 6,000 characters), labels, unread, attachment names and its Message-ID header (message-id), which a reply names in inReplyTo.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/message-search.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Search messages</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Finds messages with Gmail&#x27;s search syntax and returns them as readable rows, newest first: from, to, subject, received, snippet, body text, labels, unread and attachment names.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/message-send.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Send an email</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Sends an email from the mailbox and returns the sent message&#x27;s id, threadId and labelIds.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/message-trash.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Move a message to trash</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Moves one message to the Trash, where Gmail deletes it for good after 30 days, and returns it with its new labelIds.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/message-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a message permanently</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Deletes one message immediately and permanently, without going through the Trash.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/message-modify.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Change a message&#x27;s labels</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Adds or removes labels on one message and returns its new labelIds.</span>
     </a>
   </div>

Draft
~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="../connector-tools/gmail/draft-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List drafts</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists the drafts in the mailbox as readable rows: the draft id, messageId, to, cc, subject, snippet and body text.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/draft-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a draft</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns one draft as a readable row: the draft id, messageId, to, cc, subject and body text.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/draft-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a draft</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Saves an email as a draft without sending it and returns the draft id with its message id.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/draft-send.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Send a draft</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Sends a saved draft as it stands and returns the sent message&#x27;s id, threadId and labelIds; the draft itself is removed.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/draft-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a draft</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Deletes a draft immediately and permanently; it does not go to the Trash.</span>
     </a>
   </div>

Label
~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="../connector-tools/gmail/label-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List labels</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists the mailbox&#x27;s labels with id, name and type (system or user), without any message counts.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/label-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a label with counts</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns one label with exact counts: messagesTotal, messagesUnread, threadsTotal and threadsUnread.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/label-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a label</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Creates a user label and returns it with its id (Label_...).</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/label-update.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Update a label</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Renames a user label or changes its visibility or colors, and returns the updated label.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/label-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a label</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Deletes a user label for good and removes it from every message and thread that carries it; the messages themselves stay.</span>
     </a>
   </div>

Attachment
~~~~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="../connector-tools/gmail/attachment-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Read attachments</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Saves the attachments of one or more emails to the engine&#x27;s disk and returns one row per file: messageId, from, subject, received, filename, extension, mimeType, size, path and, with extractText, the file&#x27;s text, text_status and text_source.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/attachment-download.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Download attachments</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Saves the attachments of one or more emails into a folder on the engine&#x27;s disk, without reading them, and returns one row per file: messageId, from, subject, received, filename, extension, mimeType, size, path (where the file was saved) and save_status (saved, or skipped when the file was already there).</span>
     </a>
   </div>

Thread
~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="../connector-tools/gmail/thread-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List threads</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists conversation threads, newest first, with each thread&#x27;s id and a snippet of its latest message.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/thread-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a thread</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns every message of one conversation as readable rows, oldest first: from, to, subject, received, body text, labels and attachment names.</span>
     </a>
     <a class="tool-op" href="../connector-tools/gmail/thread-trash.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Move a thread to trash</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Moves every message of one conversation to the Trash, where Gmail deletes them for good after 30 days, and returns the thread.</span>
     </a>
   </div>

Start a flow from Gmail
-----------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Gmail and start the flow when one of these events happens. Pick Gmail in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 34 66
   :class: tool-table

   * - Event
     - What it reports
   * - **Email received**
     - Reports each email that arrives, sent mail and drafts left out. Mailbox is blank for the connection's own mailbox.
   * - **Email received from a sender**
     - Filter is the sender's address, a name, or a domain such as acme.com. Reports each email from that sender.
   * - **Email matching a search**
     - Filter is a search in Gmail's search box syntax, for example from:billing@vendor.com has:attachment subject:invoice. Reports each new email that matches it.
   * - **Email received with words in the subject**
     - Filter is one or more words that must all appear in the subject, for example purchase order, or a phrase in double quotes. Reports each new email received with such a subject.
   * - **Email received at an address**
     - Filter is the address on the To line, for example support@company.com or a plus address such as finance+invoices@company.com. Reports each new email sent to it.
   * - **Email with an attachment received**
     - Reports each new email that carries attachments, one record per email with the file names in attachments; Attachment received saves the files themselves.
   * - **Email received with a label**
     - Filter is the label as Gmail search writes it, with hyphens for spaces and slashes, for example client-invoices. Reports each new email that arrives carrying the label, such as one a Gmail filter labels on arrival.
   * - **Important email received**
     - Reports each new email that Gmail marks as important.
   * - **Email received in the Primary tab**
     - Reports each new email that Gmail sorts into Primary, leaving out Promotions, Social, Updates and Forums.
   * - **Email sent**
     - Reports each email the mailbox sends, with its recipients, subject and text.
   * - **Label added to an email**
     - Filter is the label as Gmail search writes it, for example to-agent. The first check records the emails that already carry it; later checks report each email from the last seven days that gains it.
   * - **Email starred**
     - The first check records the starred emails; later checks report each email from the last seven days that is newly starred.
   * - **Attachment received**
     - Reports one record per attachment of each new email, with the file saved on the engine's disk (path) and its text (text). Images in signatures count as attachments; Attachment of a file type received leaves them out.
   * - **Attachment of a file type received**
     - File types lists the extensions to watch, comma-separated, for example pdf, xlsx. Reports one record per matching attachment of each new email, with the file saved on the engine's disk (path) and its text (text).

Related
-------

* :doc:`/agentic-ai-guide/tools-integrations/app-actions` - how App Actions work, reads, writes and safety
* :doc:`/agentic-ai-guide/tools-integrations/app-action-apps/index` - every App Action app
* :doc:`Gmail agent tools </agentic-ai-guide/tools-integrations/connector-tools/gmail>` - the same operations for an Agent Node, with every parameter
