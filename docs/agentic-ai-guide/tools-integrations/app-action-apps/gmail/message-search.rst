:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../gmail.html">Gmail</a> › Message</p>

Search messages
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds messages with Gmail's search syntax and returns them as readable rows, newest first: from, to, subject, received, snippet, body text, labels, unread and attachment names.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/gmail>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Gmail**.
#. **Action:** under **Message**, choose **Search messages**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Gmail** so later steps can use the columns, then **Save action**.

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
     - Blank means the mailbox the connection belongs to.
   * - **Search text**
     - No
     - Gmail's search box syntax: from:, to:, subject:, is:unread, has:attachment, newer\_than:7d, label:Work. Combine with spaces. For example ``from:boss@company.com newer_than:7d``.
   * - **Fields to return**
     - No
     - Columns to keep: id, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments. Blank keeps them all. For example ``from, subject, received, snippet``.
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
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}. For example ``{"labelIds": "INBOX"}``.
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Gmail** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Gmail with this action and start the flow when something new turns up. Pick **Gmail** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
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

Let an agent decide instead
---------------------------

To let an agent call **Search messages** only when a request needs it, add the :doc:`Search messages tool </agentic-ai-guide/tools-integrations/connector-tools/gmail/message-search>` to an Agent Node.

Other Message actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="message-getmany.html">List messages</a><a href="message-get.html">Get a message</a><a href="message-send.html">Send an email</a><a href="message-trash.html">Move a message to trash</a><a href="message-delete.html">Delete a message permanently</a><a href="message-modify.html">Change a message&#x27;s labels</a></div>
