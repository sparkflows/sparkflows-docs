:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Channel</p>

Create a channel
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_channel_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a channel in a team and returns it with its new id. A standard channel is open to everyone in the team; private and shared channels created with an app-only connection also need an owner, which this operation does not set.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.
* The account behind the connection must be allowed to change this data in Microsoft Teams.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **create** in the **Channel** row, then click **Add to agent**.

The agent now sees ``msteams_channel_create`` and calls it when a request needs it.

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
   * - ``displayName``
     - text
     - Yes
     - The channel name, up to 50 characters. Example: Launch Planning.
   * - ``description``
     - text
     - No
     - What the channel is for.
   * - ``membershipType``
     - text
     - No
     - standard (the default), private or shared. One of: standard, private, shared.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Microsoft Teams.

Need it on every run?
---------------------

To run **Create a channel** every time a flow reaches it, without the agent deciding, use the :doc:`Create a channel App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/channel-create>`.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-getmany.html">List channels</a><a href="channel-get.html">Get a channel</a><a href="channel-delete.html">Delete a channel</a><a href="channel-members.html">List channel members</a></div>
