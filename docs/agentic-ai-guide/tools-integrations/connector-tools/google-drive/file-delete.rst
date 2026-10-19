:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Delete a file permanently
=========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_file_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Permanently deletes a file or folder, skipping the bin; deleting a folder also deletes everything the account owns inside it. It cannot be undone: to move a file to the bin instead use Update a file with trashed true.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.
* The account behind the connection must be allowed to change this data in Google Drive.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **delete** in the **File** row, then click **Add to agent**.

The agent now sees ``google_drive_file_delete`` and calls it when a request needs it.

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
   * - ``supportsAllDrives``
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Drive.

Need it on every run?
---------------------

To run **Delete a file permanently** every time a flow reaches it, without the agent deciding, use the :doc:`Delete a file permanently App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/file-delete>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-upload.html">Upload a file</a></div>
