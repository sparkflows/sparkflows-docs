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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Assigns an issue to one person, or to the project's default assignee with -1. It takes an Atlassian account id, which User search returns for a name or email address. Use Issue update to change the assignee together with other fields.

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
   * - ``issueKey``
     - Issue key
     - text
     - Yes
     - The issue key, for example FIN-12.
   * - ``accountId``
     - Assignee account id
     - text
     - Yes
     - The Atlassian account id of the new assignee, from User search; -1 assigns the project's default assignee. Example: 5b10ac8d82e05b22cc7d4ef5.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **assign** in the **Issue** row. The model sees it as ``jira_cloud_issue_assign``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **Assign an issue**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-search.html">Search issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
