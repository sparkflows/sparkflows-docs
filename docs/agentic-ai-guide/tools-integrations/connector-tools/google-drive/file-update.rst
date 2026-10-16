:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Update a file
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

   Changes a file's or folder's metadata, such as renaming it, starring it, moving it to another folder or to the bin, and returns the updated file. It does not change the content.

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
   * - ``fileId``
     - File id
     - text
     - Yes
     - The file or folder's id, from Search files or List files, never its name. Example: 1Q2w3E4r5T6y7U8i9O0pAsDfGhJkLzXcVb.
   * - ``name``
     - New name
     - text
     - No
     - The new name. Example: Q3 Report - final.
   * - ``description``
     - Description
     - text
     - No
     - A new description for the file's details. Example: Signed off by finance on 30 Sep..
   * - ``starred``
     - Starred
     - true or false
     - No
     - true stars the file, false unstars it.
   * - ``trashed``
     - In the bin
     - true or false
     - No
     - true moves the file to the bin, where it stays restorable for 30 days; false restores it.
   * - ``addParents``
     - Move into folder
     - text
     - No
     - Folder ids to move the file into, comma-separated; pair it with removeParents to move rather than add, and give at least one other field such as name, because the call needs a body. Example: 1Hh5TzqLmN0pQrS7uVwXyZ2aBcDeFgHiJ.
   * - ``removeParents``
     - Take out of folder
     - text
     - No
     - Folder ids to take the file out of, comma-separated; Get a file shows its current parents. Example: 0B7x9QpLmS4tUVwXyZ012345678.
   * - ``supportsAllDrives``
     - Reach shared drives
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Drive**, connect, and tick **update** in the **File** row. The model sees it as ``google_drive_file_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Drive**, then **Update a file**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a><a href="file-upload.html">Upload a file</a></div>
