:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Create a file or folder
=======================

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

   Creates an empty file or a folder from metadata alone and returns its id, name and web link. Set mimeType to application/vnd.google-apps.folder for a folder, or to a Google type such as application/vnd.google-apps.document for an empty Doc; use Upload a file to send content.

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
   * - ``name``
     - Name
     - text
     - Yes
     - The new file's or folder's name. Example: Q3 Reports.
   * - ``mimeType``
     - Type
     - text
     - No
     - application/vnd.google-apps.folder for a folder, or a Google type such as application/vnd.google-apps.document or application/vnd.google-apps.spreadsheet for an empty Doc or Sheet.
   * - ``parents``
     - Inside folder
     - list of text
     - No
     - The folder to create it in, as a one-item list of folder ids; blank puts it at the top of My Drive. Example: ["1Hh5TzqLmN0pQrS7uVwXyZ2aBcDeFgHiJ"].
   * - ``description``
     - Description
     - text
     - No
     - A short description shown in the file's details. Example: Quarterly finance reports, final versions only..
   * - ``supportsAllDrives``
     - Reach shared drives
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Drive**, connect, and tick **create** in the **File** row. The model sees it as ``google_drive_file_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Drive**, then **Create a file or folder**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a><a href="file-upload.html">Upload a file</a></div>
