:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

Upload a file
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>onedrive_file_upload</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Uploads a file from the engine's disk into a folder of a user's OneDrive and returns the stored file; a file of the same name there is replaced. Files of up to 250 MB are supported.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../onedrive>`.
* The account behind the connection must be allowed to change this data in OneDrive.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **OneDrive** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **upload** in the **File** row, then click **Add to agent**.

The agent now sees ``onedrive_file_upload`` and calls it when a request needs it.

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
   * - ``user``
     - text
     - Yes
     - The address whose OneDrive receives the file. Example: asha.rao@contoso.com.
   * - ``filePath``
     - text
     - Yes
     - The full path of the file on the engine's disk, such as the path column an attachment or download step returns. Example: C:/data/invoices/inv-4471.pdf.
   * - ``folder``
     - text
     - No
     - The folder to put the file in, as an item id or a path such as Reports/2026; blank is the top of the drive.
   * - ``fileName``
     - text
     - No
     - The name to give the file in OneDrive; blank keeps the file's own name. Example: invoice-4471.pdf.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in OneDrive.

Need it on every run?
---------------------

To run **Upload a file** every time a flow reaches it, without the agent deciding, use the :doc:`Upload a file App Action </agentic-ai-guide/tools-integrations/app-action-apps/onedrive/file-upload>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-sharelink.html">Create a sharing link</a></div>
