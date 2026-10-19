:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../slack.html">Slack</a> › User Group</p>

List user groups
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>User Group</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the workspace's user groups (the @handles that mention a team) with id, name, handle, description and, when asked, their user count and member IDs.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/slack>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Slack**.
#. **Action:** under **User Group**, choose **List user groups**.
#. **Details:** choose your Slack connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Slack** so later steps can use the columns, then **Save action**.

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
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``text, user, ts``.

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

The records come out as rows, one per record. Click **Load the fields from Slack** to see the columns before you save.

Let an agent decide instead
---------------------------

To let an agent call **List user groups** only when a request needs it, add the :doc:`List user groups tool </agentic-ai-guide/tools-integrations/connector-tools/slack/user-group-getmany>` to an Agent Node.

Other User Group actions
------------------------

.. raw:: html

   <div class="tool-related"><a href="user-group-create.html">Create a user group</a><a href="user-group-update.html">Update a user group</a><a href="user-group-enable.html">Enable a user group</a><a href="user-group-disable.html">Disable a user group</a></div>
