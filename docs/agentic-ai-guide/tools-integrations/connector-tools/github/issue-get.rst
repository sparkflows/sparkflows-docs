:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Issue</p>

Get an issue
============

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

   Fetches one issue by its number and returns title, body, state, labels, assignees, milestone, author and comment count. A pull request number works too but returns only its issue side; Pull Request get has its branches and merge state.

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
   * - ``issueNumber``
     - whole number
     - Yes
     - The issue's number, as in #42.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **get** in the **Issue** row. The model sees it as ``github_issue_get``.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-getmany.html">List issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-comment.html">Comment on an issue</a><a href="issue-listcomments.html">List an issue&#x27;s comments</a><a href="issue-addlabels.html">Add labels to an issue</a></div>
