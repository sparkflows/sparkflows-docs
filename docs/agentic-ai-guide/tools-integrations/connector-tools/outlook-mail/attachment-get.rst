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
     <div><dt>Tool name</dt><dd><code>outlook_mail_attachment_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves one attachment to the engine's disk and returns it as one row with its email, name, type, size, saved path and, with extractText, its text, text\_status and text\_source, read the same way Attachment getMany reads them. Use it when Attachment getMany has already listed the attachment and only that file is needed.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-mail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Mail** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Attachment** row, then click **Add to agent**.

The agent now sees ``outlook_mail_attachment_get`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``mailbox``
     - text
     - Yes
     - The address of the mailbox the email is in. Example: asha.rao@contoso.com.
   * - ``attachment``
     - text
     - Yes
     - The message id and the attachment id joined by a slash, messageId/attachmentId, from the messageId and attachmentId columns of Attachment getMany. Example: AAMkAGI2TG93AAA=/AAMkAGI2TG93AAABEgAQAC8.
   * - ``saveFolder``
     - text
     - No
     - A folder on the engine's disk, for example C:\\\\Data\\\\Invoices or /data/invoices; blank uses ~/.fireagent/outlook\_attachments. An agent cannot choose it: a builder fixes it in the tool workbench. Example: C:/data/invoices. *Set in the tool settings, never by the agent.*
   * - ``folderPerEmail``
     - true or false
     - No
     - true saves each email's files in a sub-folder named after the email, false puts every file straight into the folder; two files with one name are kept apart as name-2. Default: True.
   * - ``ifFileExists``
     - text
     - No
     - What happens to a file name the folder already holds from before: overwrite it, keep both (the new file takes the next free number) or skip it; save\_status says saved or skipped. Default: overwrite. One of: overwrite, keep both, skip.
   * - ``extractText``
     - true or false
     - No
     - true adds each file's text, text\_status and text\_source: the words of PDF, Word, Excel, PowerPoint, OpenDocument, RTF, attached email, zip, text and CSV files, and of pictures and scans when the read has a vision model; false only saves the files. Default: True.
   * - ``pdfPassword``
     - text
     - No
     - The password for a PDF that arrives locked; without it a locked PDF comes back with text\_status password\_protected.
   * - ``textChars``
     - whole number
     - No
     - Characters of text kept; the rest is cut. Default: 20000.

Need it on every run?
---------------------

To run **Read one email attachment** every time a flow reaches it, without the agent deciding, use the :doc:`Read one email attachment App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail/attachment-get>`.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-getmany.html">Read email attachments</a></div>
