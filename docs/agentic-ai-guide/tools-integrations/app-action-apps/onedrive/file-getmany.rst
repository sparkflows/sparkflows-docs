:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../onedrive.html">OneDrive</a> › File</p>

List files in a folder
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/onedrive.svg" alt="OneDrive logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>OneDrive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the files and folders directly inside one folder of a user's OneDrive, each with id, name, type, size, web address and who last changed it and when.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/onedrive>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **OneDrive**.
#. **Action:** under **File**, choose **List files in a folder**.
#. **Details:** choose your Microsoft Graph connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from OneDrive** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **User**
     - No
     - The address whose OneDrive this is, for example someone@company.com. For example ``someone@company.com``.
   * - **File or folder id**
     - No
     - The id of the file or folder to act on. For upload, the folder to put the files in: an id or a path such as Reports/2026; blank is the top.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``name, size, webUrl``.
   * - **Limit**
     - No
     - How many rows at most. A run from the canvas previews 20. Default: ``100``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Extra query parameters (JSON)**
     - No
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}. For example ``{"$top": "50"}``.
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from OneDrive** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch OneDrive with this action and start the flow when something new turns up. Pick **OneDrive** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **File added to a folder**
     - User is the OneDrive owner's address, and Folder the folder to watch: a path such as Reports/2026, an item id, or / for the top. The first check records the folder's files; later checks report each file that appears directly in it, uploaded, copied or moved in.
   * - **File created or modified in a folder**
     - User is the OneDrive owner's address, and Folder the folder to watch: a path such as Reports/2026, an item id, or / for the top. Reports each file directly in it that is added or saved since the last check.
   * - **File added with a name containing**
     - User is the OneDrive owner's address, and Folder the folder to watch: a path such as Reports/2026, an item id, or / for the top, and Filter a text the file name contains, such as .pdf or invoice. The first check records the matching files; later checks report each new one that appears directly in the folder.
   * - **Folder created in a folder**
     - User is the OneDrive owner's address, and Folder the folder to watch: a path such as Reports/2026, an item id, or / for the top. The first check records its folders; later checks report each folder created directly inside it.

Let an agent decide instead
---------------------------

To let an agent call **List files in a folder** only when a request needs it, add the :doc:`List files in a folder tool </agentic-ai-guide/tools-integrations/connector-tools/onedrive/file-getmany>` to an Agent Node.

Other File actions
------------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-sharelink.html">Create a sharing link</a></div>
