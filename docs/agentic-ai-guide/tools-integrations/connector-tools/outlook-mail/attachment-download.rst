:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Attachment</p>

Download email attachments
==========================

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

   Saves the attachments of one or more emails into a folder on the engine's disk, without reading them, and returns one row per file: the email it came in, the file name, type and size, path (where the file was saved) and save\_status (saved, skipped when the file was already there, or not\_a\_file for an attached item or link). Give message ids from Message getMany or Message search, or a search text that picks the emails. To read what the files say, use Read email attachments.

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
     - The address of the mailbox the emails are in. Example: asha.rao@contoso.com.
   * - ``messageIds``
     - Message ids
     - text
     - No
     - The emails to read, as one message id or several separated by commas; blank uses the search text instead. Example: AAMkAGI2TG93AAA=.
   * - ``query``
     - Search text
     - text
     - No
     - Outlook's search for the emails whose attachments to read, used when messageIds is blank: words, from:, subject:, hasattachments:yes, with double quotes for an exact phrase; only emails that have attachments are read. Example: invoice from:billing@vendor.com.
   * - ``attachmentTypes``
     - File types
     - text
     - No
     - Only attachments with these extensions, separated by commas; blank reads every attachment. Example: pdf,docx.
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
   * - ``limit``
     - Emails searched
     - whole number
     - No
     - How many emails the search text reads at most, up to 100; not used when messageIds is given. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Mail**, connect, and tick **download** in the **Attachment** row. The model sees it as ``outlook_mail_attachment_download``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Mail**, then **Download email attachments**, and fill in the inputs above. It runs every time the flow reaches it.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-getmany.html">Read email attachments</a><a href="attachment-get.html">Read one email attachment</a></div>
