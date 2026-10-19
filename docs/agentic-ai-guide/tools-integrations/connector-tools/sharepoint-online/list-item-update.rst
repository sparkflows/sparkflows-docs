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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_list_item_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes columns of an existing list item and returns its columns; columns not named keep their values. Give the new Title in title and any other columns by internal name in columns.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.
* The account behind the connection must be allowed to change this data in SharePoint Online.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **update** in the **List Item** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_list_item_update`` and calls it when a request needs it.

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
     - The list the item belongs to: its name, such as Tasks, or its id.
   * - ``itemId``
     - text
     - Yes
     - The item's id, from the id column of List Item getMany. Example: 12.
   * - ``site``
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``title``
     - text
     - No
     - The new Title. Example: Replace printer (done).
   * - ``columns``
     - JSON object
     - No
     - Other column values to change by internal column name, set beside title. Example: {"Status": "Done"}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in SharePoint Online.

Need it on every run?
---------------------

To run **Update a list item** every time a flow reaches it, without the agent deciding, use the :doc:`Update a list item App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/list-item-update>`.

Other List Item tools
---------------------

.. raw:: html

   <div class="tool-related"><a href="list-item-getmany.html">List items in a list</a><a href="list-item-get.html">Get a list item</a><a href="list-item-create.html">Create a list item</a><a href="list-item-delete.html">Delete a list item</a></div>
