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
     <div><dt>Tool name</dt><dd><code>github_repository_listcommits</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists commits on a branch, newest first, with SHA, message, author, committer and date. Filters narrow it to a file or folder, an author or a time range; use it to see what changed recently.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **listCommits** in the **Repository** row, then click **Add to agent**.

The agent now sees ``github_repository_listcommits`` and calls it when a request needs it.

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

Other Repository tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="repository-get.html">Get a repository</a><a href="repository-getmany.html">List repositories</a><a href="repository-create.html">Create a repository</a><a href="repository-listbranches.html">List branches</a></div>
