:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Issue</p>

Update an issue
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

   Changes an issue's title, body, state, labels, assignees or milestone and returns the updated issue; labels and assignees replace the current lists. Use it to close or reopen an issue; Issue addLabels adds labels without removing any.

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
   * - ``issueNumber``
     - whole number
     - Yes
     - The issue's number, as in #42.
   * - ``title``
     - text
     - No
     - The one-line title of the issue. Example: Checkout fails for EU cards.
   * - ``body``
     - text
     - No
     - The issue text in GitHub Markdown. Example: Steps to reproduce: pay with a card issued in Germany..
   * - ``state``
     - text
     - No
     - open or closed. One of: open, closed.
   * - ``stateReason``
     - text
     - No
     - Why the state changed, for example not\_planned when closing a duplicate. One of: completed, not\_planned, reopened.
   * - ``labels``
     - list of text
     - No
     - Label names; replaces the issue's current labels. Example: ["bug"].
   * - ``assignees``
     - list of text
     - No
     - GitHub logins; replaces the current assignees. Example: ["octocat"].
   * - ``milestone``
     - whole number
     - No
     - The number of the milestone to put the issue in. Example: 3.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **update** in the **Issue** row. The model sees it as ``github_issue_update``. Each call waits for human approval before it changes anything.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-create.html">Create an issue</a><a href="issue-comment.html">Comment on an issue</a><a href="issue-listcomments.html">List an issue&#x27;s comments</a><a href="issue-addlabels.html">Add labels to an issue</a></div>
