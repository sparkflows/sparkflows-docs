:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Pull Request</p>

Merge a pull request
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Pull Request</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>github_pull_request_merge</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Merges a pull request into its base branch and returns the merge commit SHA and a message. GitHub refuses when the pull request cannot be merged, for example with conflicts, failing required checks or missing approvals.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.
* The account behind the connection must be allowed to change this data in GitHub.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **merge** in the **Pull Request** row, then click **Add to agent**.

The agent now sees ``github_pull_request_merge`` and calls it when a request needs it.

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
   * - ``pullNumber``
     - whole number
     - Yes
     - The pull request's number, as in #57.
   * - ``mergeMethod``
     - text
     - No
     - merge keeps every commit behind a merge commit, squash combines them into one, rebase replays them onto the base. Default: merge. One of: merge, squash, rebase.
   * - ``commitTitle``
     - text
     - No
     - Title of the merge or squash commit; blank uses GitHub's default. Example: Fix SSO login timeout (#57).
   * - ``commitMessage``
     - text
     - No
     - Extra detail for the merge or squash commit. Example: Raises the SSO token timeout to 60 seconds..
   * - ``sha``
     - text
     - No
     - The head commit the pull request must still point to; the merge is refused if newer commits were pushed. Example: 6dcb09b5b57875f334f61aebed695e2e4193db5e.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in GitHub.

Other Pull Request tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="pull-request-get.html">Get a pull request</a><a href="pull-request-getmany.html">List pull requests</a><a href="pull-request-create.html">Open a pull request</a><a href="pull-request-update.html">Update a pull request</a><a href="pull-request-listfiles.html">List a pull request&#x27;s files</a><a href="pull-request-requestreview.html">Request a review</a></div>
