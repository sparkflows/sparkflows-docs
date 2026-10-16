:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Issue</p>

Create an issue
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_issue_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an issue in a project and returns its id, key and URL. Values go in as plain text: the connector turns the project key, issue type, priority, assignee and parent into the objects Jira expects and the description into Jira's rich-text format. To change an existing issue use Issue update.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.
* The account behind the connection must be allowed to change this data in Jira Cloud.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **create** in the **Issue** row, then click **Add to agent**.

The agent now sees ``jira_cloud_issue_create`` and calls it when a request needs it.

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
   * - ``projectKey``
     - text
     - Yes
     - The key of the project the issue goes in, for example FIN; Project getMany lists them.
   * - ``issueType``
     - text
     - Yes
     - The issue type's name as the project defines it, for example Task, Bug, Story or Sub-task.
   * - ``summary``
     - text
     - Yes
     - The one-line title of the issue. Example: Login page times out for SSO users.
   * - ``description``
     - text
     - No
     - The issue text as plain text; each line becomes a paragraph. Example: Users signing in with SSO wait 30 seconds and then see a timeout..
   * - ``priority``
     - text
     - No
     - The priority's name, for example Highest, High, Medium, Low or Lowest.
   * - ``labels``
     - list of text
     - No
     - Labels to set; a label cannot contain spaces. Example: ["billing", "urgent"].
   * - ``assigneeAccountId``
     - text
     - No
     - The Atlassian account id of the person to assign, from User search; a name or email address does not work. Example: 5b10ac8d82e05b22cc7d4ef5.
   * - ``dueDate``
     - text
     - No
     - The due date as YYYY-MM-DD. Example: 2026-10-15.
   * - ``parentKey``
     - text
     - No
     - The key of the parent issue, for a sub-task or a child of an epic. Example: FIN-7.
   * - ``components``
     - list of text
     - No
     - Component names as the project defines them. Example: ["Payments"].

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Jira Cloud.

Need it on every run?
---------------------

To run **Create an issue** every time a flow reaches it, without the agent deciding, use the :doc:`Create an issue App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/issue-create>`.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-search.html">Search issues</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
