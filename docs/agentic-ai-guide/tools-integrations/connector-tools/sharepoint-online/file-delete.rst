:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › File</p>

Delete a file or folder
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Delete · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes a file, or a folder with everything in it, moving it to the site's recycle bin. Use File move to relocate it instead.

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
   * - ``file``
     - File or folder
     - text
     - Yes
     - The file or folder as a path such as TestData/Old/draft.docx, or its item id.
   * - ``site``
     - Site
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **delete** in the **File** row. The model sees it as ``sharepoint_online_file_delete``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Delete a file or folder**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a></div>
