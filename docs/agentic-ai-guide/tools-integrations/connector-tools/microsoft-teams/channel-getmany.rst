:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Channel</p>

List channels
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Channel</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/microsoft-teams.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the channels of a team with id, displayName, description, membershipType (standard, private or shared) and webUrl. The channel id (19:...@thread.tacv2) is what the other channel and message operations take.

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
   * - ``teamId``
     - Team
     - text
     - Yes
     - The team id (a GUID), from Team getMany. Example: b1f0c3d2-1234-4c5d-9e8f-0a1b2c3d4e5f.
   * - ``filter``
     - Filter
     - text
     - No
     - An OData filter on channel properties, for example membershipType eq 'private'.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Property names to return, for example ["id", "displayName"]; blank returns the default set. Example: id,displayName.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many channels at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **list** in the **Channel** row. The model sees it as ``msteams_channel_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **List channels**, and fill in the inputs above. It runs every time the flow reaches it.

Other Channel tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="channel-get.html">Get a channel</a><a href="channel-create.html">Create a channel</a><a href="channel-delete.html">Delete a channel</a><a href="channel-members.html">List channel members</a></div>
