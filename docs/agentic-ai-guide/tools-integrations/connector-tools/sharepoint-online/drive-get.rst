:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › Drive</p>

Get a document library
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_drive_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one document library by its id with its name, owner, storage quota and web address. Use Drive getMany to find the id.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **get** in the **Drive** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_drive_get`` and calls it when a request needs it.

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
   * - ``driveId``
     - text
     - Yes
     - The id of the document library, from the id column of Drive getMany. Example: b!-RIj2DuyvEyV1T4NlOaMHk8XkS\_I8MdFlUCq1BlcjgmhRfAj3-Z8RY2VpuvV\_tpd.
   * - ``fields``
     - list of text
     - No
     - Graph drive properties to return, such as name, quota and webUrl; blank returns them all.

Need it on every run?
---------------------

To run **Get a document library** every time a flow reaches it, without the agent deciding, use the :doc:`Get a document library App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/drive-get>`.

Other Drive tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="drive-getmany.html">List document libraries</a></div>
