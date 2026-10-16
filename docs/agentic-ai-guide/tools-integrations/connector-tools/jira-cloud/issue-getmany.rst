:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Issue</p>

List issues
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_issue_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists issues that match an optional JQL filter (without one, the most recently created first), following Jira's paging up to the limit, with each issue's key, summary, status, assignee, priority and other navigable fields. It runs the same search as Issue search: use this one to browse recent issues, and Issue search when the request is a JQL condition.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **list** in the **Issue** row, then click **Add to agent**.

The agent now sees ``jira_cloud_issue_getmany`` and calls it when a request needs it.

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
     - A JQL filter such as project = FIN AND status = Open ORDER BY created DESC; blank returns the most recently created issues first.
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

To run **List issues** every time a flow reaches it, without the agent deciding, use the :doc:`List issues App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/issue-getmany>`.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-search.html">Search issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
