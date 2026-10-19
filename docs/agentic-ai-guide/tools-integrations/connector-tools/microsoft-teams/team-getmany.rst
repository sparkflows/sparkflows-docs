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
     <div><dt>Tool name</dt><dd><code>msteams_team_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the organisation's teams (Microsoft 365 groups that have a team) with id, displayName, description, mail and visibility. The id is the team id every channel operation takes.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../microsoft-teams>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Microsoft Teams** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **list** in the **Team** row, then click **Add to agent**.

The agent now sees ``msteams_team_getmany`` and calls it when a request needs it.

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
   * - ``fields``
     - list of text
     - No
     - Property names to return, for example ["id", "displayName"]; blank returns the default set. Example: id,displayName.
   * - ``limit``
     - whole number
     - No
     - How many teams at most. Default: 50.

Need it on every run?
---------------------

To run **List teams** every time a flow reaches it, without the agent deciding, use the :doc:`List teams App Action </agentic-ai-guide/tools-integrations/app-action-apps/microsoft-teams/team-getmany>`.

Other Team tools
----------------

.. raw:: html

   <div class="tool-related"><a href="team-get.html">Get a team</a><a href="team-members.html">List team members</a></div>
