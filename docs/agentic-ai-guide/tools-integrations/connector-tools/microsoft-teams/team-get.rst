:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Team</p>

Get a team
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Team</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>msteams_team_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one team's settings: displayName, description, visibility, isArchived, webUrl and its member, guest, messaging and fun settings. The team id comes from Team getMany.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Team** row, then click **Add to agent**.

The agent now sees ``msteams_team_get`` and calls it when a request needs it.

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
   * - ``fields``
     - list of text
     - No
     - Property names to return, for example ["id", "displayName"]; blank returns the default set. Example: displayName,visibility,isArchived.

Need it on every run?
---------------------

To run **Get a team** every time a flow reaches it, without the agent deciding, use the :doc:`Get a team App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/team-get>`.

Other Team tools
----------------

.. raw:: html

   <div class="tool-related"><a href="team-getmany.html">List teams</a><a href="team-members.html">List team members</a></div>
