:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Message</p>

Search messages
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_message_search</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Searches messages across the workspace with Slack's search syntax and returns the matches, best first, with text, user, username, channel, ts and permalink. It needs a user token (xoxp-); a bot token is refused with not\_allowed\_token\_type. To read one channel in time order use Channel history.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **search** in the **Message** row, then click **Add to agent**.

The agent now sees ``slack_message_search`` and calls it when a request needs it.

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
   * - ``query``
     - text
     - Yes
     - Slack search syntax: words plus modifiers such as in:#releases, from:@asha, has:link, before:2026-10-01, after:2026-09-01, during:september. Example: deploy in:#releases after:2026-09-01.
   * - ``sort``
     - text
     - No
     - score orders by relevance (the default), timestamp by date. One of: score, timestamp.
   * - ``sortDir``
     - text
     - No
     - desc (the default) or asc. One of: desc, asc.
   * - ``fields``
     - list of text
     - No
     - Columns to keep, for example ["text", "user"]; a dotted name reaches inside an object, such as profile.email. Blank keeps them all. Example: text,username,permalink.
   * - ``limit``
     - whole number
     - No
     - How many matches at most. Default: 50.

Need it on every run?
---------------------

To run **Search messages** every time a flow reaches it, without the agent deciding, use the :doc:`Search messages App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/message-search>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-send.html">Send a message</a><a href="message-update.html">Update a message</a><a href="message-delete.html">Delete a message</a><a href="message-sendephemeral.html">Send an ephemeral message</a><a href="message-getpermalink.html">Get a message link</a></div>
