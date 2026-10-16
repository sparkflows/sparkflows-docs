:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

Download a file and read its text
=================================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>onedrive_file_download</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves one file to the engine's disk and returns its details with the saved path and its text: the words of a PDF, Word, Excel, text or CSV file, with text\_status ok, password\_protected, no\_text (a scan) or unsupported. Use it to read a document's contents; File get returns only its details.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../onedrive>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **OneDrive** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **download** in the **File** row, then click **Add to agent**.

The agent now sees ``onedrive_file_download`` and calls it when a request needs it.

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
     - The address whose OneDrive this is. Example: asha.rao@contoso.com.
   * - ``fileId``
     - text
     - Yes
     - The item id of the file, from the id column of File getMany. Example: 01BYE5RZ6QN3ZWBTUFOFD3GSPGOHDJD36K.
   * - ``saveFolder``
     - text
     - No
     - A folder on the engine's disk to save the file in; its path comes back in the path column, and blank uses a folder under ~/.fireagent. Example: C:/data/onedrive.
   * - ``textChars``
     - whole number
     - No
     - Characters of the file's text kept in the text column; the rest is cut. Default: 20000.
   * - ``pdfPassword``
     - text
     - No
     - The password of a locked PDF; without it a locked PDF comes back with text\_status password\_protected.

Need it on every run?
---------------------

To run **Download a file and read its text** every time a flow reaches it, without the agent deciding, use the :doc:`Download a file and read its text App Action </agentic-ai-guide/tools-integrations/app-action-apps/onedrive/file-download>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-upload.html">Upload a file</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-sharelink.html">Create a sharing link</a></div>
