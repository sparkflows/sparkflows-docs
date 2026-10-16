:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Channel</p>

Get a channel
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_channel_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one channel of a team: displayName, description, membershipType, email, webUrl and createdDateTime. The ids come from Team getMany and Channel getMany.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Channel** row, then click **Add to agent**.

The agent now sees ``msteams_channel_get`` and calls it when a request needs it.

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
   * - ``fields``
     - list of text
     - No
     - Property names to return, for example ["id", "displayName"]; blank returns the default set. Example: displayName,membershipType,webUrl.

Need it on every run?
---------------------

To run **Get a channel** every time a flow reaches it, without the agent deciding, use the :doc:`Get a channel App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/channel-get>`.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-getmany.html">List channels</a><a href="channel-create.html">Create a channel</a><a href="channel-delete.html">Delete a channel</a><a href="channel-members.html">List channel members</a></div>
