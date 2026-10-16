:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Team</p>

List teams
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Team</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/microsoft-teams.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the organisation's teams (Microsoft 365 groups that have a team) with id, displayName, description, mail and visibility. The id is the team id every channel operation takes.

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
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Property names to return, for example ["id", "displayName"]; blank returns the default set. Example: id,displayName.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many teams at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **list** in the **Team** row. The model sees it as ``msteams_team_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **List teams**, and fill in the inputs above. It runs every time the flow reaches it.

Other Team tools
----------------

.. raw:: html

   <div class="tool-related"><a href="team-get.html">Get a team</a><a href="team-members.html">List team members</a></div>
