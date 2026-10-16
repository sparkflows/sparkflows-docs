:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../sharepoint-online.html">SharePoint Online</a> › File</p>

Move or rename a file
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>SharePoint Online</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>sharepoint_online_file_move</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Moves a file or folder into another folder of the same library, renames it, or both, and returns it. Give destinationFolderId to move and newName to rename; File copy keeps the original in place.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up <../sharepoint-online>`.
* The account behind the connection must be allowed to change this data in SharePoint Online.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **SharePoint Online** under **Connectors** and connect your Microsoft Graph or SharePoint connection.
#. Tick **move** in the **File** row, then click **Add to agent**.

The agent now sees ``sharepoint_online_file_move`` and calls it when a request needs it.

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
   * - ``file``
     - text
     - Yes
     - The file or folder to move, as a path such as TestData/Inbox/q3.xlsx or its item id.
   * - ``site``
     - text
     - No
     - The site as its URL, name or id; blank uses the site on the connection. Example: https://contoso.sharepoint.com/sites/Finance.
   * - ``destinationFolderId``
     - text
     - No
     - The item id of the folder to move it into, from the id column of File getMany or File get. Example: 01BYE5RZ6QN3ZWBTUFOFD3GSPGOHDJD36K.
   * - ``newName``
     - text
     - No
     - The new name, extension included. Example: q3-final.xlsx.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in SharePoint Online.

Need it on every run?
---------------------

To run **Move or rename a file** every time a flow reaches it, without the agent deciding, use the :doc:`Move or rename a file App Action </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online/file-move>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-delete.html">Delete a file or folder</a><a href="file-copy.html">Copy a file</a></div>
