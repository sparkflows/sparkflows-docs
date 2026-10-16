:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../gmail.html">Gmail</a> › Attachment</p>

Download attachments
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/gmail.svg" alt="Gmail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Gmail</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>gmail_attachment_download</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves the attachments of one or more emails into a folder on the engine's disk, without reading them, and returns one row per file: messageId, from, subject, received, filename, extension, mimeType, size, path (where the file was saved) and save\_status (saved, or skipped when the file was already there). Name the emails by id, or leave messageIds blank and find them with a Gmail search. To read what the files say, use Read attachments.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../gmail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Gmail** under **Connectors** and connect your Google connection.
#. Tick **download** in the **Attachment** row, then click **Add to agent**.

The agent now sees ``gmail_attachment_download`` and calls it when a request needs it.

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
   * - ``messageIds``
     - text
     - No
     - One message id, or several separated by commas, from Message search or get; blank uses query. Example: 18c3f2a9b7d4e1f0.
   * - ``query``
     - text
     - No
     - A Gmail search that finds the emails when messageIds is blank, for example from:billing@vendor.com newer\_than:30d; has:attachment is added automatically.
   * - ``fileTypes``
     - text
     - No
     - Only attachments with these extensions, comma-separated, for example pdf,docx,csv; blank reads every attachment. Example: pdf,xlsx.
   * - ``saveFolder``
     - text
     - No
     - A folder on the engine's disk, for example C:\\\\Data\\\\Invoices or /data/invoices; blank uses ~/.fireagent/gmail\_attachments. An agent cannot choose it: a builder fixes it in the tool workbench. Example: C:/data/invoices. *Set in the tool settings, never by the agent.*
   * - ``folderPerEmail``
     - true or false
     - No
     - true saves each email's files in a sub-folder named after the email, false puts every file straight into the folder; two files with one name are kept apart as name-2. Default: True.
   * - ``ifFileExists``
     - text
     - No
     - What happens to a file name the folder already holds from before: overwrite it, keep both (the new file takes the next free number) or skip it; save\_status says saved or skipped. Default: overwrite. One of: overwrite, keep both, skip.
   * - ``limit``
     - whole number
     - No
     - How many emails the search reads at most, up to 100; not used with messageIds. Default: 10.
   * - ``mailbox``
     - text
     - No
     - The mailbox to act on; blank means the connection's own mailbox (me). Set it only for a delegated mailbox. Example: someone@company.com.

Need it on every run?
---------------------

To run **Download attachments** every time a flow reaches it, without the agent deciding, use the :doc:`Download attachments App Action </agentic-ai-guide/tools-integrations/app-action-apps/gmail/attachment-download>`.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-getmany.html">Read attachments</a></div>
