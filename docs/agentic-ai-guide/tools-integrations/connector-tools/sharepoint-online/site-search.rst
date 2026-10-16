:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › Site</p>

Search sites
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>Site</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_site_search</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds sites whose name or description matches keywords and returns their ids, names and web addresses. Use it to locate a site before working with its files or lists; to search the documents inside a site use File search.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **search** in the **Site** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_site_search`` and calls it when a request needs it.

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
   * - ``query``
     - text
     - Yes
     - Words matched against site names and descriptions; \* returns every site. Example: Finance.
   * - ``fields``
     - list of text
     - No
     - Graph site properties to return, such as id, displayName and webUrl; blank returns them all.
   * - ``limit``
     - whole number
     - No
     - How many sites at most. Default: 50.

Need it on every run?
---------------------

To run **Search sites** every time a flow reaches it, without the agent deciding, use the :doc:`Search sites App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/site-search>`.

Other Site tools
----------------

.. raw:: html

   <div class="tool-related"><a href="site-get.html">Get a site</a><a href="site-getmany.html">List sites</a></div>
