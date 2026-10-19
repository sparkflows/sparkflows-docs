:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › Page</p>

Get a site page
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>Page</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_page_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one site page by its id with its name, title, layout, web address and dates. The page content itself is not returned.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **get** in the **Page** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_page_get`` and calls it when a request needs it.

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
   * - ``pageId``
     - text
     - Yes
     - The page's id, from the id column of Page getMany. Example: 3b1a7c2e-6a47-4b8f-9c2d-8e7f1d2a4b6c.
   * - ``site``
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``fields``
     - list of text
     - No
     - Graph page properties to return, such as title, pageLayout and webUrl; blank returns them all.

Need it on every run?
---------------------

To run **Get a site page** every time a flow reaches it, without the agent deciding, use the :doc:`Get a site page App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/page-get>`.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-getmany.html">List site pages</a></div>
