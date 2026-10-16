:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Pull Request</p>

Update a pull request
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Pull Request</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes a pull request's title, body, base branch or state and returns the updated pull request. Setting state to closed closes it without merging; Pull Request merge merges it.

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
   * - ``pullNumber``
     - whole number
     - Yes
     - The pull request's number, as in #57.
   * - ``title``
     - text
     - No
     - The one-line title of the pull request. Example: Fix SSO login timeout.
   * - ``body``
     - text
     - No
     - The pull request text in GitHub Markdown. Example: Raises the SSO token timeout to 60 seconds..
   * - ``state``
     - text
     - No
     - open or closed. One of: open, closed.
   * - ``base``
     - text
     - No
     - A new branch to merge into. Example: main.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **update** in the **Pull Request** row. The model sees it as ``github_pull_request_update``. Each call waits for human approval before it changes anything.

Other Pull Request tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="pull-request-get.html">Get a pull request</a><a href="pull-request-getmany.html">List pull requests</a><a href="pull-request-create.html">Open a pull request</a><a href="pull-request-merge.html">Merge a pull request</a><a href="pull-request-listfiles.html">List a pull request&#x27;s files</a><a href="pull-request-requestreview.html">Request a review</a></div>
