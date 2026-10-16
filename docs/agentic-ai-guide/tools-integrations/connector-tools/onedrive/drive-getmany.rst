:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › Drive</p>

List drives
===========

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

   Lists a user's drives with their ids, names, types and owners. Blank user lists the drives Microsoft Graph returns for the connection's own account; Drive get reads one user's OneDrive.

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
     - No
     - The address whose drives to list. Example: asha.rao@contoso.com.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph drive properties to return, such as id, name, driveType and owner; blank returns them all.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many drives at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **OneDrive**, connect, and tick **list** in the **Drive** row. The model sees it as ``onedrive_drive_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **OneDrive**, then **List drives**, and fill in the inputs above. It runs every time the flow reaches it.

Other Drive tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="drive-get.html">Get a user&#x27;s OneDrive</a></div>
