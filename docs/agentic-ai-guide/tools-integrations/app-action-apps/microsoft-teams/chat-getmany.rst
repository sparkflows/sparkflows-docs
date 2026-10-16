:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Chat</p>

List chats
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Chat</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists one-on-one, group and meeting chats with id, topic, chatType, createdDateTime and lastUpdatedDateTime.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/microsoft-teams>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Microsoft Teams**.
#. **Action:** under **Chat**, choose **List chats**.
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
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}. For example ``{"$top": "50"}``.
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Microsoft Teams** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Microsoft Teams with this action and start the flow when something new turns up. Pick **Microsoft Teams** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Chat started**
     - User is the person whose chats to watch, as an address or a user id. Reports each new one-on-one, group or meeting chat that person takes part in.

Let an agent decide instead
---------------------------

To let an agent call **List chats** only when a request needs it, add the :doc:`List chats tool </agentic-ai-guide/tools-integrations/connector-tools/microsoft-teams/chat-getmany>` to an Agent Node.

Other Chat actions
------------------

.. raw:: html

   <div class="tool-related"><a href="chat-get.html">Get a chat</a><a href="chat-messages.html">List chat messages</a><a href="chat-send.html">Send a chat message</a></div>
