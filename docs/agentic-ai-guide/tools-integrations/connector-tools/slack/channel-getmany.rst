:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Channel</p>

List channels
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_channel_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the workspace's channels with id, name, is\_private, is\_archived, topic, purpose and num\_members. Use it to find a channel ID from its name; only public channels are listed unless types says otherwise, and private ones only where the app is a member.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **list** in the **Channel** row, then click **Add to agent**.

The agent now sees ``slack_channel_getmany`` and calls it when a request needs it.

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
   * - ``types``
     - text
     - No
     - Comma-separated kinds to list: public\_channel, private\_channel, mpim (group direct messages), im (direct messages). Default public\_channel. Example: public\_channel,private\_channel.
   * - ``excludeArchived``
     - true or false
     - No
     - true leaves archived channels out.
   * - ``fields``
     - list of text
     - No
     - Columns to keep, for example ["text", "user"]; a dotted name reaches inside an object, such as profile.email. Blank keeps them all. Example: id,name,is\_private,num\_members.
   * - ``limit``
     - whole number
     - No
     - How many channels at most; raise it to find one channel by name in a large workspace. Default: 50.

Need it on every run?
---------------------

To run **List channels** every time a flow reaches it, without the agent deciding, use the :doc:`List channels App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/channel-getmany>`.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-get.html">Get a channel</a><a href="channel-history.html">Read channel history</a><a href="channel-replies.html">Read thread replies</a><a href="channel-members.html">List channel members</a><a href="channel-create.html">Create a channel</a><a href="channel-invite.html">Invite members to a channel</a><a href="channel-kick.html">Remove a member from a channel</a><a href="channel-join.html">Join a channel</a><a href="channel-leave.html">Leave a channel</a><a href="channel-archive.html">Archive a channel</a><a href="channel-unarchive.html">Unarchive a channel</a><a href="channel-rename.html">Rename a channel</a><a href="channel-settopic.html">Set a channel topic</a><a href="channel-setpurpose.html">Set a channel purpose</a></div>
