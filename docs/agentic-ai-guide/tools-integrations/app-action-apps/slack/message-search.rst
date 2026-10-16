:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../slack.html">Slack</a> › Message</p>

Search messages
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Searches messages across the workspace with Slack's search syntax and returns the matches, best first, with text, user, username, channel, ts and permalink.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/slack>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Slack**.
#. **Action:** under **Message**, choose **Search messages**.
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
   * - **Search text**
     - No
     - Slack's search box syntax: words, in:#channel, from:@person, has:link, before:2026-10-01. For example ``deploy in:#releases from:@asha``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``text, user, ts``.
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

The records come out as rows, one per record. Click **Load the fields from Slack** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Slack with this action and start the flow when something new turns up. Pick **Slack** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Message matching a search**
     - Search text takes Slack's search syntax, for example deploy in:#releases from:@asha. Reports each new message in the workspace that matches it. Searching needs a user token (xoxp-) on the connection.

Let an agent decide instead
---------------------------

To let an agent call **Search messages** only when a request needs it, add the :doc:`Search messages tool </agentic-ai-guide/tools-integrations/connector-tools/slack/message-search>` to an Agent Node.

Other Message actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="message-send.html">Send a message</a><a href="message-update.html">Update a message</a><a href="message-delete.html">Delete a message</a><a href="message-sendephemeral.html">Send an ephemeral message</a><a href="message-getpermalink.html">Get a message link</a></div>
