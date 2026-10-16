:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › List Item</p>

List items in a list
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>List Item</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_list_item_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the items of a list, each as one row with its id, dates, author and every column of the list. Use it to read or scan a list, narrowed with a filter on indexed columns; List Item get reads one item by id.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **list** in the **List Item** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_list_item_getmany`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``list``
     - text
     - Yes
     - The list the items belong to: its name, such as Tasks, or its id.
   * - ``site``
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``filter``
     - text
     - No
     - An OData filter on the item's columns, such as fields/Status eq 'Open'; a column without an index works on lists of up to 5,000 items.
   * - ``fields``
     - list of text
     - No
     - Columns to return by internal name, such as Title and Status; blank returns every column. Example: ["Title", "Status", "AssignedTo"].
   * - ``limit``
     - whole number
     - No
     - How many items at most. Default: 50.

Need it on every run?
---------------------

To run **List items in a list** every time a flow reaches it, without the agent deciding, use the :doc:`List items in a list App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/list-item-getmany>`.

Other List Item tools
---------------------

.. raw:: html

   <div class="tool-related"><a href="list-item-get.html">Get a list item</a><a href="list-item-create.html">Create a list item</a><a href="list-item-update.html">Update a list item</a><a href="list-item-delete.html">Delete a list item</a></div>
