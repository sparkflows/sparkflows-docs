:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

Create a sharing link
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>onedrive_file_sharelink</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a sharing link to a file or folder and returns the link with its web address, type and scope. It grants access to whoever holds the link within the scope, so it changes the item's permissions.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../onedrive>`.
* The account behind the connection must be allowed to change this data in OneDrive.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **OneDrive** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **shareLink** in the **File** row, then click **Add to agent**.

The agent now sees ``onedrive_file_sharelink`` and calls it when a request needs it.

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
     - The address whose OneDrive holds the item. Example: asha.rao@contoso.com.
   * - ``fileId``
     - text
     - Yes
     - The item id of the file or folder to share, from the id column of File getMany. Example: 01BYE5RZ6QN3ZWBTUFOFD3GSPGOHDJD36K.
   * - ``type``
     - text
     - Yes
     - What the link allows: view (read only), edit, or embed (OneDrive personal accounts only). One of: view, edit, embed.
   * - ``scope``
     - text
     - No
     - anonymous (anyone with the link), organization (people in the tenant) or users (specific people only); blank uses the tenant's default. One of: anonymous, organization, users.
   * - ``expirationDateTime``
     - text
     - No
     - When the link stops working; blank means it does not expire unless tenant policy says so. Example: 2026-12-31T23:59:00Z.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in OneDrive.

Need it on every run?
---------------------

To run **Create a sharing link** every time a flow reaches it, without the agent deciding, use the :doc:`Create a sharing link App Action </agentic-ai-guide/tools-integrations/app-action-apps/onedrive/file-sharelink>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-createfolder.html">Create a folder</a></div>
