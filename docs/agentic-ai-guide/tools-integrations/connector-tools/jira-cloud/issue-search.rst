:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Issue</p>

Search issues
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds issues with a JQL query and returns each match's key, summary, status, assignee, priority and other navigable fields, following Jira's paging up to the limit. Use it for any condition on project, status, assignee, dates or text; Issue get is the direct call when the key is known.

Prerequisites
-------------

* **Connection:** Jira connection. See :doc:`the Jira Cloud prerequisites <../jira-cloud>`.

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
   * - ``jql``
     - JQL query
     - text
     - No
     - The JQL query, for example project = FIN AND assignee = currentUser() AND created >= -7d; text ~ "login timeout" matches words in the summary, description and comments. Example: project = FIN AND status != Done AND priority = High ORDER BY updated DESC.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Jira field ids to return for each issue; blank returns the navigable fields. Example: ["summary", "status", "assignee", "priority"].
   * - ``expand``
     - Expand
     - text
     - No
     - Extra sections for each issue, comma-separated: renderedFields, changelog, transitions or names.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many issues at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **search** in the **Issue** row. The model sees it as ``jira_cloud_issue_search``.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **Search issues**, and fill in the inputs above. It runs every time the flow reaches it.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
