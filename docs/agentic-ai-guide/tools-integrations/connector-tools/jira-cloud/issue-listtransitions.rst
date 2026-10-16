:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Issue</p>

List an issue's transitions
===========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_issue_listtransitions</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the transitions the issue can take from its current status, each with its id, name and the status it leads to. Use it before Issue transition to find the id that reaches the wanted status.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **listTransitions** in the **Issue** row, then click **Add to agent**.

The agent now sees ``jira_cloud_issue_listtransitions`` and calls it when a request needs it.

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
   * - ``expand``
     - text
     - No
     - transitions.fields also returns the fields each transition's screen asks for, such as resolution.

Need it on every run?
---------------------

To run **List an issue's transitions** every time a flow reaches it, without the agent deciding, use the :doc:`List an issue's transitions App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/issue-listtransitions>`.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-search.html">Search issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
