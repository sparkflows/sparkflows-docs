:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › List Item</p>

Get a list item
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>List Item</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one list item by its id with its dates, author and every column. Use List Item getMany to find the id.

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
   * - ``list``
     - List
     - text
     - Yes
     - The list the item belongs to: its name, such as Tasks, or its id.
   * - ``itemId``
     - Item id
     - text
     - Yes
     - The item's id, from the id column of List Item getMany. Example: 12.
   * - ``site``
     - Site
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Columns to return by internal name, such as Title and Status; blank returns every column.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **get** in the **List Item** row. The model sees it as ``sharepoint_online_list_item_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Get a list item**, and fill in the inputs above. It runs every time the flow reaches it.

Other List Item tools
---------------------

.. raw:: html

   <div class="tool-related"><a href="list-item-getmany.html">List items in a list</a><a href="list-item-create.html">Create a list item</a><a href="list-item-update.html">Update a list item</a><a href="list-item-delete.html">Delete a list item</a></div>
