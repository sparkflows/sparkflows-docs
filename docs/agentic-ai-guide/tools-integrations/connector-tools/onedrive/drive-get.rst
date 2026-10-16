:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › Drive</p>

Get a user's OneDrive
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>onedrive_drive_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns a user's OneDrive with its id, owner, web address and storage quota (total, used and remaining). Use the id as destinationDriveId in File copy.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../onedrive>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **OneDrive** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Drive** row, then click **Add to agent**.

The agent now sees ``onedrive_drive_get`` and calls it when a request needs it.

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
   * - ``user``
     - text
     - Yes
     - The address whose OneDrive to read. Example: asha.rao@contoso.com.
   * - ``fields``
     - list of text
     - No
     - Graph drive properties to return, such as id, owner, quota and webUrl; blank returns them all. Example: ["id", "quota", "webUrl"].

Need it on every run?
---------------------

To run **Get a user's OneDrive** every time a flow reaches it, without the agent deciding, use the :doc:`Get a user's OneDrive App Action </agentic-ai-guide/tools-integrations/app-action-apps/onedrive/drive-get>`.

Other Drive tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="drive-getmany.html">List drives</a></div>
