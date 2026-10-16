:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › File</p>

Download a file and read its text
=================================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves one file to the engine's disk and returns its details with the saved path and its text: the words of a PDF, Word, Excel, text or CSV file, with text\_status ok, password\_protected, no\_text (a scan) or unsupported. Use it to read a document's contents; File get returns only its details.

Prerequisites
-------------

* **Connection:** Microsoft Graph or SharePoint connection. See :doc:`the SharePoint Online prerequisites <../sharepoint-online>`.

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
   * - ``file``
     - File
     - text
     - Yes
     - The file as a path such as TestData/Reports/q3-summary.pdf, or its item id from File getMany or File search.
   * - ``site``
     - Site
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``saveFolder``
     - Save into folder
     - text
     - No
     - A folder on the engine's disk to save the file in; its path comes back in the path column, and blank uses a folder under ~/.fireagent. Example: C:/data/sharepoint.
   * - ``textChars``
     - Text kept
     - whole number
     - No
     - Characters of the file's text kept in the text column; the rest is cut. Default: 20000.
   * - ``pdfPassword``
     - PDF password
     - text
     - No
     - The password of a locked PDF; without it a locked PDF comes back with text\_status password\_protected.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **download** in the **File** row. The model sees it as ``sharepoint_online_file_download``.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Download a file and read its text**, and fill in the inputs above. It runs every time the flow reaches it.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-search.html">Search files</a><a href="file-upload.html">Upload a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a></div>
