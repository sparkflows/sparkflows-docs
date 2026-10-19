:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Message</p>

Send an ephemeral message
=========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_message_sendephemeral</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Shows a message to one member of a channel only; nobody else sees it and Slack does not keep it. Returns the message\_ts. Use it for private hints or confirmations; for a message the whole channel sees use Message send.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.
* The account behind the connection must be allowed to change this data in Slack.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **sendEphemeral** in the **Message** row, then click **Add to agent**.

The agent now sees ``slack_message_sendephemeral`` and calls it when a request needs it.

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
     - The ID of the channel the member is in, for example C0123ABC.
   * - ``user``
     - text
     - Yes
     - The user ID (U0123ABC) of the member who sees the message; they must be in the channel. User lookupByEmail finds the ID from an email address.
   * - ``text``
     - text
     - Yes
     - The message text in Slack mrkdwn: \*bold\*, \_italic\_, \`code\`, <https://example.com\|a link>, <@U0123ABC> to mention someone. Example: Only you can see this: your report is ready..
   * - ``threadTs``
     - text
     - No
     - The ts of a thread's parent message, to show the message inside that thread. Example: 1712345678.000100.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Slack.

Need it on every run?
---------------------

To run **Send an ephemeral message** every time a flow reaches it, without the agent deciding, use the :doc:`Send an ephemeral message App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/message-sendephemeral>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-send.html">Send a message</a><a href="message-update.html">Update a message</a><a href="message-delete.html">Delete a message</a><a href="message-getpermalink.html">Get a message link</a><a href="message-search.html">Search messages</a></div>
