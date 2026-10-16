:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › File</p>

Search files
============

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

   Finds files and folders in the site's default document library whose names or contents match words, and returns them in the same columns as File getMany. Use it when the folder is unknown; to list one folder use File getMany.

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
   * - ``query``
     - Search text
     - text
     - Yes
     - Words to find in file names and contents across the site's documents. Example: budget 2026.
   * - ``site``
     - Site
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph driveItem properties to return, such as id, name and webUrl; blank returns the readable columns.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many matches at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **search** in the **File** row. The model sees it as ``sharepoint_online_file_search``.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Search files**, and fill in the inputs above. It runs every time the flow reaches it.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a></div>
