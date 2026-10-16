:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Attachment</p>

Read email attachments
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves the attachments of one or more emails to the engine's disk and returns one row per file: the email it came in, the file name, type and size, the saved path, and with extractText the file's text, text\_status and text\_source.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/outlook-mail>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Outlook Mail**.
#. **Action:** under **Attachment**, choose **Read email attachments**.
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
     - The address of the mailbox, for example someone@company.com.
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
   * - **File types**
     - No
     - Only attachments with these extensions, comma-separated, for example pdf,docx. Blank takes every attachment.
   * - **Save into folder**
     - No
     - A folder on the machine the engine runs on, for example C:\\Data\\Invoices or /data/invoices. The full path of each saved file comes back in the path column. Blank uses ~/.fireagent/outlook\_attachments.
   * - **A folder per email**
     - No
     - Where the saved files go.

       * ``true`` (default): Each email's files go in their own sub-folder, named after the email.
       * ``false``: Every file goes straight into the folder.

       Two files with the same name are kept apart as ``name-2``.
   * - **If the file is already there**
     - No
     - What to do when the folder already holds a file with the same name.

       * ``overwrite`` (default): Replace the old file.
       * ``keep both``: Keep both. The new file gets the next free number.
       * ``skip``: Keep the old file and skip the new one.

       The ``save_status`` column says ``saved`` or ``skipped``.
   * - **PDF password (optional)**
     - No
     - For PDFs that arrive locked. Without it a locked PDF comes back with text\_status = password\_protected.
   * - **Text kept per file**
     - No
     - Characters of text kept per file; the rest is cut. Default: ``20000``.
   * - **Read the text of each file**
     - No
     - Whether to read the words inside each file.

       * ``true`` (default): Adds a ``text`` column with the words of each file: PDF, Word, Excel, PowerPoint, OpenDocument, RTF, attached emails, zip archives, text and CSV. With a model set under **Read pictures and scans with**, photos, screenshots and scanned PDFs too.
       * ``false``: Only saves the files.

       The ``text_status`` column says how it went: ``ok``, ``password_protected``, ``no_text``, ``small_image``, ``unsupported`` or ``vision_error``.
   * - **Read pictures and scans with**
     - No
     - An LLM connection (OpenAI, Azure OpenAI or Gemini) whose model reads the words in photos, screenshots and scanned PDFs, which hold no text of their own. Blank leaves them unread. Used in an agent's App Action; an agent that uses this app as a tool reads them with its own model.

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
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}.
   * - **Nested fields**
     - No
     - Some records keep a value inside another value, such as a priority inside an issue. This decides how those inner values become columns.

       * ``deep`` (default): Every inner value gets its own column, named with dots, such as ``fields.priority.name``.
       * ``oneLevel``: Only the first level is split. Anything deeper stays in one column as JSON text.
       * ``json``: Each inner value stays whole, in one column of JSON text.

       See the example below the table.

**Nested fields, by example.** Take a record ``{"id": 7, "fields": {"priority": {"name": "High"}}}``. Each choice gives you these columns:

.. list-table::
   :header-rows: 1
   :widths: 20 80
   :class: tool-table

   * - Choice
     - Columns you get
   * - ``deep``
     - ``id`` = ``7`` and ``fields.priority.name`` = ``High``
   * - ``oneLevel``
     - ``id`` = ``7`` and ``fields.priority`` = ``{"name": "High"}``
   * - ``json``
     - ``id`` = ``7`` and ``fields`` = ``{"priority": {"name": "High"}}``

Keep ``deep`` unless a later step needs the whole inner value as JSON.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Outlook Mail** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Let an agent decide instead
---------------------------

To let an agent call **Read email attachments** only when a request needs it, add the :doc:`Read email attachments tool </agentic-ai-guide/tools-integrations/connector-tools/outlook-mail/attachment-getmany>` to an Agent Node.

Other Attachment actions
------------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-download.html">Download email attachments</a><a href="attachment-get.html">Read one email attachment</a></div>
