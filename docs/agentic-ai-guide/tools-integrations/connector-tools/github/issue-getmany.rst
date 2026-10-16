:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Issue</p>

List issues
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>github_issue_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists a repository's issues, newest first, with number, title, state, labels, assignees and dates; GitHub includes pull requests in this list, marked by a pull\_request field. Use Search issues for text search or for issues across repositories.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **list** in the **Issue** row, then click **Add to agent**.

The agent now sees ``github_issue_getmany`` and calls it when a request needs it.

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
   * - ``repository``
     - text
     - Yes
     - The repository as owner/name, for example octocat/hello-world.
   * - ``state``
     - text
     - No
     - Which issues to list; default open. One of: open, closed, all.
   * - ``labels``
     - text
     - No
     - Comma-separated label names; only issues that have all of them. Example: bug,ui.
   * - ``assignee``
     - text
     - No
     - A login, none for unassigned issues or \* for assigned to anyone. Example: octocat.
   * - ``since``
     - text
     - No
     - Only issues updated at or after this time, ISO 8601. Example: 2026-09-01T00:00:00Z.
   * - ``sort``
     - text
     - No
     - Default created. One of: created, updated, comments.
   * - ``direction``
     - text
     - No
     - Default desc. One of: asc, desc.
   * - ``limit``
     - whole number
     - No
     - How many issues at most. Default: 50.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-comment.html">Comment on an issue</a><a href="issue-listcomments.html">List an issue&#x27;s comments</a><a href="issue-addlabels.html">Add labels to an issue</a></div>
