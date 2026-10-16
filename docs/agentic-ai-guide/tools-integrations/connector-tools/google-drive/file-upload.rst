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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-drive.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Uploads a file from the engine's disk into Drive and returns the new file's id, name and web link. The path is a local file, such as one an email attachment step saved; set mimeType to a Google type to convert it on the way in, for example a .docx into a Google Doc.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Drive prerequisites <../google-drive>`.
* The connection's account must be allowed to change this data in Google Drive.

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
   * - ``path``
     - File path
     - text
     - Yes
     - The file's full path on the engine's disk, for example the path column an attachment step returns. Example: /home/sparkflows/.fireagent/gmail\_attachments/INV-1001/invoice.pdf.
   * - ``folderId``
     - Into folder
     - text
     - No
     - The id of the folder to upload into; blank puts the file at the top of My Drive. Example: 1Hh5TzqLmN0pQrS7uVwXyZ2aBcDeFgHiJ.
   * - ``name``
     - Name in Drive
     - text
     - No
     - The name to give the file in Drive; blank keeps its own. Example: Invoice INV-1001.pdf.
   * - ``mimeType``
     - Convert to
     - text
     - No
     - A Google type to convert the file into (a Doc, Sheet or Slides deck); blank uploads it unchanged. Example: application/vnd.google-apps.document. One of: application/vnd.google-apps.document, application/vnd.google-apps.spreadsheet, application/vnd.google-apps.presentation.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Drive**, connect, and tick **upload** in the **File** row. The model sees it as ``google_drive_file_upload``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Drive**, then **Upload a file**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a></div>
