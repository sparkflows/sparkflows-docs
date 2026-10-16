:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Channel Message</p>

Post a channel message
======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Channel Message</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_channel_message_send</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Posts a new message in a channel and returns it with its id and webUrl; the text is sent as HTML. Microsoft Graph posts only for a signed-in user, so the connection needs a user (delegated) access token; with app-only credentials the call is refused before anything is sent.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.
* The account behind the connection must be allowed to change this data in Microsoft Teams.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **send** in the **Channel Message** row, then click **Add to agent**.

The agent now sees ``msteams_channel_message_send`` and calls it when a request needs it.

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
   * - ``text``
     - text
     - Yes
     - The message, as plain text or HTML such as <b>bold</b>, with <br> for a line break. Example: The release notes are ready for review..
   * - ``subject``
     - text
     - No
     - An optional subject line shown above the post. Example: Release 4.2.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Microsoft Teams.

Need it on every run?
---------------------

To run **Post a channel message** every time a flow reaches it, without the agent deciding, use the :doc:`Post a channel message App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/channel-message-send>`.

Other Channel Message tools
---------------------------

.. raw:: html

   <div class="tool-related"><a href="channel-message-getmany.html">List channel messages</a><a href="channel-message-replies.html">List replies to a post</a></div>
