:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../slack.html">Slack</a> › Channel</p>

List channels
=============

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

   Lists the workspace's channels with id, name, is\_private, is\_archived, topic, purpose and num\_members.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/slack>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Slack**.
#. **Action:** under **Channel**, choose **List channels**.
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
   * - **Channel created**
     - Reports each channel created since the last check, among the first 500 the workspace lists.

Let an agent decide instead
---------------------------

To let an agent call **List channels** only when a request needs it, add the :doc:`List channels tool </agentic-ai-guide/tools-integrations/connector-tools/slack/channel-getmany>` to an Agent Node.

Other Channel actions
---------------------

.. raw:: html

   <div class="tool-related"><a href="channel-get.html">Get a channel</a><a href="channel-history.html">Read channel history</a><a href="channel-replies.html">Read thread replies</a><a href="channel-members.html">List channel members</a><a href="channel-create.html">Create a channel</a><a href="channel-invite.html">Invite members to a channel</a><a href="channel-kick.html">Remove a member from a channel</a><a href="channel-join.html">Join a channel</a><a href="channel-leave.html">Leave a channel</a><a href="channel-archive.html">Archive a channel</a><a href="channel-unarchive.html">Unarchive a channel</a><a href="channel-rename.html">Rename a channel</a><a href="channel-settopic.html">Set a channel topic</a><a href="channel-setpurpose.html">Set a channel purpose</a></div>
