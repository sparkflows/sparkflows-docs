:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Issue</p>

Update an issue
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_issue_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes fields on an existing issue; only the fields given change, and labels, components and fix versions replace the current lists. Jira answers with no content, so the result is the status of the write. To change the status use Issue transition, and to change only the assignee Issue assign.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.
* The account behind the connection must be allowed to change this data in Jira Cloud.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **update** in the **Issue** row, then click **Add to agent**.

The agent now sees ``jira_cloud_issue_update`` and calls it when a request needs it.

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
   * - ``summary``
     - text
     - No
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
     - Labels to set; replaces the issue's current labels. Example: ["billing", "urgent"].
   * - ``assigneeAccountId``
     - text
     - No
     - The Atlassian account id of the person to assign, from User search; a name or email address does not work. Example: 5b10ac8d82e05b22cc7d4ef5.
   * - ``dueDate``
     - text
     - No
     - The due date as YYYY-MM-DD. Example: 2026-10-15.
   * - ``components``
     - list of text
     - No
     - Component names as the project defines them; replaces the current components. Example: ["Payments"].
   * - ``fixVersions``
     - list of text
     - No
     - Version names as the project defines them; replaces the current fix versions. Example: ["2026.10"].

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Jira Cloud.

Need it on every run?
---------------------

To run **Update an issue** every time a flow reaches it, without the agent deciding, use the :doc:`Update an issue App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/issue-update>`.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-search.html">Search issues</a><a href="issue-create.html">Create an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
