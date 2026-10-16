:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › User</p>

Get a user
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_user_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one user by Atlassian account id and returns the display name, email address (when the user's privacy settings show it), active flag and time zone. Use User search to find someone by name or email address.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **get** in the **User** row, then click **Add to agent**.

The agent now sees ``jira_cloud_user_get`` and calls it when a request needs it.

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
   * - ``accountId``
     - text
     - Yes
     - The user's Atlassian account id, from User search or from an issue's assignee or reporter. Example: 5b10ac8d82e05b22cc7d4ef5.

Need it on every run?
---------------------

To run **Get a user** every time a flow reaches it, without the agent deciding, use the :doc:`Get a user App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/user-get>`.

Other User tools
----------------

.. raw:: html

   <div class="tool-related"><a href="user-getmany.html">List users</a><a href="user-search.html">Find users</a></div>
