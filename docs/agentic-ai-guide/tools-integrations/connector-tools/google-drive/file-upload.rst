:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Upload a file
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_file_upload</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Uploads a file from the engine's disk into Drive and returns the new file's id, name and web link. The path is a local file, such as one an email attachment step saved; set mimeType to a Google type to convert it on the way in, for example a .docx into a Google Doc.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.
* The account behind the connection must be allowed to change this data in Google Drive.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **upload** in the **File** row, then click **Add to agent**.

The agent now sees ``google_drive_file_upload`` and calls it when a request needs it.

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
   * - ``path``
     - text
     - Yes
     - The file's full path on the engine's disk, for example the path column an attachment step returns. Example: /home/sparkflows/.fireagent/gmail\_attachments/INV-1001/invoice.pdf.
   * - ``folderId``
     - text
     - No
     - The id of the folder to upload into; blank puts the file at the top of My Drive. Example: 1Hh5TzqLmN0pQrS7uVwXyZ2aBcDeFgHiJ.
   * - ``name``
     - text
     - No
     - The name to give the file in Drive; blank keeps its own. Example: Invoice INV-1001.pdf.
   * - ``mimeType``
     - text
     - No
     - A Google type to convert the file into (a Doc, Sheet or Slides deck); blank uploads it unchanged. Example: application/vnd.google-apps.document. One of: application/vnd.google-apps.document, application/vnd.google-apps.spreadsheet, application/vnd.google-apps.presentation.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Drive.

Need it on every run?
---------------------

To run **Upload a file** every time a flow reaches it, without the agent deciding, use the :doc:`Upload a file App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/file-upload>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a></div>
