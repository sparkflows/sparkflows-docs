:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Pull Request</p>

Get a pull request
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Pull Request</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one pull request by number and returns title, body, state, author, head and base branches, draft and merged flags, mergeability and counts of commits, changed files and lines. Use Pull Request listFiles for the files it changes.

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
   * - ``pullNumber``
     - whole number
     - Yes
     - The pull request's number, as in #57.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **get** in the **Pull Request** row. The model sees it as ``github_pull_request_get``.

Other Pull Request tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="pull-request-getmany.html">List pull requests</a><a href="pull-request-create.html">Open a pull request</a><a href="pull-request-update.html">Update a pull request</a><a href="pull-request-merge.html">Merge a pull request</a><a href="pull-request-listfiles.html">List a pull request&#x27;s files</a><a href="pull-request-requestreview.html">Request a review</a></div>
