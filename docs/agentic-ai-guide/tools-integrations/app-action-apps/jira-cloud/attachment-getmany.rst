:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../jira-cloud.html">Jira</a> › Attachment</p>

List an issue's attachments
===========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Jira</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the files attached to an issue, each with its id, file name, size, MIME type, author, created time and content URL. Use it to find the attachment id that Attachment get and Attachment delete need.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/jira-cloud>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Jira**.
#. **Action:** under **Attachment**, choose **List an issue's attachments**.
#. **Details:** choose your Jira connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Jira** so later steps can use the columns, then **Save action**.

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
   * - **Issue key**
     - No
     - The issue key, for example FIN-12 (or the attachment id, project key or sprint id where the operation names one).
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``summary, status, assignee, priority``.

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
     - Some records keep a value inside another value, such as a priority inside an issue. This decides how those inner values become columns.

       * ``deep`` (default): Every inner value gets its own column, named with dots, such as ``fields.priority.name``.
       * ``oneLevel``: Only the first level is split. Anything deeper stays in one column as JSON text.
       * ``json``: Each inner value stays whole, in one column of JSON text.

       See the example below the table.

**Nested fields, by example.** Take a record ``{"id": 7, "fields": {"priority": {"name": "High"}}}``. Each choice gives you these columns:

.. list-table::
   :header-rows: 1
   :widths: 20 80
   :class: tool-table

   * - Choice
     - Columns you get
   * - ``deep``
     - ``id`` = ``7`` and ``fields.priority.name`` = ``High``
   * - ``oneLevel``
     - ``id`` = ``7`` and ``fields.priority`` = ``{"name": "High"}``
   * - ``json``
     - ``id`` = ``7`` and ``fields`` = ``{"priority": {"name": "High"}}``

Keep ``deep`` unless a later step needs the whole inner value as JSON.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Jira** to see the columns before you save.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Jira with this action and start the flow when something new turns up. Pick **Jira** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Attachment added to an issue**
     - Issue key is the issue to watch, for example FIN-12. Reports each file attached to it since the last check, with its name, size, type, author and content address.

Let an agent decide instead
---------------------------

To let an agent call **List an issue's attachments** only when a request needs it, add the :doc:`List an issue's attachments tool </agentic-ai-guide/tools-integrations/connector-tools/jira-cloud/attachment-getmany>` to an Agent Node.

Other Attachment actions
------------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-get.html">Get an attachment&#x27;s details</a><a href="attachment-delete.html">Delete an attachment</a></div>
