:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Chat</p>

Send a chat message
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Chat</dd></div>
     <div><dt>Type</dt><dd>Changes data</dd></div>
     <div><dt>Passes on</dt><dd>Your rows, with the result of each write</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sends a message in an existing chat and returns it with its id; the text is sent as HTML. Graph sends only for a signed-in user, so the connection needs a user (delegated) access token; with app-only credentials the call is refused before anything is sent.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/microsoft-teams>`.
* The account behind the connection must be allowed to change this data in Microsoft Teams.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Microsoft Teams**.
#. **Action:** under **Chat**, choose **Send a chat message**.
#. **Details:** choose your Microsoft Graph connection, click **Test**, then fill in the boxes below.
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
   * - **Item id**
     - No
     - The channel, chat, meeting or message to act on: its id, from a list step before this one.

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

Each row that arrives is written to Microsoft Teams. When its columns already have these names, leave **Fields to set** empty. Otherwise click the chip of a field to add it, then type its value or click one under **What arrives here**.

.. list-table::
   :header-rows: 1
   :widths: 24 22 54
   :class: tool-params

   * - Field
     - Column name
     - Example or hint
   * - **Message**
     - ``text``
     - ``Can we move the review to 3pm?``

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
     - The id Microsoft Teams gave the record
   * - ``result_error``
     - Why the row failed, if it did

Add a **Filter** on ``result_status = 'failed'`` to collect the rows that failed.

.. important::

   Running from the canvas is a preview: the write is skipped and ``result_status`` is ``skipped``. A full or scheduled run writes for real.

Let an agent decide instead
---------------------------

To let an agent call **Send a chat message** only when a request needs it, add the :doc:`Send a chat message tool </agentic-ai-guide/tools-integrations/connector-tools/microsoft-teams/chat-send>` to an Agent Node.

Other Chat actions
------------------

.. raw:: html

   <div class="tool-related"><a href="chat-getmany.html">List chats</a><a href="chat-get.html">Get a chat</a><a href="chat-messages.html">List chat messages</a></div>
