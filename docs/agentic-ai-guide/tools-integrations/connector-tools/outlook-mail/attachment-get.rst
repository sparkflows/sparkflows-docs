:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Attachment</p>

Read one email attachment
=========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-mail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves one attachment to the engine's disk and returns it as one row with its email, name, type, size, saved path and, with extractText, its text, text\_status and text\_source, read the same way Attachment getMany reads them. Use it when Attachment getMany has already listed the attachment and only that file is needed.

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
     - The address of the mailbox the email is in. Example: asha.rao@contoso.com.
   * - ``attachment``
     - Message and attachment id
     - text
     - Yes
     - The message id and the attachment id joined by a slash, messageId/attachmentId, from the messageId and attachmentId columns of Attachment getMany. Example: AAMkAGI2TG93AAA=/AAMkAGI2TG93AAABEgAQAC8.
   * - ``saveFolder``
     - Save into folder
     - text
     - No
     - A folder on the engine's disk, for example C:\\\\Data\\\\Invoices or /data/invoices; blank uses ~/.fireagent/outlook\_attachments. An agent cannot choose it: a builder fixes it in the tool workbench. Example: C:/data/invoices. *Set in the tool settings, never by the agent.*
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
   * - ``extractText``
     - Read the text of the file
     - true or false
     - No
     - true adds each file's text, text\_status and text\_source: the words of PDF, Word, Excel, PowerPoint, OpenDocument, RTF, attached email, zip, text and CSV files, and of pictures and scans when the read has a vision model; false only saves the files. Default: True.
   * - ``pdfPassword``
     - PDF password
     - text
     - No
     - The password for a PDF that arrives locked; without it a locked PDF comes back with text\_status password\_protected.
   * - ``textChars``
     - Text kept
     - whole number
     - No
     - Characters of text kept; the rest is cut. Default: 20000.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Mail**, connect, and tick **get** in the **Attachment** row. The model sees it as ``outlook_mail_attachment_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Mail**, then **Read one email attachment**, and fill in the inputs above. It runs every time the flow reaches it.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-getmany.html">Read email attachments</a><a href="attachment-download.html">Download email attachments</a></div>
