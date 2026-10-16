.. _app-action-slack:

.. rst-class:: agentic-tutorial

Slack App Actions
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Node</dt><dd>App Action</dd></div>
     <div><dt>Actions</dt><dd>37 across 6 resources</dd></div>
     <div><dt>Reads / changes data</dt><dd>16 / 21</dd></div>
     <div><dt>Connection</dt><dd>Slack · Bot Token</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Slack as a fixed workflow step: read channels and threads, look people up, and post messages. An App Action runs every time the flow reaches it, exactly as you set it; no model decides. To let an agent choose instead, use the :doc:`Slack agent tools </agentic-ai-guide/tools-integrations/connector-tools/slack>`.

.. contents:: On this page
   :local:
   :depth: 1
   :class: tool-toc

Prerequisites
-------------

* **Connection:** A **Slack** connection that holds one **Bot Token** (``xoxb-``). Sparkflows calls Slack's own API, so there is no URL or username to enter.
* A Slack app installed in the workspace, with its Bot User OAuth Token.
* The bot scopes for the operations you tick. Slack refuses a call whose scope is missing with ``missing_scope``.
* The app invited to each channel it reads or posts in, private channels included.
* How to create the connection: :ref:`connector-tools-slack`.

Add a Slack App Action
----------------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs in the flow.
#. **App:** choose **Slack**, or type ``slack`` in **Search apps**.
#. **Action:** pick one of the 37 actions below. Each is marked **reads** or **changes data**.
#. **Details:** choose the Slack connection and click **Test**, then fill in the inputs. Click a field under **What arrives here** to insert a value from an earlier step.
#. For a read, click **Load the fields** so later steps can use the columns it returns. Then click **Save action**.

.. figure:: ../../../_assets/agentic-ai-guide/tools/app-actions/slack-actions.png
   :alt: The Slack actions in the App Action Action step
   :width: 560px

   Step 2, **Action**, for Slack.

.. tip::

   A canvas run skips actions that change data unless **Write when run from the canvas** is on; full and scheduled runs always perform them. Every write hands on ``result_status``, ``result_id`` and ``result_error`` for each row. See :doc:`/agentic-ai-guide/tools-integrations/app-actions`.

Actions
-------

The inputs are the boxes on the **Details** step, by their label. Any input can take a value from an earlier step with a ``${...}`` reference.

Message
~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="slack/message-send.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Send a message</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Posts a message to a channel, a private channel or a person&#x27;s direct message with the app, and returns the posted message with its ts, the id later operations use.</span>
     </a>
     <a class="tool-op" href="slack/message-update.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Update a message</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Changes the text of a message the app posted earlier and returns the updated message.</span>
     </a>
     <a class="tool-op" href="slack/message-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a message</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Deletes a message from a channel.</span>
     </a>
     <a class="tool-op" href="slack/message-sendephemeral.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Send an ephemeral message</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Shows a message to one member of a channel only; nobody else sees it and Slack does not keep it.</span>
     </a>
     <a class="tool-op" href="slack/message-getpermalink.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a message link</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns the permanent link (permalink) to one message, for sharing or citing it outside Slack.</span>
     </a>
     <a class="tool-op" href="slack/message-search.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Search messages</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Searches messages across the workspace with Slack&#x27;s search syntax and returns the matches, best first, with text, user, username, channel, ts and permalink.</span>
     </a>
   </div>

Channel
~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="slack/channel-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a channel</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns one channel&#x27;s details: name, topic, purpose, created, creator, is_private, is_archived and, when asked, num_members.</span>
     </a>
     <a class="tool-op" href="slack/channel-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List channels</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists the workspace&#x27;s channels with id, name, is_private, is_archived, topic, purpose and num_members.</span>
     </a>
     <a class="tool-op" href="slack/channel-history.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Read channel history</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns the messages of one channel, newest first, each with ts, user, text, thread_ts and reply_count; thread replies are not included.</span>
     </a>
     <a class="tool-op" href="slack/channel-replies.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Read thread replies</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns one thread: the parent message followed by its replies, oldest first, each with ts, user and text.</span>
     </a>
     <a class="tool-op" href="slack/channel-members.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List channel members</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists the members of one channel, one row per member with the user ID in id.</span>
     </a>
     <a class="tool-op" href="slack/channel-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a channel</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Creates a public or private channel and returns it with its new ID; the app becomes its first member.</span>
     </a>
     <a class="tool-op" href="slack/channel-invite.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Invite members to a channel</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Adds up to 1,000 members to a channel and returns the channel.</span>
     </a>
     <a class="tool-op" href="slack/channel-kick.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Remove a member from a channel</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Removes one member from a channel.</span>
     </a>
     <a class="tool-op" href="slack/channel-join.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Join a channel</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Adds the app to a public channel so it can read and post there, and returns the channel.</span>
     </a>
     <a class="tool-op" href="slack/channel-leave.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Leave a channel</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Removes the app from a channel, so it stops reading and posting there.</span>
     </a>
     <a class="tool-op" href="slack/channel-archive.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Archive a channel</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Archives a channel: it becomes read-only and leaves the channel list, while its history is kept.</span>
     </a>
     <a class="tool-op" href="slack/channel-unarchive.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Unarchive a channel</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Reopens an archived channel so members can post in it again.</span>
     </a>
     <a class="tool-op" href="slack/channel-rename.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Rename a channel</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Renames a channel and returns it with the new name.</span>
     </a>
     <a class="tool-op" href="slack/channel-settopic.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Set a channel topic</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Sets the topic shown in the channel header and returns the channel.</span>
     </a>
     <a class="tool-op" href="slack/channel-setpurpose.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Set a channel purpose</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Sets the channel&#x27;s description (purpose) and returns the channel.</span>
     </a>
   </div>

User
~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="slack/user-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a user</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns one member&#x27;s account: id, name, real_name, profile (display name, email, title, phone), tz, is_admin, is_bot and deleted.</span>
     </a>
     <a class="tool-op" href="slack/user-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List users</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists the workspace&#x27;s members, bots and deactivated accounts included (deleted is true), with id, name, real_name, profile and tz.</span>
     </a>
     <a class="tool-op" href="slack/user-getprofile.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a user&#x27;s profile</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns a member&#x27;s profile: display_name, real_name, email, phone, title, status_text and status_emoji.</span>
     </a>
     <a class="tool-op" href="slack/user-getstatus.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a user&#x27;s presence</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns whether a member is active or away (presence) and, for the token&#x27;s own user, online and auto_away details.</span>
     </a>
     <a class="tool-op" href="slack/user-lookupbyemail.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Find a user by email</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Finds the member who uses an email address and returns their account with id, name, real_name and profile.</span>
     </a>
   </div>

File
~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="slack/file-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a file</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns one file&#x27;s details: name, title, filetype, size, user, created, permalink and the channels it was shared in.</span>
     </a>
     <a class="tool-op" href="slack/file-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List files</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists files shared in the workspace, newest first, with id, name, title, filetype, size, user, created and permalink; filter by channel, user, type or time.</span>
     </a>
     <a class="tool-op" href="slack/file-delete.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Delete a file</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Deletes a file from Slack for everyone.</span>
     </a>
   </div>

Reaction
~~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="slack/reaction-add.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Add a reaction</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Adds an emoji reaction to a message as the app, for example to acknowledge it.</span>
     </a>
     <a class="tool-op" href="slack/reaction-get.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Get a message&#x27;s reactions</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Returns one message with its reactions: each emoji name, its count and the users who added it.</span>
     </a>
     <a class="tool-op" href="slack/reaction-remove.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Remove a reaction</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Removes a reaction the app added to a message.</span>
     </a>
   </div>

User Group
~~~~~~~~~~

.. raw:: html

   <div class="tool-ops">
     <a class="tool-op" href="slack/user-group-getmany.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">List user groups</span><span class="tool-op-kind is-read">Reads</span></span>
       <span class="tool-op-desc">Lists the workspace&#x27;s user groups (the @handles that mention a team) with id, name, handle, description and, when asked, their user count and member IDs.</span>
     </a>
     <a class="tool-op" href="slack/user-group-create.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Create a user group</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Creates a user group, an @handle that mentions several people at once, and returns it with its ID (S0123ABC).</span>
     </a>
     <a class="tool-op" href="slack/user-group-update.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Update a user group</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Changes a user group&#x27;s name, handle, description or default channels and returns the group.</span>
     </a>
     <a class="tool-op" href="slack/user-group-enable.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Enable a user group</span><span class="tool-op-kind is-write">Changes data</span></span>
       <span class="tool-op-desc">Re-enables a disabled user group so its @handle works again, and returns the group.</span>
     </a>
     <a class="tool-op" href="slack/user-group-disable.html" target="_blank" rel="noopener">
       <span class="tool-op-head"><span class="tool-op-title">Disable a user group</span><span class="tool-op-kind is-delete">Changes data</span></span>
       <span class="tool-op-desc">Disables a user group: its @handle stops notifying anyone, while the group and its settings are kept.</span>
     </a>
   </div>

Start a flow from Slack
-----------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Slack and start the flow when one of these events happens. Pick Slack in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 34 66
   :class: tool-table

   * - Event
     - What it reports
   * - **Message posted in a channel**
     - Channel is the channel id, for example C0123ABC, which a Channel list returns. Reports each new message posted in the channel.
   * - **Message containing text**
     - Channel is the channel id, for example C0123ABC, which a Channel list returns, and Filter the text to look for, matched regardless of case. Reports each new message in the channel whose text contains it.
   * - **Member mentioned in a channel**
     - Channel is the channel id, for example C0123ABC, which a Channel list returns, and Filter the member's user id, for example U0123ABC. Reports each new message in the channel that mentions the member.
   * - **Message posted by a member**
     - Channel is the channel id, for example C0123ABC, which a Channel list returns, and Filter the member's user id, for example U0123ABC. Reports each new message the member posts in the channel.
   * - **Reply posted in a thread**
     - Channel is the channel id, for example C0123ABC, which a Channel list returns, and Thread ts the ts of the thread's first message, for example 1712345678.000100. Reports each reply posted in the thread since the last check.
   * - **Message matching a search**
     - Search text takes Slack's search syntax, for example deploy in:#releases from:@asha. Reports each new message in the workspace that matches it. Searching needs a user token (xoxp-) on the connection.
   * - **File shared**
     - Reports each file shared in the workspace since the last check, with its name, type, size, uploader and permalink. A bot token lists only the files the bot can see.
   * - **File shared in a channel**
     - Filter is the channel id, for example C0123ABC. Reports each file shared in that channel since the last check, with its name, type, size, uploader and permalink.
   * - **Reaction added or removed**
     - Channel is the channel id, for example C0123ABC, which a Channel list returns, and Message ts the message's ts, for example 1712345678.000100. Reports the message with every reaction and who added it, each time a reaction is added or removed.
   * - **Channel created**
     - Reports each channel created since the last check, among the first 500 the workspace lists.
   * - **Member joined a channel**
     - Channel is the channel id, for example C0123ABC, which a Channel list returns. The first check records the members; later checks report the user id of each member who joins.
   * - **Member joined the workspace**
     - The first check records the workspace's members; later checks report each person who joins, bots left out.
   * - **Member deactivated**
     - The first check records the accounts already deactivated; later checks report each member whose account is deactivated.

Related
-------

* :doc:`/agentic-ai-guide/tools-integrations/app-actions` - how App Actions work, reads, writes and safety
* :doc:`/agentic-ai-guide/tools-integrations/app-action-apps/index` - every App Action app
* :doc:`Slack agent tools </agentic-ai-guide/tools-integrations/connector-tools/slack>` - the same operations for an Agent Node, with every parameter
