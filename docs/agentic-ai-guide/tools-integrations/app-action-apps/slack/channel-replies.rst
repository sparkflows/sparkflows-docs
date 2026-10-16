:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../slack.html">Slack</a> › Channel</p>

Read thread replies
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one thread: the parent message followed by its replies, oldest first, each with ts, user and text.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/slack>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Slack**.
#. **Action:** under **Channel**, choose **Read thread replies**.
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
   * - **Channel**
     - No
     - The channel's id, which a Channel list returns. Posting a message also takes a name such as #general; reading a channel takes only the id. For example ``C0123ABC, the channel id``.
   * - **Message, user or file id**
     - No
     - The message timestamp (ts) for message operations, the user id for user operations, the file id for file operations. For example ``1712345678.000100 (a message ts) or U0123ABC``.
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
   * - **Reply posted in a thread**
     - Channel is the channel id, for example C0123ABC, which a Channel list returns, and Thread ts the ts of the thread's first message, for example 1712345678.000100. Reports each reply posted in the thread since the last check.

Let an agent decide instead
---------------------------

To let an agent call **Read thread replies** only when a request needs it, add the :doc:`Read thread replies tool </agentic-ai-guide/tools-integrations/connector-tools/slack/channel-replies>` to an Agent Node.

Other Channel actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="channel-get.html">Get a channel</a><a href="channel-getmany.html">List channels</a><a href="channel-history.html">Read channel history</a><a href="channel-members.html">List channel members</a><a href="channel-create.html">Create a channel</a><a href="channel-invite.html">Invite members to a channel</a><a href="channel-kick.html">Remove a member from a channel</a><a href="channel-join.html">Join a channel</a><a href="channel-leave.html">Leave a channel</a><a href="channel-archive.html">Archive a channel</a><a href="channel-unarchive.html">Unarchive a channel</a><a href="channel-rename.html">Rename a channel</a><a href="channel-settopic.html">Set a channel topic</a><a href="channel-setpurpose.html">Set a channel purpose</a></div>
