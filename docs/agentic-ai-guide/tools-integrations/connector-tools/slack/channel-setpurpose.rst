:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Channel</p>

Set a channel purpose
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sets the channel's description (purpose) and returns the channel. The purpose is plain text up to 250 characters; the header topic is set with Channel setTopic.

Prerequisites
-------------

* **Connection:** Slack connection. See :doc:`the Slack prerequisites <../slack>`.
* The connection's account must be allowed to change this data in Slack.

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
   * - ``channel``
     - Channel
     - text
     - Yes
     - The channel ID, for example C0123ABC; Channel getMany finds it from the channel's name.
   * - ``purpose``
     - Purpose
     - text
     - Yes
     - The new description, plain text up to 250 characters. Example: Coordination for the Apollo launch..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **setPurpose** in the **Channel** row. The model sees it as ``slack_channel_setpurpose``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **Set a channel purpose**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-get.html">Get a channel</a><a href="channel-getmany.html">List channels</a><a href="channel-history.html">Read channel history</a><a href="channel-replies.html">Read thread replies</a><a href="channel-members.html">List channel members</a><a href="channel-create.html">Create a channel</a><a href="channel-invite.html">Invite members to a channel</a><a href="channel-kick.html">Remove a member from a channel</a><a href="channel-join.html">Join a channel</a><a href="channel-leave.html">Leave a channel</a><a href="channel-archive.html">Archive a channel</a><a href="channel-unarchive.html">Unarchive a channel</a><a href="channel-rename.html">Rename a channel</a><a href="channel-settopic.html">Set a channel topic</a></div>
