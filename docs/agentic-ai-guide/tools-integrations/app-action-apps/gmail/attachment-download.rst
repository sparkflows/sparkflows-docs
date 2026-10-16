:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../gmail.html">Gmail</a> › Attachment</p>

Download attachments
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves the attachments of one or more emails into a folder on the engine's disk, without reading them, and returns one row per file: messageId, from, subject, received, filename, extension, mimeType, size, path (where the file was saved) and save\_status (saved, or skipped when the file was already there).

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/gmail>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Gmail**.
#. **Action:** under **Attachment**, choose **Download attachments**.
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
   * - **Message, draft, label or thread id**
     - No
     - The id of the item to act on. For attachments, the message id (several comma-separated), or leave it blank and search.
   * - **Search text**
     - No
     - Gmail's search box syntax: from:, to:, subject:, is:unread, has:attachment, newer\_than:7d, label:Work. Combine with spaces. For example ``from:boss@company.com newer_than:7d``.
   * - **Fields to return**
     - No
     - Columns to keep: id, threadId, from, to, cc, subject, received, snippet, body, labels, unread, attachments. Blank keeps them all. For example ``from, subject, received, snippet``.
   * - **Limit**
     - No
     - How many rows at most. A run from the canvas previews 20. Default: ``100``.
   * - **File types**
     - No
     - Only attachments with these extensions, comma-separated, for example pdf,docx,csv. Blank takes every attachment. For example ``pdf, docx, csv``.
   * - **Save into folder**
     - No
     - A folder on the machine the engine runs on, for example C:\\Data\\Invoices or /data/invoices. The full path of each saved file comes back in the path column. Blank uses ~/.fireagent/gmail\_attachments.
   * - **A folder per email**
     - No
     - true saves each email's files in a sub-folder named after the email; false puts every file straight into the folder. Two files with one name are kept apart as name-2. Choices: ``true``, ``false``. Default: ``true``.
   * - **If the file is already there**
     - No
     - For a file name the folder holds from before: overwrite it, keep both (the new file takes the next free number) or skip it. save\_status says saved or skipped. Choices: ``overwrite``, ``keep both``, ``skip``. Default: ``overwrite``.

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

Let an agent decide instead
---------------------------

To let an agent call **Download attachments** only when a request needs it, add the :doc:`Download attachments tool </agentic-ai-guide/tools-integrations/connector-tools/gmail/attachment-download>` to an Agent Node.

Other Attachment actions
------------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-getmany.html">Read attachments</a></div>
