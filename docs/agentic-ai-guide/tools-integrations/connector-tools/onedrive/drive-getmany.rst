:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › Drive</p>

List drives
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>onedrive_drive_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists a user's drives with their ids, names, types and owners. Blank user lists the drives Microsoft Graph returns for the connection's own account; Drive get reads one user's OneDrive.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../onedrive>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **OneDrive** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **list** in the **Drive** row, then click **Add to agent**.

The agent now sees ``onedrive_drive_getmany`` and calls it when a request needs it.

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
     - No
     - The address whose drives to list. Example: asha.rao@contoso.com.
   * - ``fields``
     - list of text
     - No
     - Graph drive properties to return, such as id, name, driveType and owner; blank returns them all.
   * - ``limit``
     - whole number
     - No
     - How many drives at most. Default: 50.

Need it on every run?
---------------------

To run **List drives** every time a flow reaches it, without the agent deciding, use the :doc:`List drives App Action </agentic-ai-guide/tools-integrations/app-action-apps/onedrive/drive-getmany>`.

Other Drive tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="drive-get.html">Get a user&#x27;s OneDrive</a></div>
