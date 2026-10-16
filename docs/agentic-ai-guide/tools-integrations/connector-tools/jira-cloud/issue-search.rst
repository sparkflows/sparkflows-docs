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
     <div><dt>Tool name</dt><dd><code>jira_cloud_issue_search</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Finds issues with a JQL query and returns each match's key, summary, status, assignee, priority and other navigable fields, following Jira's paging up to the limit. Use it for any condition on project, status, assignee, dates or text; Issue get is the direct call when the key is known.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **search** in the **Issue** row, then click **Add to agent**.

The agent now sees ``jira_cloud_issue_search`` and calls it when a request needs it.

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
   * - ``jql``
     - text
     - No
     - The JQL query, for example project = FIN AND assignee = currentUser() AND created >= -7d; text ~ "login timeout" matches words in the summary, description and comments. Example: project = FIN AND status != Done AND priority = High ORDER BY updated DESC.
   * - ``fields``
     - list of text
     - No
     - Jira field ids to return for each issue; blank returns the navigable fields. Example: ["summary", "status", "assignee", "priority"].
   * - ``expand``
     - text
     - No
     - Extra sections for each issue, comma-separated: renderedFields, changelog, transitions or names.
   * - ``limit``
     - whole number
     - No
     - How many issues at most. Default: 50.

Need it on every run?
---------------------

To run **Search issues** every time a flow reaches it, without the agent deciding, use the :doc:`Search issues App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/issue-search>`.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
