:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Channel</p>

List channel members
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the members of one channel with displayName, email, userId and roles.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/microsoft-teams>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Microsoft Teams**.
#. **Action:** under **Channel**, choose **List channel members**.
#. **Details:** choose your Microsoft Graph connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Microsoft Teams** so later steps can use the columns, then **Save action**.

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
   * - **Target**
     - No
     - The team to act on: its id. List the teams first and click a team's id on the left to put it here.
   * - **Item id**
     - No
     - The channel, chat, meeting or message to act on: its id, from a list step before this one.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``id, displayName``.
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
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}.
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

The records come out as rows, one per record. Click **Load the fields from Microsoft Teams** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Let an agent decide instead
---------------------------

To let an agent call **List channel members** only when a request needs it, add the :doc:`List channel members tool </agentic-ai-guide/tools-integrations/connector-tools/microsoft-teams/channel-members>` to an Agent Node.

Other Channel actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="channel-getmany.html">List channels</a><a href="channel-get.html">Get a channel</a><a href="channel-create.html">Create a channel</a><a href="channel-delete.html">Delete a channel</a></div>
