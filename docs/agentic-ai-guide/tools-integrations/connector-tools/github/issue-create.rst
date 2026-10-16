:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Issue</p>

Create an issue
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Opens a new issue in a repository and returns it with its number and URL. Use it to file a bug, request or task; to add to an existing issue use Issue comment.

Prerequisites
-------------

* **Connection:** GitHub connection. See :doc:`the GitHub prerequisites <../github>`.
* The connection's account must be allowed to change this data in GitHub.

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
   * - ``title``
     - text
     - Yes
     - The one-line title of the issue. Example: Checkout fails for EU cards.
   * - ``body``
     - text
     - No
     - The issue text in GitHub Markdown. Example: Steps to reproduce: pay with a card issued in Germany..
   * - ``labels``
     - list of text
     - No
     - Label names to apply; GitHub drops them silently unless the connection has push access. Example: ["bug"].
   * - ``assignees``
     - list of text
     - No
     - GitHub logins to assign. Example: ["octocat"].
   * - ``milestone``
     - whole number
     - No
     - The number of the milestone to put the issue in. Example: 3.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **create** in the **Issue** row. The model sees it as ``github_issue_create``. Each call waits for human approval before it changes anything.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-update.html">Update an issue</a><a href="issue-comment.html">Comment on an issue</a><a href="issue-listcomments.html">List an issue&#x27;s comments</a><a href="issue-addlabels.html">Add labels to an issue</a></div>
