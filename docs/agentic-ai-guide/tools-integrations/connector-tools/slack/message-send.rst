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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_message_send</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Posts a message to a channel, a private channel or a person's direct message with the app, and returns the posted message with its ts, the id later operations use. Set threadTs to reply in a thread; to change a posted message use Message update, and to show a message to one member only use Message sendEphemeral.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.
* The account behind the connection must be allowed to change this data in Slack.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **send** in the **Message** row, then click **Add to agent**.

The agent now sees ``slack_message_send`` and calls it when a request needs it.

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
     - Where to post: a channel ID (C0123ABC), a channel name such as #general, or a user ID (U0123ABC) for a direct message from the app.
   * - ``text``
     - text
     - Yes
     - The message text in Slack mrkdwn: \*bold\*, \_italic\_, \`code\`, <https://example.com\|a link>, <@U0123ABC> to mention someone. Example: Build 42 finished: all tests passed..
   * - ``threadTs``
     - text
     - No
     - The ts of the parent message, to post this as a reply in its thread; Channel history and Message search return it. Example: 1712345678.000100.
   * - ``replyBroadcast``
     - true or false
     - No
     - With threadTs, true also shows the reply in the channel itself.
   * - ``blocks``
     - list of JSON object
     - No
     - Block Kit layout blocks for a formatted message, for example [{"type": "section", "text": {"type": "mrkdwn", "text": "\*Deploy done\*"}}]; text is then the notification fallback.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Slack.

Need it on every run?
---------------------

To run **Send a message** every time a flow reaches it, without the agent deciding, use the :doc:`Send a message App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/message-send>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-update.html">Update a message</a><a href="message-delete.html">Delete a message</a><a href="message-sendephemeral.html">Send an ephemeral message</a><a href="message-getpermalink.html">Get a message link</a><a href="message-search.html">Search messages</a></div>
