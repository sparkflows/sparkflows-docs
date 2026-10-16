:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › List Item</p>

Update a list item
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>List Item</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes columns of an existing list item and returns its columns; columns not named keep their values. Give the new Title in title and any other columns by internal name in columns.

Prerequisites
-------------

* **Connection:** Microsoft Graph or SharePoint connection. See :doc:`the SharePoint Online prerequisites <../sharepoint-online>`.
* The connection's account must be allowed to change this data in SharePoint Online.

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
   * - ``title``
     - Title
     - text
     - No
     - The new Title. Example: Replace printer (done).
   * - ``columns``
     - Other columns
     - JSON object
     - No
     - Other column values to change by internal column name, set beside title. Example: {"Status": "Done"}.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **update** in the **List Item** row. The model sees it as ``sharepoint_online_list_item_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Update a list item**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other List Item tools
---------------------

.. raw:: html

   <div class="tool-related"><a href="list-item-getmany.html">List items in a list</a><a href="list-item-get.html">Get a list item</a><a href="list-item-create.html">Create a list item</a><a href="list-item-delete.html">Delete a list item</a></div>
