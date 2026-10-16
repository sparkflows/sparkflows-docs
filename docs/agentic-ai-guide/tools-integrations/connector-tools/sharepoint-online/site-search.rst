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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/sharepoint-online.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds sites whose name or description matches keywords and returns their ids, names and web addresses. Use it to locate a site before working with its files or lists; to search the documents inside a site use File search.

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
   * - ``query``
     - Keywords
     - text
     - Yes
     - Words matched against site names and descriptions; \* returns every site. Example: Finance.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph site properties to return, such as id, displayName and webUrl; blank returns them all.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many sites at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **SharePoint Online**, connect, and tick **search** in the **Site** row. The model sees it as ``sharepoint_online_site_search``.

**As an App Action.** Drop **App Action** on the canvas, pick **SharePoint**, then **Search sites**, and fill in the inputs above. It runs every time the flow reaches it.

Other Site tools
----------------

.. raw:: html

   <div class="tool-related"><a href="site-get.html">Get a site</a><a href="site-getmany.html">List sites</a></div>
