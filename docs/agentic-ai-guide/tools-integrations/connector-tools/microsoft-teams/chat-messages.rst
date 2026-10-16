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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/microsoft-teams.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the messages of one chat, most recently changed first, with id, from, body (HTML) and createdDateTime. An app-only connection needs the Chat.Read.All permission.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Microsoft Teams prerequisites <../microsoft-teams>`.

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
   * - ``chatId``
     - Chat
     - text
     - Yes
     - The chat id, for example 19:2da4c29f6d7041eca70b638b43d45437@thread.v2, from Chat getMany.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many messages at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **messages** in the **Chat** row. The model sees it as ``msteams_chat_messages``.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **List chat messages**, and fill in the inputs above. It runs every time the flow reaches it.

Other Chat tools
----------------

.. raw:: html

   <div class="tool-related"><a href="chat-getmany.html">List chats</a><a href="chat-get.html">Get a chat</a><a href="chat-send.html">Send a chat message</a></div>
