:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › Message</p>

Delete a message
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>Message</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_message_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes a message from a channel. A bot token deletes only the app's own messages; a user token deletes whatever that user may delete.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.
* The account behind the connection must be allowed to change this data in Slack.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **delete** in the **Message** row, then click **Add to agent**.

The agent now sees ``slack_message_delete`` and calls it when a request needs it.

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
     - The ts of the message to delete, for example 1712345678.000100; Channel history lists it.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Slack.

Need it on every run?
---------------------

To run **Delete a message** every time a flow reaches it, without the agent deciding, use the :doc:`Delete a message App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/message-delete>`.

Other Message tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="message-send.html">Send a message</a><a href="message-update.html">Update a message</a><a href="message-sendephemeral.html">Send an ephemeral message</a><a href="message-getpermalink.html">Get a message link</a><a href="message-search.html">Search messages</a></div>
