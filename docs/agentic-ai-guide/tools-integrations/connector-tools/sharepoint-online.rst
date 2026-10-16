.. _connector-tools-sharepoint-online:

.. rst-class:: agentic-tutorial

SharePoint Online Tools
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint Online logo">
     <dl class="tool-facts">
     <div><dt>Connection</dt><dd>Microsoft Graph or SharePoint</dd></div>
     <div><dt>Tools</dt><dd>25 across 6 resources</dd></div>
     <div><dt>Reads / writes</dt><dd>15 / 10</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · App Action</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Let an agent find SharePoint sites, browse document libraries, read and upload files, and read and write list items.

.. contents:: On this page
   :local:
   :depth: 1
   :class: tool-toc

Prerequisites
-------------

* **Connection:** A **Microsoft Graph** connection (an Entra ID app registration with tenant ID, client ID and client secret), or a **SharePoint** connection. Grant the Microsoft Graph application permissions below with admin consent.
* ``Sites.Read.All`` to read sites, libraries, files and lists; ``Sites.ReadWrite.All`` to upload, move, create folders and change list items.
* To limit the app to chosen sites, use ``Sites.Selected`` and grant it each site.

Add SharePoint Online to an agent
---------------------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node on the canvas.
#. Choose **SharePoint Online** under **Connectors**, or type ``sharepoint`` in the search box.
#. **Connect.** Choose your Microsoft Graph or SharePoint connection and click **Test connection**. The rest of the screen unlocks when it shows **Connected**.
#. **How the agent sees it.** Keep **A separate tool for each one**, so the agent picks each operation by name.
#. **Tick the operations.** The grid opens with the **Look things up** pack: reads only. Add each write the agent needs; every write waits for approval when it runs.
#. Click **Add to agent**. The ticked operations arrive as one SharePoint Online node, joined to the Agent Node by a dashed tool link.

.. figure:: ../../../_assets/agentic-ai-guide/tools/connectors/sharepoint-online-connected.png
   :alt: SharePoint Online connected, with the connector card and its tool count
   :width: 100%

   Connected: the tested connection, the SharePoint Online card with how many tools are ticked.

.. figure:: ../../../_assets/agentic-ai-guide/tools/connectors/sharepoint-online-tools.png
   :alt: The SharePoint Online operations grid
   :width: 100%

   What the agent may do in SharePoint Online. Blue ticks are the **Look things up** pack; dashed boxes are writes, and a red dot marks an action that writes.

Tools
-----

Each ticked operation becomes one tool, named ``sharepoint_online_<resource>_<operation>``. **Read** tools run straight away. **Write** and **Delete** tools change data in SharePoint Online, so each call waits for :doc:`human approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it takes effect. Click a tool to open its page with every parameter.

.. raw:: html

   <nav class="tool-jump" aria-label="Jump to a resource"><a href="#res-site">Site<span>3</span></a><a href="#res-drive">Drive<span>2</span></a><a href="#res-file">File<span>9</span></a><a href="#res-list">List<span>4</span></a><a href="#res-list_item">List Item<span>5</span></a><a href="#res-page">Page<span>2</span></a></nav>

.. raw:: html

   <span id="res-site" class="tool-anchor"></span>

Site
~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sharepoint-online/site-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a site</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one site with its id, name, title, description and web address.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/site-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List sites</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the SharePoint sites of the organization with their ids, names and web addresses.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/site-search.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Search sites</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Finds sites whose name or description matches keywords and returns their ids, names and web addresses.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-drive" class="tool-anchor"></span>

Drive
~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sharepoint-online/drive-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List document libraries</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the document libraries of a site with their ids, names and web addresses.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/drive-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a document library</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one document library by its id with its name, owner, storage quota and web address.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-file" class="tool-anchor"></span>

File
~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sharepoint-online/file-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List files in a folder</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the files and folders directly inside one folder of the site&#x27;s default document library, each with id, name, type, path, size, web address and who last changed it and when.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/file-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a file or folder</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one file or folder, by path or id, with its id, type, size, web address and who last changed it and when.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/file-search.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Search files</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Finds files and folders in the site&#x27;s default document library whose names or contents match words, and returns them in the same columns as File getMany.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/file-download.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Download a file and read its text</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Saves one file to the engine&#x27;s disk and returns its details with the saved path and its text: the words of a PDF, Word, Excel, text or CSV file, with text_status ok, password_protected, no_text (a scan) or unsupported.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/file-upload.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Upload a file</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Uploads a file from the engine&#x27;s disk into a folder of the site&#x27;s default document library and returns the stored file; a file of the same name there is replaced.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/file-createfolder.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a folder</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Creates a folder in the site&#x27;s default document library and returns it with its id.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/file-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a file or folder</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes a file, or a folder with everything in it, moving it to the site&#x27;s recycle bin.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/file-move.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Move or rename a file</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Moves a file or folder into another folder of the same library, renames it, or both, and returns it.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/file-copy.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Copy a file</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Copies a file or folder into another folder, optionally under a new name.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-list" class="tool-anchor"></span>

List
~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sharepoint-online/list-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List the site&#x27;s lists</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the lists and libraries of a site with their ids, names and web addresses.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/list-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a list</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one list, by name or id, with its display name, template and web address, plus its column definitions when expand is columns.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/list-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a list</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Creates a list on the site with a Title column plus any text columns named, and returns it with its id.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/list-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a list</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes a list together with all its items, moving it to the site&#x27;s recycle bin.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-list_item" class="tool-anchor"></span>

List Item
~~~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sharepoint-online/list-item-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List items in a list</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the items of a list, each as one row with its id, dates, author and every column of the list.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/list-item-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a list item</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one list item by its id with its dates, author and every column.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/list-item-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a list item</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Adds an item to a list and returns it with its id and columns.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/list-item-update.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Update a list item</span><span class="tool-op-kind is-write">Write</span></span>
       <span class="tool-op-desc">Changes columns of an existing list item and returns its columns; columns not named keep their values.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/list-item-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a list item</span><span class="tool-op-kind is-delete">Delete</span></span>
       <span class="tool-op-desc">Deletes an item from a list, moving it to the site&#x27;s recycle bin.</span>
     </a>
   </div>

.. raw:: html

   <span id="res-page" class="tool-anchor"></span>

Page
~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="sharepoint-online/page-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List site pages</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Lists the pages of a site with their ids, names, titles, web addresses and dates.</span>
     </a>
     <a class="tool-op" href="sharepoint-online/page-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a site page</span><span class="tool-op-kind is-read">Read</span></span>
       <span class="tool-op-desc">Returns one site page by its id with its name, title, layout, web address and dates.</span>
     </a>
   </div>

Use SharePoint Online as an App Action
--------------------------------------

The same 25 operations are also a fixed workflow step. Drop **App Action** on the canvas, pick **SharePoint**, choose the action and fill in its details. It runs every time the flow reaches it, exactly as set; no model decides. Use it for the steps that must always happen, such as saving an approved result, and keep the agent tool for what the model should choose. See :doc:`SharePoint App Actions </agentic-ai-guide/tools-integrations/app-action-apps/sharepoint-online>` for every action, its inputs and the trigger events.

Good to know
------------

* Find a site with **Search sites** and pass its id to the library, file and list tools.
* **Download a file and read its text** saves the file to the engine's disk and returns its words.
* List items use the list's internal column names, which **Get a list** returns with ``expand`` columns.

Example
-------

**Read a policy library.** Look things up pack only. Then give the Agent Node instructions like these:

.. code-block:: text

   Find the site named "HR Policies". In its Documents library, list the files
   changed this quarter and summarise each policy in two lines.

Other common uses:

* Answer questions from documents in a team site.
* Publish a generated report to a library folder after approval.
* Update a status column in a SharePoint list.

Troubleshooting
---------------

***Access denied* on one site only.**
   With ``Sites.Selected``, each site has to be granted to the app separately.

**A list update changes nothing.**
   Use the internal column name (for example ``Status0``), not the display name.

**The agent does not call the tool, or picks the wrong one.**
   Name the tool in the instructions and untick operations that sound alike. See :ref:`making-tools-reliable`.

FAQ
---

**Microsoft Graph or SharePoint connection?**
   Either works. Use Microsoft Graph when the same app also serves Outlook, OneDrive or Teams.

Related
-------

* :doc:`/agentic-ai-guide/tools-integrations/tools-connectors` - how tools work, choosing operations, and fixed settings
* :doc:`/agentic-ai-guide/tools-integrations/connector-tools/index` - every connector
* :doc:`/agentic-ai-guide/safety-guardrails/human-in-the-loop` - approving writes
* :doc:`/agentic-ai-guide/tools-integrations/app-actions` - the same operations as fixed workflow steps
