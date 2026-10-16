:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Pull Request</p>

Request a review
================

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

   Asks people or teams to review a pull request and returns the pull request with its requested reviewers. Give reviewers, teamReviewers or both.

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
   * - ``reviewers``
     - list of text
     - No
     - GitHub logins to ask for a review. Example: ["octocat"].
   * - ``teamReviewers``
     - list of text
     - No
     - Slugs of teams in the repository's organisation. Example: ["platform"].

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **requestReview** in the **Pull Request** row. The model sees it as ``github_pull_request_requestreview``. Each call waits for human approval before it changes anything.

Other Pull Request tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="pull-request-get.html">Get a pull request</a><a href="pull-request-getmany.html">List pull requests</a><a href="pull-request-create.html">Open a pull request</a><a href="pull-request-update.html">Update a pull request</a><a href="pull-request-merge.html">Merge a pull request</a><a href="pull-request-listfiles.html">List a pull request&#x27;s files</a></div>
