:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

Get a file or folder
====================

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

   Returns one file or folder by its item id with its type, size, path, web address and who last changed it and when. Use File download to read the file's contents as well.

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
   * - ``fileId``
     - Item id
     - text
     - Yes
     - The item id of the file or folder, from the id column of File getMany. Example: 01BYE5RZ6QN3ZWBTUFOFD3GSPGOHDJD36K.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph driveItem properties to return, such as id, name, size and webUrl; blank returns the readable columns.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **OneDrive**, connect, and tick **get** in the **File** row. The model sees it as ``onedrive_file_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **OneDrive**, then **Get a file or folder**, and fill in the inputs above. It runs every time the flow reaches it.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-sharelink.html">Create a sharing link</a></div>
