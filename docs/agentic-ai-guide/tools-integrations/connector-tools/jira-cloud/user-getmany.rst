:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › User</p>

List users
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_user_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every user of the site, including app and bot accounts, with account id, display name, account type and active flag, following Jira's paging up to the limit. Use User search to find particular people.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **list** in the **User** row, then click **Add to agent**.

The agent now sees ``jira_cloud_user_getmany`` and calls it when a request needs it.

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
   * - ``limit``
     - whole number
     - No
     - How many users at most. Default: 50.

Need it on every run?
---------------------

To run **List users** every time a flow reaches it, without the agent deciding, use the :doc:`List users App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/user-getmany>`.

Other User tools
----------------

.. raw:: html

   <div class="tool-related"><a href="user-get.html">Get a user</a><a href="user-search.html">Find users</a></div>
