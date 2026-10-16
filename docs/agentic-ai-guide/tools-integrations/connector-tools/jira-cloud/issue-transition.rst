:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Issue</p>

Change an issue's status
========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_issue_transition</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Moves an issue to another status, such as In Progress or Done, by performing one of its workflow's transitions. Transition ids differ per workflow and per current status, so fetch them with Issue listTransitions first. Use Issue update for fields other than the status.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.
* The account behind the connection must be allowed to change this data in Jira Cloud.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **transition** in the **Issue** row, then click **Add to agent**.

The agent now sees ``jira_cloud_issue_transition`` and calls it when a request needs it.

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
   * - ``transitionId``
     - text
     - Yes
     - The id of the transition to perform, from Issue listTransitions, for example 31; it is not the status name.
   * - ``resolution``
     - text
     - No
     - The resolution to set when the transition's screen asks for one, by name; Issue listTransitions with transitions.fields shows which fields a transition needs. Example: Done.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Jira Cloud.

Need it on every run?
---------------------

To run **Change an issue's status** every time a flow reaches it, without the agent deciding, use the :doc:`Change an issue's status App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/issue-transition>`.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-search.html">Search issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
