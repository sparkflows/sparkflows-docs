:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › Drive</p>

Get a user's OneDrive
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/onedrive.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a user's OneDrive with its id, owner, web address and storage quota (total, used and remaining). Use the id as destinationDriveId in File copy.

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
     - The address whose OneDrive to read. Example: asha.rao@contoso.com.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph drive properties to return, such as id, owner, quota and webUrl; blank returns them all. Example: ["id", "quota", "webUrl"].

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **OneDrive**, connect, and tick **get** in the **Drive** row. The model sees it as ``onedrive_drive_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **OneDrive**, then **Get a user's OneDrive**, and fill in the inputs above. It runs every time the flow reaches it.

Other Drive tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="drive-getmany.html">List drives</a></div>
