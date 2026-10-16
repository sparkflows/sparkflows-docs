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
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists a repository's issues, newest first, with number, title, state, labels, assignees and dates; GitHub includes pull requests in this list, marked by a pull\_request field. Use Search issues for text search or for issues across repositories.

Prerequisites
-------------

* **Connection:** GitHub connection. See :doc:`the GitHub prerequisites <../github>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - Description
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

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **list** in the **Issue** row. The model sees it as ``github_issue_getmany``.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-comment.html">Comment on an issue</a><a href="issue-listcomments.html">List an issue&#x27;s comments</a><a href="issue-addlabels.html">Add labels to an issue</a></div>
