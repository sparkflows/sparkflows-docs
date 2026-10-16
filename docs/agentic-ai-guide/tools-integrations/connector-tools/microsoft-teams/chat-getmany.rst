:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Chat</p>

List chats
==========

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

   Lists one-on-one, group and meeting chats with id, topic, chatType, createdDateTime and lastUpdatedDateTime. With user set it lists that user's chats, which is what an app-only connection needs; blank lists the chats of the signed-in user of a delegated token.

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
   * - ``user``
     - User
     - text
     - No
     - The user whose chats to list: a user id or user principal name, for example someone@company.com. Required with an app-only connection.
   * - ``expand``
     - Include
     - text
     - No
     - members adds each chat's members; lastMessagePreview adds its latest message. One of: members, lastMessagePreview.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many chats at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **list** in the **Chat** row. The model sees it as ``msteams_chat_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **List chats**, and fill in the inputs above. It runs every time the flow reaches it.

Other Chat tools
----------------

.. raw:: html

   <div class="tool-related"><a href="chat-get.html">Get a chat</a><a href="chat-messages.html">List chat messages</a><a href="chat-send.html">Send a chat message</a></div>
