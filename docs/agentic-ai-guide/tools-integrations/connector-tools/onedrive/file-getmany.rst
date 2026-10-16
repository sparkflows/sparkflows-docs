:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

List files in a folder
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/onedrive.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the files and folders directly inside one folder of a user's OneDrive, each with id, name, type, size, web address and who last changed it and when. Use it to browse a folder; the ids it returns are what File get, download, move, copy and delete take.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the OneDrive prerequisites <../onedrive>`.

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
   * - ``user``
     - User
     - text
     - Yes
     - The address whose OneDrive this is. Example: asha.rao@contoso.com.
   * - ``folder``
     - Folder
     - text
     - No
     - The folder to list, as an item id or a path such as Reports/2026; blank lists the top of the drive.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph driveItem properties to return, such as id, name, size and webUrl; blank returns the readable columns, and a list without name comes back in Graph's raw shape. Example: ["id", "name", "size", "webUrl"].
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many files and folders at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **OneDrive**, connect, and tick **list** in the **File** row. The model sees it as ``onedrive_file_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **OneDrive**, then **List files in a folder**, and fill in the inputs above. It runs every time the flow reaches it.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-sharelink.html">Create a sharing link</a></div>
