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
     <div><dt>Tool name</dt><dd><code>msteams_chat_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists one-on-one, group and meeting chats with id, topic, chatType, createdDateTime and lastUpdatedDateTime. With user set it lists that user's chats, which is what an app-only connection needs; blank lists the chats of the signed-in user of a delegated token.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **list** in the **Chat** row, then click **Add to agent**.

The agent now sees ``msteams_chat_getmany`` and calls it when a request needs it.

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
   * - ``user``
     - text
     - No
     - The user whose chats to list: a user id or user principal name, for example someone@company.com. Required with an app-only connection.
   * - ``expand``
     - text
     - No
     - members adds each chat's members; lastMessagePreview adds its latest message. One of: members, lastMessagePreview.
   * - ``limit``
     - whole number
     - No
     - How many chats at most. Default: 50.

Need it on every run?
---------------------

To run **List chats** every time a flow reaches it, without the agent deciding, use the :doc:`List chats App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/chat-getmany>`.

Other Chat tools
----------------

.. raw:: html

   <div class="tool-related"><a href="chat-get.html">Get a chat</a><a href="chat-messages.html">List chat messages</a><a href="chat-send.html">Send a chat message</a></div>
