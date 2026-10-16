:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › List</p>

Get a list
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>List</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_list_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one list, by name or id, with its display name, template and web address, plus its column definitions when expand is columns. Use it to learn the internal column names before creating or updating items.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **get** in the **List** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_list_get`` and calls it when a request needs it.

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
     - The list's name, such as Tasks, or its id.
   * - ``site``
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``expand``
     - text
     - No
     - columns adds the list's column definitions, with the internal names List Item create and update use.
   * - ``fields``
     - list of text
     - No
     - Graph list properties to return, such as displayName, list and webUrl; blank returns them all.

Need it on every run?
---------------------

To run **Get a list** every time a flow reaches it, without the agent deciding, use the :doc:`Get a list App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/list-get>`.

Other List tools
----------------

.. raw:: html

   <div class="tool-related"><a href="list-getmany.html">List the site&#x27;s lists</a><a href="list-create.html">Create a list</a><a href="list-delete.html">Delete a list</a></div>
