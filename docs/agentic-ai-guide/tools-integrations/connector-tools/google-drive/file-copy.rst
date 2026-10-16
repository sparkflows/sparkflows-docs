:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Copy a file
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_file_copy</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Makes a copy of a file, optionally into another folder, and returns the new file's id, name and web link. Folders cannot be copied.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.
* The account behind the connection must be allowed to change this data in Google Drive.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **copy** in the **File** row, then click **Add to agent**.

The agent now sees ``google_drive_file_copy`` and calls it when a request needs it.

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
     - The file's id, from Search files or List files, never its name. Example: 1Q2w3E4r5T6y7U8i9O0pAsDfGhJkLzXcVb.
   * - ``name``
     - text
     - Yes
     - The copy's name. Example: Copy of Q3 Report.
   * - ``parents``
     - list of text
     - No
     - The folder to put the copy in, as a one-item list of folder ids; blank keeps the original's folder. Example: ["1Hh5TzqLmN0pQrS7uVwXyZ2aBcDeFgHiJ"].
   * - ``description``
     - text
     - No
     - A description for the copy. Example: Working copy for the October review..
   * - ``supportsAllDrives``
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Drive.

Need it on every run?
---------------------

To run **Copy a file** every time a flow reaches it, without the agent deciding, use the :doc:`Copy a file App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/file-copy>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-delete.html">Delete a file permanently</a><a href="file-upload.html">Upload a file</a></div>
