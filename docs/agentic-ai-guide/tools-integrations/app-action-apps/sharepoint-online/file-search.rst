:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../sharepoint-online.html">SharePoint</a> › File</p>

Search files
============

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

   Finds files and folders in the site's default document library whose names or contents match words, and returns them in the same columns as File getMany.

Before you start
----------------

* A Microsoft Graph or SharePoint connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/sharepoint-online>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **SharePoint**.
#. **Action:** under **File**, choose **Search files**.
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
   * - **Search text**
     - No
     - Words to find in file names and contents across the site's documents. For example ``budget 2026``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``name, path, size, webUrl``.
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

The records come out as rows, one per record. Click **Load the fields from SharePoint** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch SharePoint with this action and start the flow when something new turns up. Pick **SharePoint** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **File matching a search added or changed**
     - Search text is the words to find in file names and contents, for example contract renewal. Reports each file of the site's default library that matches and is added or saved since the last check. Site is the site's address, which a SharePoint connection can already hold.

Let an agent decide instead
---------------------------

To let an agent call **Search files** only when a request needs it, add the :doc:`Search files tool </agentic-ai-guide/tools-integrations/connector-tools/sharepoint-online/file-search>` to an Agent Node.

Other File actions
------------------

.. raw:: html

   <div class="tool-related"><a href="file-getmany.html">List files in a folder</a><a href="file-get.html">Get a file or folder</a><a href="file-download.html">Download a file and read its text</a><a href="file-upload.html">Upload a file</a><a href="file-createfolder.html">Create a folder</a><a href="file-delete.html">Delete a file or folder</a><a href="file-move.html">Move or rename a file</a><a href="file-copy.html">Copy a file</a></div>
