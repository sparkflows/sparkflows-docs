:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../google-drive.html">Google Drive</a> › File</p>

Upload a file
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>File</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Uploads a file from the engine's disk into Drive and returns the new file's id, name and web link.

Before you start
----------------

* A Google connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/google-drive>`.
* The account behind the connection must be allowed to change this data in Google Drive.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Google Drive**.
#. **Action:** under **File**, choose **Upload a file**.
#. **Details:** choose your Google connection, click **Test**, then fill in the boxes below.
#. Click **Save action**.

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
   * - **File or folder id**
     - No
     - The id of the file; for getMany the folder to list, for upload the folder the files go into.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **If a row is rejected**
     - No
     - stop fails the run at the first rejected row. continue writes the rest and marks that row failed in result\_status and result\_error. Choices: ``stop``, ``continue``. Default: ``stop``.

Fields to set
-------------

Each row that arrives is written to Google Drive. When its columns already have these names, leave **Fields to set** empty. Otherwise click the chip of a field to add it, then type its value or click one under **What arrives here**.

.. list-table::
   :header-rows: 1
   :widths: 24 22 54
   :class: tool-params

   * - Field
     - Column name
     - Example or hint
   * - **File path**
     - ``path``
     - ``/home/sparkflows/.fireagent/gmail_attachments/INV-1001/invoice.pdf``
   * - **Name in Drive**
     - ``name``
     - ``Invoice INV-1001.pdf``
   * - **Convert to**
     - ``mimeType``
     - ``application/vnd.google-apps.document``

What it passes on
-----------------

Every row comes out with three columns added, so the next step can route on them:

.. list-table::
   :header-rows: 1
   :widths: 26 74
   :class: tool-table

   * - Column
     - Value
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``
   * - ``result_id``
     - The id Google Drive gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Upload a file** only when a request needs it, add the :doc:`Upload a file tool </agentic-ai-guide/tools-integrations/connector-tools/google-drive/file-upload>` to an Agent Node.

Other File actions
------------------

.. raw:: html

   <div class="tool-related"><a href="file-get.html">Get a file</a><a href="file-getmany.html">List files</a><a href="file-search.html">Search files</a><a href="file-download.html">Download a file</a><a href="file-create.html">Create a file or folder</a><a href="file-update.html">Update a file</a><a href="file-copy.html">Copy a file</a><a href="file-delete.html">Delete a file permanently</a></div>
