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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_file_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an empty file or a folder from metadata alone and returns its id, name and web link. Set mimeType to application/vnd.google-apps.folder for a folder, or to a Google type such as application/vnd.google-apps.document for an empty Doc; use Upload a file to send content.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.
* The account behind the connection must be allowed to change this data in Google Drive.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **create** in the **File** row, then click **Add to agent**.

The agent now sees ``google_drive_file_create`` and calls it when a request needs it.

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
   * - ``name``
     - text
     - Yes
     - The new file's or folder's name. Example: Q3 Reports.
   * - ``mimeType``
     - text
     - No
     - application/vnd.google-apps.folder for a folder, or a Google type such as application/vnd.google-apps.document or application/vnd.google-apps.spreadsheet for an empty Doc or Sheet.
   * - ``parents``
     - list of text
     - No
     - The folder to create it in, as a one-item list of folder ids; blank puts it at the top of My Drive. Example: ["1Hh5TzqLmN0pQrS7uVwXyZ2aBcDeFgHiJ"].
   * - ``description``
     - text
     - No
     - A short description shown in the file's details. Example: Quarterly finance reports, final versions only..
   * - ``supportsAllDrives``
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Drive.

Need it on every run?
---------------------

To run **Create a file or folder** every time a flow reaches it, without the agent deciding, use the :doc:`Create a file or folder App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/file-create>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a><a href="file-upload.html">Upload a file</a></div>
