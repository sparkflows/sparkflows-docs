:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Issue</p>

Assign an issue
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_issue_assign</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Assigns an issue to one person, or to the project's default assignee with -1. It takes an Atlassian account id, which User search returns for a name or email address. Use Issue update to change the assignee together with other fields.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.
* The account behind the connection must be allowed to change this data in Jira Cloud.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **assign** in the **Issue** row, then click **Add to agent**.

The agent now sees ``jira_cloud_issue_assign`` and calls it when a request needs it.

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
   * - ``issueKey``
     - text
     - Yes
     - The issue key, for example FIN-12.
   * - ``accountId``
     - text
     - Yes
     - The Atlassian account id of the new assignee, from User search; -1 assigns the project's default assignee. Example: 5b10ac8d82e05b22cc7d4ef5.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Jira Cloud.

Need it on every run?
---------------------

To run **Assign an issue** every time a flow reaches it, without the agent deciding, use the :doc:`Assign an issue App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/issue-assign>`.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-search.html">Search issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
