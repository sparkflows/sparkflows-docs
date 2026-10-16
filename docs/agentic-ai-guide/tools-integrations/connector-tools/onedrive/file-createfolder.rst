:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

Create a folder
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/onedrive.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a folder in a user's OneDrive, at the top or inside another folder, and returns it with its id. A name already in use there makes the call fail.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the OneDrive prerequisites <../onedrive>`.
* The connection's account must be allowed to change this data in OneDrive.

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
     - The address whose OneDrive gets the folder. Example: asha.rao@contoso.com.
   * - ``name``
     - Folder name
     - text
     - Yes
     - The new folder's name. Example: Reports.
   * - ``parentFolder``
     - Inside folder
     - text
     - No
     - The folder to create it in, as an item id or a path such as Reports; blank is the top of the drive.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **OneDrive**, connect, and tick **createFolder** in the **File** row. The model sees it as ``onedrive_file_createfolder``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **OneDrive**, then **Create a folder**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-sharelink.html">Create a sharing link</a></div>
