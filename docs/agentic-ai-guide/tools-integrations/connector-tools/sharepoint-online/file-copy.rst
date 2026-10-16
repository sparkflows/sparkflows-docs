:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › File</p>

Copy a file
===========

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

   Copies a file or folder into another folder, optionally under a new name. SharePoint makes the copy in the background, so the new item's id is not returned; list the destination folder afterwards to find it.

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
     - The file or folder to copy, as a path such as Templates/budget.xlsx or its item id.
   * - ``site``
     - Site
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``destinationFolderId``
     - Into folder (id)
     - text
     - No
     - The item id of the folder to copy into, from the id column of File getMany or File get; blank copies into the same folder. Example: 01BYE5RZ6QN3ZWBTUFOFD3GSPGOHDJD36K.
   * - ``destinationDriveId``
     - Into library (id)
     - text
     - No
     - The id of the library that holds the destination folder, from Drive getMany; needed when copying into another library. Example: b!-RIj2DuyvEyV1T4NlOaMHk8XkS\_I8MdFlUCq1BlcjgmhRfAj3-Z8RY2VpuvV\_tpd.
   * - ``newName``
     - Name of the copy
     - text
     - No
     - The copy's name; needed when copying into the same folder. Example: budget-2027.xlsx.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **copy** in the **File** row. The model sees it as ``sharepoint_online_file_copy``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Copy a file**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a></div>
