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
     <div><dt>Tool name</dt><dd><code>slack_reaction_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one message with its reactions: each emoji name, its count and the users who added it. Needs the channel ID and the message's ts.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **get** in the **Reaction** row, then click **Add to agent**.

The agent now sees ``slack_reaction_get`` and calls it when a request needs it.

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
     - The ID of the channel that holds the message, for example C0123ABC.
   * - ``messageTs``
     - text
     - Yes
     - The ts of the message, for example 1712345678.000100; Channel history and Message search return it.
   * - ``full``
     - true or false
     - No
     - true lists every user of each reaction, not only the first ones.

Need it on every run?
---------------------

To run **Get a message's reactions** every time a flow reaches it, without the agent deciding, use the :doc:`Get a message's reactions App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/reaction-get>`.

Other Reaction tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="reaction-add.html">Add a reaction</a><a href="reaction-remove.html">Remove a reaction</a></div>
