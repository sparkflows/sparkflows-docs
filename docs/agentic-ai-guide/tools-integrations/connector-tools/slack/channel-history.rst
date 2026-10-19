:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Channel</p>

Read channel history
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_channel_history</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the messages of one channel, newest first, each with ts, user, text, thread\_ts and reply\_count; thread replies are not included. Use oldest and latest to read a time window, and Channel replies to read a thread. The app must be a member of the channel.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **history** in the **Channel** row, then click **Add to agent**.

The agent now sees ``slack_channel_history`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``channel``
     - text
     - Yes
     - The channel ID, for example C0123ABC; Channel getMany finds it from the channel's name.
   * - ``oldest``
     - text
     - No
     - Only messages after this time, as Unix seconds or a message ts. Example: 1788220800.
   * - ``latest``
     - text
     - No
     - Only messages before this time, as Unix seconds or a message ts. Example: 1790812800.
   * - ``fields``
     - list of text
     - No
     - Columns to keep, for example ["text", "user"]; a dotted name reaches inside an object, such as profile.email. Blank keeps them all. Example: ts,user,text,reply\_count.
   * - ``limit``
     - whole number
     - No
     - How many messages at most. Default: 50.

Need it on every run?
---------------------

To run **Read channel history** every time a flow reaches it, without the agent deciding, use the :doc:`Read channel history App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/channel-history>`.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-get.html">Get a channel</a><a href="channel-getmany.html">List channels</a><a href="channel-replies.html">Read thread replies</a><a href="channel-members.html">List channel members</a><a href="channel-create.html">Create a channel</a><a href="channel-invite.html">Invite members to a channel</a><a href="channel-kick.html">Remove a member from a channel</a><a href="channel-join.html">Join a channel</a><a href="channel-leave.html">Leave a channel</a><a href="channel-archive.html">Archive a channel</a><a href="channel-unarchive.html">Unarchive a channel</a><a href="channel-rename.html">Rename a channel</a><a href="channel-settopic.html">Set a channel topic</a><a href="channel-setpurpose.html">Set a channel purpose</a></div>
