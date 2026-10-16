:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Channel</p>

Get a channel
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_channel_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one channel's details: name, topic, purpose, created, creator, is\_private, is\_archived and, when asked, num\_members. The channel ID comes from Channel getMany.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **get** in the **Channel** row, then click **Add to agent**.

The agent now sees ``slack_channel_get`` and calls it when a request needs it.

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
   * - ``includeNumMembers``
     - true or false
     - No
     - true adds the number of members (num\_members).

Need it on every run?
---------------------

To run **Get a channel** every time a flow reaches it, without the agent deciding, use the :doc:`Get a channel App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/channel-get>`.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-getmany.html">List channels</a><a href="channel-history.html">Read channel history</a><a href="channel-replies.html">Read thread replies</a><a href="channel-members.html">List channel members</a><a href="channel-create.html">Create a channel</a><a href="channel-invite.html">Invite members to a channel</a><a href="channel-kick.html">Remove a member from a channel</a><a href="channel-join.html">Join a channel</a><a href="channel-leave.html">Leave a channel</a><a href="channel-archive.html">Archive a channel</a><a href="channel-unarchive.html">Unarchive a channel</a><a href="channel-rename.html">Rename a channel</a><a href="channel-settopic.html">Set a channel topic</a><a href="channel-setpurpose.html">Set a channel purpose</a></div>
