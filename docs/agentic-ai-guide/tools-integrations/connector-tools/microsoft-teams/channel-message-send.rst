:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Channel Message</p>

Post a channel message
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Channel Message</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/microsoft-teams.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Posts a new message in a channel and returns it with its id and webUrl; the text is sent as HTML. Microsoft Graph posts only for a signed-in user, so the connection needs a user (delegated) access token; with app-only credentials the call is refused before anything is sent.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Microsoft Teams prerequisites <../microsoft-teams>`.
* The connection's account must be allowed to change this data in Microsoft Teams.

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
   * - ``text``
     - Message
     - text
     - Yes
     - The message, as plain text or HTML such as <b>bold</b>, with <br> for a line break. Example: The release notes are ready for review..
   * - ``subject``
     - Subject
     - text
     - No
     - An optional subject line shown above the post. Example: Release 4.2.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **send** in the **Channel Message** row. The model sees it as ``msteams_channel_message_send``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **Post a channel message**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Channel Message tools
---------------------------

.. raw:: html

   <div class="tool-related"><a href="channel-message-getmany.html">List channel messages</a><a href="channel-message-replies.html">List replies to a post</a></div>
