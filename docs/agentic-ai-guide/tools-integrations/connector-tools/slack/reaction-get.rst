:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Reaction</p>

Get a message's reactions
=========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Reaction</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one message with its reactions: each emoji name, its count and the users who added it. Needs the channel ID and the message's ts.

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
   * - ``full``
     - Every user
     - true or false
     - No
     - true lists every user of each reaction, not only the first ones.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **get** in the **Reaction** row. The model sees it as ``slack_reaction_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **Get a message's reactions**, and fill in the inputs above. It runs every time the flow reaches it.

Other Reaction tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="reaction-add.html">Add a reaction</a><a href="reaction-remove.html">Remove a reaction</a></div>
