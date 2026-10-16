:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › List</p>

List the site's lists
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>List</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the lists and libraries of a site with their ids, names and web addresses. Use it to find the list name or id that the List Item operations take.

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
   * - ``site``
     - Site
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph list properties to return, such as id, displayName and webUrl; blank returns them all. Example: ["id", "displayName", "webUrl"].
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many lists at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **list** in the **List** row. The model sees it as ``sharepoint_online_list_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **List the site's lists**, and fill in the inputs above. It runs every time the flow reaches it.

Other List tools
----------------

.. raw:: html

   <div class="tool-related"><a href="list-get.html">Get a list</a><a href="list-create.html">Create a list</a><a href="list-delete.html">Delete a list</a></div>
