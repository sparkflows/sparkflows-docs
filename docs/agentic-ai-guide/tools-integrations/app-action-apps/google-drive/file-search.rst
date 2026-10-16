:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Search files
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds files and folders that match a Drive query and returns their name, type, size, dates and web link.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-drive>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Drive**.
#. **Action:** under **File**, choose **Search files**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Google Drive** so later steps can use the columns, then **Save action**.

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
   * - **Search text**
     - No
     - Drive's query language: name contains '...', mimeType = 'application/pdf', '<folder id>' in parents, modifiedTime > '2026-10-01'. For example ``name contains 'report' and trashed = false``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``id, name, webViewLink, modifiedTime``.
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

The records come out as rows, one per record. Click **Load the fields from Google Drive** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Google Drive with this action and start the flow when something new turns up. Pick **Google Drive** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **File created**
     - Reports each file created, uploaded or copied into the account's Drive or shared with it, folders left out.
   * - **File created or modified**
     - Reports each file added or edited since the last check, with who changed it last in lastModifyingUser.
   * - **File shared with me**
     - Reports each file or folder newly shared with the account, with who shared it in sharingUser.
   * - **Google Doc created**
     - Reports each new Google Docs document in the account's Drive or shared with it; its id is what the Google Docs app takes as Document.
   * - **Google Sheet created**
     - Reports each new Google Sheets spreadsheet in the account's Drive or shared with it; its id is what the Google Sheets app takes as Spreadsheet.
   * - **File created matching a search**
     - Filter is a Drive search, for example name contains 'invoice' and mimeType = 'application/pdf'. Reports each new file that matches it.
   * - **File created in a shared drive**
     - Filter is the shared drive's id, from a Drive list or the part of the drive's address after /folders/. Reports each file created anywhere in that drive, in any of its folders.

Let an agent decide instead
---------------------------

To let an agent call **Search files** only when a request needs it, add the :doc:`Search files tool </agentic-ai-guide/tools-integrations/connector-tools/google-drive/file-search>` to an Agent Node.

Other File actions
------------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a><a href="file-upload.html">Upload a file</a></div>
