:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Download a file
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-drive.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches a file's content and returns it as text in a response column. It suits text files such as CSV, TXT or JSON; Google Docs, Sheets and Slides cannot be downloaded this way, and binary files such as PDFs come back unreadable.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Drive prerequisites <../google-drive>`.

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
   * - ``fileId``
     - File id
     - text
     - Yes
     - The file's id, from Search files or List files, never its name. Example: 1Q2w3E4r5T6y7U8i9O0pAsDfGhJkLzXcVb.
   * - ``supportsAllDrives``
     - Reach shared drives
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Drive**, connect, and tick **download** in the **File** row. The model sees it as ``google_drive_file_download``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Drive**, then **Download a file**, and fill in the inputs above. It runs every time the flow reaches it.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a><a href="file-upload.html">Upload a file</a></div>
