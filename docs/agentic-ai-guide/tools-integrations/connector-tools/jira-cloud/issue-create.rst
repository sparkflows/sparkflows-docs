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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an issue in a project and returns its id, key and URL. Values go in as plain text: the connector turns the project key, issue type, priority, assignee and parent into the objects Jira expects and the description into Jira's rich-text format. To change an existing issue use Issue update.

Prerequisites
-------------

* **Connection:** Jira connection. See :doc:`the Jira Cloud prerequisites <../jira-cloud>`.
* The connection's account must be allowed to change this data in Jira Cloud.

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
   * - ``projectKey``
     - Project key
     - text
     - Yes
     - The key of the project the issue goes in, for example FIN; Project getMany lists them.
   * - ``issueType``
     - Issue type
     - text
     - Yes
     - The issue type's name as the project defines it, for example Task, Bug, Story or Sub-task.
   * - ``summary``
     - Summary
     - text
     - Yes
     - The one-line title of the issue. Example: Login page times out for SSO users.
   * - ``description``
     - Description
     - text
     - No
     - The issue text as plain text; each line becomes a paragraph. Example: Users signing in with SSO wait 30 seconds and then see a timeout..
   * - ``priority``
     - Priority
     - text
     - No
     - The priority's name, for example Highest, High, Medium, Low or Lowest.
   * - ``labels``
     - Labels
     - list of text
     - No
     - Labels to set; a label cannot contain spaces. Example: ["billing", "urgent"].
   * - ``assigneeAccountId``
     - Assignee account id
     - text
     - No
     - The Atlassian account id of the person to assign, from User search; a name or email address does not work. Example: 5b10ac8d82e05b22cc7d4ef5.
   * - ``dueDate``
     - Due date
     - text
     - No
     - The due date as YYYY-MM-DD. Example: 2026-10-15.
   * - ``parentKey``
     - Parent issue key
     - text
     - No
     - The key of the parent issue, for a sub-task or a child of an epic. Example: FIN-7.
   * - ``components``
     - Components
     - list of text
     - No
     - Component names as the project defines them. Example: ["Payments"].

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **create** in the **Issue** row. The model sees it as ``jira_cloud_issue_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **Create an issue**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-search.html">Search issues</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
