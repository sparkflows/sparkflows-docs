:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Get a file
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_file_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one file's or folder's metadata: name, type, size, created and modified time, parent folders and web link. It returns no content; use Download a file for that, and Search files to find an id from a name.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **get** in the **File** row, then click **Add to agent**.

The agent now sees ``google_drive_file_get`` and calls it when a request needs it.

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
   * - ``fileId``
     - text
     - Yes
     - The file or folder's id, from Search files or List files, never its name. Example: 1Q2w3E4r5T6y7U8i9O0pAsDfGhJkLzXcVb.
   * - ``fields``
     - list of text
     - No
     - File fields to return, for example ["id", "name", "mimeType", "webViewLink", "modifiedTime"]; blank returns id, name, mimeType, created and modified time, size, webViewLink and parents.
   * - ``supportsAllDrives``
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

Need it on every run?
---------------------

To run **Get a file** every time a flow reaches it, without the agent deciding, use the :doc:`Get a file App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/file-get>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a><a href="file-upload.html">Upload a file</a></div>
