:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Issue</p>

Get an issue
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_issue_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one issue by its key and returns its fields: summary, status, assignee, reporter, priority, labels, description, dates and custom fields. Use it when the key is known; to find issues by a condition use Issue search.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **get** in the **Issue** row, then click **Add to agent**.

The agent now sees ``jira_cloud_issue_get`` and calls it when a request needs it.

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
   * - ``fields``
     - list of text
     - No
     - Jira field ids to return, such as summary, status, assignee or customfield\_10020; blank returns every field. Example: ["summary", "status", "assignee", "priority"].
   * - ``expand``
     - text
     - No
     - Extra sections, comma-separated: renderedFields (rich-text fields as HTML instead of Atlassian Document Format), changelog, transitions or names.

Need it on every run?
---------------------

To run **Get an issue** every time a flow reaches it, without the agent deciding, use the :doc:`Get an issue App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/issue-get>`.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-getmany.html">List issues</a><a href="issue-search.html">Search issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
