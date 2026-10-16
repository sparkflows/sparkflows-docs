:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Chat</p>

List chat messages
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Chat</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_chat_messages</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the messages of one chat, most recently changed first, with id, from, body (HTML) and createdDateTime. An app-only connection needs the Chat.Read.All permission.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **messages** in the **Chat** row, then click **Add to agent**.

The agent now sees ``msteams_chat_messages`` and calls it when a request needs it.

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
   * - ``chatId``
     - text
     - Yes
     - The chat id, for example 19:2da4c29f6d7041eca70b638b43d45437@thread.v2, from Chat getMany.
   * - ``limit``
     - whole number
     - No
     - How many messages at most. Default: 50.

Need it on every run?
---------------------

To run **List chat messages** every time a flow reaches it, without the agent deciding, use the :doc:`List chat messages App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/chat-messages>`.

Other Chat tools
----------------

.. raw:: html

   <div class="tool-related"><a href="chat-getmany.html">List chats</a><a href="chat-get.html">Get a chat</a><a href="chat-send.html">Send a chat message</a></div>
