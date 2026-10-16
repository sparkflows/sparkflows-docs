:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › File</p>

Upload a file
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Uploads a file from the engine's disk into a folder of the site's default document library and returns the stored file; a file of the same name there is replaced. Files of up to 250 MB are supported.

Prerequisites
-------------

* **Connection:** Microsoft Graph or SharePoint connection. See :doc:`the SharePoint Online prerequisites <../sharepoint-online>`.
* The connection's account must be allowed to change this data in SharePoint Online.

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
   * - ``filePath``
     - File on the engine
     - text
     - Yes
     - The full path of the file on the engine's disk, such as the path column an attachment or download step returns. Example: C:/data/invoices/inv-4471.pdf.
   * - ``site``
     - Site
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``folder``
     - Into folder
     - text
     - No
     - The folder to put the file in, as a path such as TestData/Reports or an item id; blank is the top of the library.
   * - ``fileName``
     - Name in SharePoint
     - text
     - No
     - The name to give the file in SharePoint; blank keeps the file's own name. Example: invoice-4471.pdf.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **upload** in the **File** row. The model sees it as ``sharepoint_online_file_upload``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Upload a file**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file and read its text</a><a href="file-createfolder.html">Create a folder</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a></div>
