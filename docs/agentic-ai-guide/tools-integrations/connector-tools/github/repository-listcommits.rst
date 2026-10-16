:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Repository</p>

List commits
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Repository</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists commits on a branch, newest first, with SHA, message, author, committer and date. Filters narrow it to a file or folder, an author or a time range; use it to see what changed recently.

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
   * - ``branch``
     - text
     - No
     - The branch, tag or commit SHA to list from; blank is the default branch. Example: main.
   * - ``path``
     - text
     - No
     - Only commits that touch this file or folder. Example: src/billing.
   * - ``author``
     - text
     - No
     - Only commits by this GitHub login or email address. Example: octocat.
   * - ``since``
     - text
     - No
     - Only commits after this time, ISO 8601. Example: 2026-09-01T00:00:00Z.
   * - ``until``
     - text
     - No
     - Only commits before this time, ISO 8601. Example: 2026-09-30T23:59:59Z.
   * - ``limit``
     - whole number
     - No
     - How many commits at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **listCommits** in the **Repository** row. The model sees it as ``github_repository_listcommits``.

Other Repository tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="repository-get.html">Get a repository</a><a href="repository-getmany.html">List repositories</a><a href="repository-create.html">Create a repository</a><a href="repository-listbranches.html">List branches</a></div>
