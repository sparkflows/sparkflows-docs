:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › User Group</p>

List user groups
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>User Group</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_user_group_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the workspace's user groups (the @handles that mention a team) with id, name, handle, description and, when asked, their user count and member IDs. User groups need a paid Slack plan.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **list** in the **User Group** row, then click **Add to agent**.

The agent now sees ``slack_user_group_getmany`` and calls it when a request needs it.

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
   * - ``includeUsers``
     - true or false
     - No
     - true adds each group's member user IDs (users).
   * - ``includeCount``
     - true or false
     - No
     - true adds user\_count.
   * - ``includeDisabled``
     - true or false
     - No
     - true lists disabled groups too.

Need it on every run?
---------------------

To run **List user groups** every time a flow reaches it, without the agent deciding, use the :doc:`List user groups App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/user-group-getmany>`.

Other User Group tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="user-group-create.html">Create a user group</a><a href="user-group-update.html">Update a user group</a><a href="user-group-enable.html">Enable a user group</a><a href="user-group-disable.html">Disable a user group</a></div>
