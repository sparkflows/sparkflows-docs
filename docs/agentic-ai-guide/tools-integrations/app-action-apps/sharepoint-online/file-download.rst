:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../sharepoint-online.html">SharePoint</a> › File</p>

Download a file and read its text
=================================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/sharepoint_online.svg" alt="SharePoint logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>SharePoint</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Saves one file to the engine's disk and returns its details with the saved path and its text: the words of a PDF, Word, Excel, text or CSV file, with text\_status ok, password\_protected, no\_text (a scan) or unsupported.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/sharepoint-online>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **SharePoint**.
#. **Action:** under **File**, choose **Download a file and read its text**.
#. **Details:** choose your Microsoft Graph or SharePoint connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from SharePoint** so later steps can use the columns, then **Save action**.

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
   * - **Site**
     - No
     - The site's URL, name or id. Blank uses the site on the connection.
   * - **File, folder, list or item**
     - No
     - A file or folder by id or path (TestData/Reports), the list for List operations, or the item id for List Item operations. For example ``TestData/Reports, or an item id``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``name, path, size, webUrl``.
   * - **Save into folder**
     - No
     - A folder on the engine's disk; the path of each saved file comes back in the path column. Blank uses a folder under ~/.fireagent.
   * - **PDF password (optional)**
     - No
     - For PDFs that arrive locked. Without it a locked PDF comes back with text\_status = password\_protected.
   * - **Text kept per file**
     - No
     - Characters of text kept per file; the rest is cut. Default: ``20000``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from SharePoint** to see the columns before you save.

Let an agent decide instead
---------------------------

To let an agent call **Download a file and read its text** only when a request needs it, add the :doc:`Download a file and read its text tool </agentic-ai-guide/tools-integrations/connector-tools/sharepoint-online/file-download>` to an Agent Node.

Other File actions
------------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-search.html">Search files</a><a href="file-upload.html">Upload a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a></div>
