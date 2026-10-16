:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Message</p>

Get a message link
==================

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

   Returns the permanent link (permalink) to one message, for sharing or citing it outside Slack. Needs the channel ID and the message ts, both returned by Channel history and Message search.

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
   * - ``channel``
     - Channel
     - text
     - Yes
     - The ID of the channel that holds the message, for example C0123ABC.
   * - ``messageTs``
     - Message ts
     - text
     - Yes
     - The ts of the message, for example 1712345678.000100; Channel history and Message search return it.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **getPermalink** in the **Message** row. The model sees it as ``slack_message_getpermalink``.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **Get a message link**, and fill in the inputs above. It runs every time the flow reaches it.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-send.html">Send a message</a><a href="message-update.html">Update a message</a><a href="message-delete.html">Delete a message</a><a href="message-sendephemeral.html">Send an ephemeral message</a><a href="message-search.html">Search messages</a></div>
