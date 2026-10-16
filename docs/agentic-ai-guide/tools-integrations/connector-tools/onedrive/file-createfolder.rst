:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

Create a folder
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>onedrive_file_createfolder</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a folder in a user's OneDrive, at the top or inside another folder, and returns it with its id. A name already in use there makes the call fail.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../onedrive>`.
* The account behind the connection must be allowed to change this data in OneDrive.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **OneDrive** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **createFolder** in the **File** row, then click **Add to agent**.

The agent now sees ``onedrive_file_createfolder`` and calls it when a request needs it.

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
     - The address whose OneDrive gets the folder. Example: asha.rao@contoso.com.
   * - ``name``
     - text
     - Yes
     - The new folder's name. Example: Reports.
   * - ``parentFolder``
     - text
     - No
     - The folder to create it in, as an item id or a path such as Reports; blank is the top of the drive.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in OneDrive.

Need it on every run?
---------------------

To run **Create a folder** every time a flow reaches it, without the agent deciding, use the :doc:`Create a folder App Action </agentic-ai-guide/tools-integrations/app-action-apps/onedrive/file-createfolder>`.

Other File tools
----------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-sharelink.html">Create a sharing link</a></div>
