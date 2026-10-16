:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › Drive</p>

Get a document library
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one document library by its id with its name, owner, storage quota and web address. Use Drive getMany to find the id.

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
   * - ``driveId``
     - Library id
     - text
     - Yes
     - The id of the document library, from the id column of Drive getMany. Example: b!-RIj2DuyvEyV1T4NlOaMHk8XkS\_I8MdFlUCq1BlcjgmhRfAj3-Z8RY2VpuvV\_tpd.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph drive properties to return, such as name, quota and webUrl; blank returns them all.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **get** in the **Drive** row. The model sees it as ``sharepoint_online_drive_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Get a document library**, and fill in the inputs above. It runs every time the flow reaches it.

Other Drive tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="drive-getmany.html">List document libraries</a></div>
