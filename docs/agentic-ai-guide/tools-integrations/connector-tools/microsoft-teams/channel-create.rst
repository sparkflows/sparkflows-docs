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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/microsoft-teams.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a channel in a team and returns it with its new id. A standard channel is open to everyone in the team; private and shared channels created with an app-only connection also need an owner, which this operation does not set.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Microsoft Teams prerequisites <../microsoft-teams>`.
* The connection's account must be allowed to change this data in Microsoft Teams.

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
   * - ``teamId``
     - Team
     - text
     - Yes
     - The team id (a GUID), from Team getMany. Example: b1f0c3d2-1234-4c5d-9e8f-0a1b2c3d4e5f.
   * - ``displayName``
     - Name
     - text
     - Yes
     - The channel name, up to 50 characters. Example: Launch Planning.
   * - ``description``
     - Description
     - text
     - No
     - What the channel is for.
   * - ``membershipType``
     - Membership
     - text
     - No
     - standard (the default), private or shared. One of: standard, private, shared.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **create** in the **Channel** row. The model sees it as ``msteams_channel_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **Create a channel**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-getmany.html">List channels</a><a href="channel-get.html">Get a channel</a><a href="channel-delete.html">Delete a channel</a><a href="channel-members.html">List channel members</a></div>
