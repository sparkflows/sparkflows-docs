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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Searches messages across the workspace with Slack's search syntax and returns the matches, best first, with text, user, username, channel, ts and permalink. It needs a user token (xoxp-); a bot token is refused with not\_allowed\_token\_type. To read one channel in time order use Channel history.

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
   * - ``query``
     - Search
     - text
     - Yes
     - Slack search syntax: words plus modifiers such as in:#releases, from:@asha, has:link, before:2026-10-01, after:2026-09-01, during:september. Example: deploy in:#releases after:2026-09-01.
   * - ``sort``
     - Sort by
     - text
     - No
     - score orders by relevance (the default), timestamp by date. One of: score, timestamp.
   * - ``sortDir``
     - Direction
     - text
     - No
     - desc (the default) or asc. One of: desc, asc.
   * - ``fields``
     - Columns to return
     - list of text
     - No
     - Columns to keep, for example ["text", "user"]; a dotted name reaches inside an object, such as profile.email. Blank keeps them all. Example: text,username,permalink.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many matches at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **search** in the **Message** row. The model sees it as ``slack_message_search``.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **Search messages**, and fill in the inputs above. It runs every time the flow reaches it.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-send.html">Send a message</a><a href="message-update.html">Update a message</a><a href="message-delete.html">Delete a message</a><a href="message-sendephemeral.html">Send an ephemeral message</a><a href="message-getpermalink.html">Get a message link</a></div>
