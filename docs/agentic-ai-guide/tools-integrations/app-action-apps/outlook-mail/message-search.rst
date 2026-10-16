:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Message</p>

Search emails
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds emails with Outlook's search over sender, recipients, subject, body and attachment names, and returns them in the same columns as Message getMany.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/outlook-mail>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Outlook Mail**.
#. **Action:** under **Message**, choose **Search emails**.
#. **Details:** choose your Microsoft Graph connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Outlook Mail** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Mailbox**
     - No
     - The address of the mailbox, for example someone@company.com. For example ``someone@company.com``.
   * - **Message, folder or attachment id**
     - No
     - The message to act on (several comma-separated for attachments); for a list or search, the folder (inbox, sentitems, drafts, archive or a folder id); for one attachment messageId/attachmentId. For example ``inbox, or a message id from a list step``.
   * - **Search text**
     - No
     - Outlook's search: words, from:, subject:, hasattachments:yes. For example ``invoice from:billing@vendor.com``.
   * - **Fields to return**
     - No
     - Columns to keep: id, conversationId, from, to, cc, subject, receivedDateTime, sentDateTime, preview, body, isRead, importance, hasAttachments, categories, webLink. Blank keeps them all. For example ``from, subject, receivedDateTime, preview``.
   * - **Limit**
     - No
     - How many rows at most. A run from the canvas previews 20. Default: ``100``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Extra query parameters (JSON)**
     - No
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}. For example ``{"$filter": "isRead eq false"}``.
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Outlook Mail** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Outlook Mail with this action and start the flow when something new turns up. Pick **Outlook Mail** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Email matching a search received**
     - Mailbox is the address to watch, and Filter an Outlook search, for example invoice from:billing@vendor.com hasattachments:yes. Reports each email arriving in the Inbox that matches it.

Let an agent decide instead
---------------------------

To let an agent call **Search emails** only when a request needs it, add the :doc:`Search emails tool </agentic-ai-guide/tools-integrations/connector-tools/outlook-mail/message-search>` to an Agent Node.

Other Message actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List emails</a><a href="message-get.html">Get an email</a><a href="message-send.html">Send an email</a><a href="message-reply.html">Reply to an email</a><a href="message-replyall.html">Reply to everyone on an email</a><a href="message-forward.html">Forward an email</a><a href="message-update.html">Update an email</a><a href="message-move.html">Move an email to a folder</a><a href="message-delete.html">Delete an email</a><a href="message-createdraft.html">Create a draft email</a></div>
