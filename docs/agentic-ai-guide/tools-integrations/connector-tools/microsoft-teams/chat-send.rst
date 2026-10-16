:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Chat</p>

Send a chat message
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Chat</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_chat_send</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Sends a message in an existing chat and returns it with its id; the text is sent as HTML. Graph sends only for a signed-in user, so the connection needs a user (delegated) access token; with app-only credentials the call is refused before anything is sent.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.
* The account behind the connection must be allowed to change this data in Microsoft Teams.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **send** in the **Chat** row, then click **Add to agent**.

The agent now sees ``msteams_chat_send`` and calls it when a request needs it.

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
   * - ``text``
     - text
     - Yes
     - The message, as plain text or HTML, with <br> for a line break. Example: Can we move the review to 3pm?.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Microsoft Teams.

Need it on every run?
---------------------

To run **Send a chat message** every time a flow reaches it, without the agent deciding, use the :doc:`Send a chat message App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/chat-send>`.

Other Chat tools
----------------

.. raw:: html

   <div class="tool-related"><a href="chat-getmany.html">List chats</a><a href="chat-get.html">Get a chat</a><a href="chat-messages.html">List chat messages</a></div>
