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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>github_issue_update</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes an issue's title, body, state, labels, assignees or milestone and returns the updated issue; labels and assignees replace the current lists. Use it to close or reopen an issue; Issue addLabels adds labels without removing any.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.
* The account behind the connection must be allowed to change this data in GitHub.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **update** in the **Issue** row, then click **Add to agent**.

The agent now sees ``github_issue_update`` and calls it when a request needs it.

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

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in GitHub.

Other Issue tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-getmany.html">List issues</a><a href="issue-create.html">Create an issue</a><a href="issue-comment.html">Comment on an issue</a><a href="issue-listcomments.html">List an issue&#x27;s comments</a><a href="issue-addlabels.html">Add labels to an issue</a></div>
