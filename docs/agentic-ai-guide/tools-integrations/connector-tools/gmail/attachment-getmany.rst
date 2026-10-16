:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Attachment</p>

Read attachments
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/gmail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves the attachments of one or more emails to the engine's disk and returns one row per file: messageId, from, subject, received, filename, extension, mimeType, size, path and, with extractText, the file's text, text\_status and text\_source. The text is read from PDF, Word, Excel, PowerPoint, OpenDocument, RTF, attached email, zip, text and CSV files, and from photos, screenshots and scanned PDFs by a vision model when the read has one: the agent's own model, or the LLM connection an App Action names (text\_source vision). text\_status is ok, password\_protected, no\_text, small\_image, unsupported or vision\_error. Name the emails by id, or leave messageIds blank and find them with a Gmail search.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Gmail prerequisites <../gmail>`.

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
   * - ``messageIds``
     - Messages
     - text
     - No
     - One message id, or several separated by commas, from Message search or get; blank uses query. Example: 18c3f2a9b7d4e1f0.
   * - ``query``
     - Search
     - text
     - No
     - A Gmail search that finds the emails when messageIds is blank, for example from:billing@vendor.com newer\_than:30d; has:attachment is added automatically.
   * - ``fileTypes``
     - File types
     - text
     - No
     - Only attachments with these extensions, comma-separated, for example pdf,docx,csv; blank reads every attachment. Example: pdf,xlsx.
   * - ``extractText``
     - Read the text of each file
     - true or false
     - No
     - true adds each file's text, text\_status and text\_source: the words of PDF, Word, Excel, PowerPoint, OpenDocument, RTF, attached email, zip, text and CSV files, and of pictures and scans when the read has a vision model; false only saves the files. Default: True.
   * - ``textChars``
     - Text kept per file
     - whole number
     - No
     - Characters of text kept per file; the rest is cut. Default: 20000.
   * - ``saveFolder``
     - Save into folder
     - text
     - No
     - A folder on the engine's disk, for example C:\\\\Data\\\\Invoices or /data/invoices; blank uses ~/.fireagent/gmail\_attachments. An agent cannot choose it: a builder fixes it in the tool workbench. Example: C:/data/invoices. *Set in the tool settings, never by the agent.*
   * - ``folderPerEmail``
     - A folder per email
     - true or false
     - No
     - true saves each email's files in a sub-folder named after the email, false puts every file straight into the folder; two files with one name are kept apart as name-2. Default: True.
   * - ``ifFileExists``
     - If the file is already there
     - text
     - No
     - What happens to a file name the folder already holds from before: overwrite it, keep both (the new file takes the next free number) or skip it; save\_status says saved or skipped. Default: overwrite. One of: overwrite, keep both, skip.
   * - ``pdfPassword``
     - PDF password
     - text
     - No
     - The password of PDFs that arrive locked, such as bank or broker statements; without it they come back with text\_status password\_protected.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many emails the search reads at most, up to 100; not used with messageIds. Default: 10.
   * - ``mailbox``
     - Mailbox
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Gmail**, connect, and tick **list** in the **Attachment** row. The model sees it as ``gmail_attachment_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Gmail**, then **Read attachments**, and fill in the inputs above. It runs every time the flow reaches it.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-download.html">Download attachments</a></div>
