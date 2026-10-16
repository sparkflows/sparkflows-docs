:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › List</p>

Create a list
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>List</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a list on the site with a Title column plus any text columns named, and returns it with its id. Use List Item create to add rows to it afterwards.

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
   * - ``name``
     - List name
     - text
     - Yes
     - The list's display name. Example: Vendor onboarding.
   * - ``site``
     - Site
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``columns``
     - Columns
     - list of text
     - No
     - Text columns to add besides Title, each a name without spaces. Example: ["Owner", "DueDate", "Status"].
   * - ``template``
     - Template
     - text
     - No
     - The list template: genericList (the default) for a plain list, or documentLibrary, tasks, events, contacts, links or announcements.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **create** in the **List** row. The model sees it as ``sharepoint_online_list_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Create a list**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other List tools
----------------

.. raw:: html

   <div class="tool-related"><a href="list-getmany.html">List the site&#x27;s lists</a><a href="list-get.html">Get a list</a><a href="list-delete.html">Delete a list</a></div>
