:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Channel Message</p>

List replies to a post
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Channel Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/microsoft-teams.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the replies to one channel post with id, from, body (HTML) and createdDateTime. The post's id comes from Channel Message getMany, which can also return every post with its replies when expand is replies.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Microsoft Teams prerequisites <../microsoft-teams>`.

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
   * - ``teamId``
     - Team
     - text
     - Yes
     - The team id (a GUID), from Team getMany. Example: b1f0c3d2-1234-4c5d-9e8f-0a1b2c3d4e5f.
   * - ``channelId``
     - Channel
     - text
     - Yes
     - The channel id, for example 19:a1b2c3d4e5f6@thread.tacv2, from Channel getMany.
   * - ``messageId``
     - Post
     - text
     - Yes
     - The id of the post whose replies to list, from Channel Message getMany. Example: 1616965872395.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many replies at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **replies** in the **Channel Message** row. The model sees it as ``msteams_channel_message_replies``.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **List replies to a post**, and fill in the inputs above. It runs every time the flow reaches it.

Other Channel Message tools
---------------------------

.. raw:: html

   <div class="tool-related"><a href="channel-message-getmany.html">List channel messages</a><a href="channel-message-send.html">Post a channel message</a></div>
