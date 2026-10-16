:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › Drive</p>

List document libraries
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_drive_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the document libraries of a site with their ids, names and web addresses. The file operations always work in the site's default library (Documents).

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **list** in the **Drive** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_drive_getmany`` and calls it when a request needs it.

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
   * - ``site``
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``fields``
     - list of text
     - No
     - Graph drive properties to return, such as id, name, driveType and webUrl; blank returns them all. Example: ["id", "name", "webUrl"].
   * - ``limit``
     - whole number
     - No
     - How many libraries at most. Default: 50.

Need it on every run?
---------------------

To run **List document libraries** every time a flow reaches it, without the agent deciding, use the :doc:`List document libraries App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/drive-getmany>`.

Other Drive tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="drive-get.html">Get a document library</a></div>
