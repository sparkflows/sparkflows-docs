:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › User Group</p>

Enable a user group
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>User Group</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>slack_user_group_enable</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Re-enables a disabled user group so its @handle works again, and returns the group. User Group getMany with includeDisabled lists disabled groups.

Before you start
----------------

* A Slack connection. See :doc:`how to set one up <../slack>`.
* The account behind the connection must be allowed to change this data in Slack.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Slack** under **Connectors** and connect your Slack connection.
#. Tick **enable** in the **User Group** row, then click **Add to agent**.

The agent now sees ``slack_user_group_enable`` and calls it when a request needs it.

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
   * - ``usergroupId``
     - text
     - Yes
     - The user group ID, for example S0123ABC; User Group getMany lists them.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Slack.

Need it on every run?
---------------------

To run **Enable a user group** every time a flow reaches it, without the agent deciding, use the :doc:`Enable a user group App Action </agentic-ai-guide/tools-integrations/app-action-apps/slack/user-group-enable>`.

Other User Group tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="user-group-getmany.html">List user groups</a><a href="user-group-create.html">Create a user group</a><a href="user-group-update.html">Update a user group</a><a href="user-group-disable.html">Disable a user group</a></div>
