:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › List</p>

Delete a list
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>List</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_list_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes a list together with all its items, moving it to the site's recycle bin. Use List Item delete to remove single items instead.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.
* The account behind the connection must be allowed to change this data in SharePoint Online.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **delete** in the **List** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_list_delete`` and calls it when a request needs it.

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
     - The list's name, such as Tasks, or its id. Example: Old tasks.
   * - ``site``
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in SharePoint Online.

Need it on every run?
---------------------

To run **Delete a list** every time a flow reaches it, without the agent deciding, use the :doc:`Delete a list App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/list-delete>`.

Other List tools
----------------

.. raw:: html

   <div class="tool-related"><a href="list-getmany.html">List the site&#x27;s lists</a><a href="list-get.html">Get a list</a><a href="list-create.html">Create a list</a></div>
