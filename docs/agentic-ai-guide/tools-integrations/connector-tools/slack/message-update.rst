:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Message</p>

Update a message
================

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

   Changes the text of a message the app posted earlier and returns the updated message. A bot token can edit only the app's own messages; to post a new message instead use Message send.

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
     - The ID of the channel that holds the message, for example C0123ABC.
   * - ``messageTs``
     - Message ts
     - text
     - Yes
     - The ts of the message to change, for example 1712345678.000100; Message send returns it and Channel history lists it.
   * - ``text``
     - New text
     - text
     - Yes
     - The message text in Slack mrkdwn: \*bold\*, \_italic\_, \`code\`, <https://example.com\|a link>, <@U0123ABC> to mention someone. Example: Build 42 finished: 2 tests failed..
   * - ``blocks``
     - Blocks
     - list of JSON object
     - No
     - Block Kit layout blocks for a formatted message, for example [{"type": "section", "text": {"type": "mrkdwn", "text": "\*Deploy done\*"}}]; text is then the notification fallback.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **update** in the **Message** row. The model sees it as ``slack_message_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **Update a message**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-send.html">Send a message</a><a href="message-delete.html">Delete a message</a><a href="message-sendephemeral.html">Send an ephemeral message</a><a href="message-getpermalink.html">Get a message link</a><a href="message-search.html">Search messages</a></div>
