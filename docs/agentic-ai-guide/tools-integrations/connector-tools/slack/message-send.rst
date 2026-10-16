:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Message</p>

Send a message
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Posts a message to a channel, a private channel or a person's direct message with the app, and returns the posted message with its ts, the id later operations use. Set threadTs to reply in a thread; to change a posted message use Message update, and to show a message to one member only use Message sendEphemeral.

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
     - Where to post: a channel ID (C0123ABC), a channel name such as #general, or a user ID (U0123ABC) for a direct message from the app.
   * - ``text``
     - Message
     - text
     - Yes
     - The message text in Slack mrkdwn: \*bold\*, \_italic\_, \`code\`, <https://example.com\|a link>, <@U0123ABC> to mention someone. Example: Build 42 finished: all tests passed..
   * - ``threadTs``
     - Reply in thread
     - text
     - No
     - The ts of the parent message, to post this as a reply in its thread; Channel history and Message search return it. Example: 1712345678.000100.
   * - ``replyBroadcast``
     - Also send to channel
     - true or false
     - No
     - With threadTs, true also shows the reply in the channel itself.
   * - ``blocks``
     - Blocks
     - list of JSON object
     - No
     - Block Kit layout blocks for a formatted message, for example [{"type": "section", "text": {"type": "mrkdwn", "text": "\*Deploy done\*"}}]; text is then the notification fallback.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **send** in the **Message** row. The model sees it as ``slack_message_send``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **Send a message**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-update.html">Update a message</a><a href="message-delete.html">Delete a message</a><a href="message-sendephemeral.html">Send an ephemeral message</a><a href="message-getpermalink.html">Get a message link</a><a href="message-search.html">Search messages</a></div>
