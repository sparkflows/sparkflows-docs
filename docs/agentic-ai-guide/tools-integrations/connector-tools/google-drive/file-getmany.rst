:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

List files
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_file_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists files and folders with their name, type, size, dates and web link. With folderId it lists only what is directly inside that folder and leaves out the bin; without it every file the account can see comes back, trashed ones included. Use Search files to filter by name, type or date.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **list** in the **File** row, then click **Add to agent**.

The agent now sees ``google_drive_file_getmany`` and calls it when a request needs it.

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
   * - ``folderId``
     - text
     - No
     - The folder whose direct contents to list, from Search files or List files; blank lists every file. Example: 1Hh5TzqLmN0pQrS7uVwXyZ2aBcDeFgHiJ.
   * - ``limit``
     - whole number
     - No
     - How many files at most. Example: 50. Default: 50.
   * - ``orderBy``
     - text
     - No
     - Sort keys separated by commas, each optionally followed by desc, from createdTime, modifiedTime, name, folder, starred, viewedByMeTime and quotaBytesUsed, for example modifiedTime desc.
   * - ``fields``
     - list of text
     - No
     - File fields to return, for example ["id", "name", "mimeType", "webViewLink", "modifiedTime"]; blank returns id, name, mimeType, created and modified time, size, webViewLink and parents.
   * - ``corpora``
     - text
     - No
     - Which files to look through: user (My Drive and files shared with the account, the default), drive (one shared drive, named in driveId), domain, or allDrives (everything, slowest). One of: user, drive, domain, allDrives.
   * - ``driveId``
     - text
     - No
     - The shared drive to look in when corpora is drive, from List shared drives. Example: 0AHq3nLpQx7fUUk9PVA.
   * - ``includeItemsFromAllDrives``
     - true or false
     - No
     - true includes files that live in shared drives in the results; false keeps to My Drive and files shared with the account. Default: True.
   * - ``supportsAllDrives``
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

Need it on every run?
---------------------

To run **List files** every time a flow reaches it, without the agent deciding, use the :doc:`List files App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/file-getmany>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a><a href="file-upload.html">Upload a file</a></div>
