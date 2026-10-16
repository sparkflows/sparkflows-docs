:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

Create a sharing link
=====================

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

   Creates a sharing link to a file or folder and returns the link with its web address, type and scope. It grants access to whoever holds the link within the scope, so it changes the item's permissions.

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
     - The address whose OneDrive holds the item. Example: asha.rao@contoso.com.
   * - ``fileId``
     - Item id
     - text
     - Yes
     - The item id of the file or folder to share, from the id column of File getMany. Example: 01BYE5RZ6QN3ZWBTUFOFD3GSPGOHDJD36K.
   * - ``type``
     - Link type
     - text
     - Yes
     - What the link allows: view (read only), edit, or embed (OneDrive personal accounts only). One of: view, edit, embed.
   * - ``scope``
     - Who can use it
     - text
     - No
     - anonymous (anyone with the link), organization (people in the tenant) or users (specific people only); blank uses the tenant's default. One of: anonymous, organization, users.
   * - ``expirationDateTime``
     - Expires
     - text
     - No
     - When the link stops working; blank means it does not expire unless tenant policy says so. Example: 2026-12-31T23:59:00Z.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **OneDrive**, connect, and tick **shareLink** in the **File** row. The model sees it as ``onedrive_file_sharelink``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **OneDrive**, then **Create a sharing link**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-createfolder.html">Create a folder</a></div>
