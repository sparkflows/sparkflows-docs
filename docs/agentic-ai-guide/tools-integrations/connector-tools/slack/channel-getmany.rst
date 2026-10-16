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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the workspace's channels with id, name, is\_private, is\_archived, topic, purpose and num\_members. Use it to find a channel ID from its name; only public channels are listed unless types says otherwise, and private ones only where the app is a member.

Prerequisites
-------------

* **Connection:** Slack connection. See :doc:`the Slack prerequisites <../slack>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``types``
     - Channel types
     - text
     - No
     - Comma-separated kinds to list: public\_channel, private\_channel, mpim (group direct messages), im (direct messages). Default public\_channel. Example: public\_channel,private\_channel.
   * - ``excludeArchived``
     - Leave out archived
     - true or false
     - No
     - true leaves archived channels out.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Columns to keep, for example ["text", "user"]; a dotted name reaches inside an object, such as profile.email. Blank keeps them all. Example: id,name,is\_private,num\_members.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many channels at most; raise it to find one channel by name in a large workspace. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **list** in the **Channel** row. The model sees it as ``slack_channel_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **List channels**, and fill in the inputs above. It runs every time the flow reaches it.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-get.html">Get a channel</a><a href="channel-history.html">Read channel history</a><a href="channel-replies.html">Read thread replies</a><a href="channel-members.html">List channel members</a><a href="channel-create.html">Create a channel</a><a href="channel-invite.html">Invite members to a channel</a><a href="channel-kick.html">Remove a member from a channel</a><a href="channel-join.html">Join a channel</a><a href="channel-leave.html">Leave a channel</a><a href="channel-archive.html">Archive a channel</a><a href="channel-unarchive.html">Unarchive a channel</a><a href="channel-rename.html">Rename a channel</a><a href="channel-settopic.html">Set a channel topic</a><a href="channel-setpurpose.html">Set a channel purpose</a></div>
