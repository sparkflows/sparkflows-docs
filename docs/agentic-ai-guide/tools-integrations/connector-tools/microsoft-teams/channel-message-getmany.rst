:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Channel Message</p>

List channel messages
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Channel Message</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_channel_message_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the top-level posts of a channel with id, from, subject, body (HTML), createdDateTime and webUrl; replies are left out unless expand is replies. An app-only connection needs the ChannelMessage.Read.All permission.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **list** in the **Channel Message** row, then click **Add to agent**.

The agent now sees ``msteams_channel_message_getmany`` and calls it when a request needs it.

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
   * - ``teamId``
     - text
     - Yes
     - The team id (a GUID), from Team getMany. Example: b1f0c3d2-1234-4c5d-9e8f-0a1b2c3d4e5f.
   * - ``channelId``
     - text
     - Yes
     - The channel id, for example 19:a1b2c3d4e5f6@thread.tacv2, from Channel getMany.
   * - ``expand``
     - text
     - No
     - replies adds each post's replies to its row.
   * - ``limit``
     - whole number
     - No
     - How many posts at most. Default: 50.

Need it on every run?
---------------------

To run **List channel messages** every time a flow reaches it, without the agent deciding, use the :doc:`List channel messages App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/channel-message-getmany>`.

Other Channel Message tools
---------------------------

.. raw:: html

   <div class="tool-related"><a href="channel-message-send.html">Post a channel message</a><a href="channel-message-replies.html">List replies to a post</a></div>
