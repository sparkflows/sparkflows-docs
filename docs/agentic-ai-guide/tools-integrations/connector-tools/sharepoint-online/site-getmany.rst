:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › Site</p>

List sites
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>Site</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_site_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the SharePoint sites of the organization with their ids, names and web addresses. Use Site search to find sites by keyword instead of reading them all.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **list** in the **Site** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_site_getmany`` and calls it when a request needs it.

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
   * - ``fields``
     - list of text
     - No
     - Graph site properties to return, such as id, displayName and webUrl; blank returns them all. Example: ["id", "displayName", "webUrl"].
   * - ``limit``
     - whole number
     - No
     - How many sites at most. Default: 50.

Need it on every run?
---------------------

To run **List sites** every time a flow reaches it, without the agent deciding, use the :doc:`List sites App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/site-getmany>`.

Other Site tools
----------------

.. raw:: html

   <div class="tool-related"><a href="site-get.html">Get a site</a><a href="site-search.html">Search sites</a></div>
