:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Pull Request</p>

List pull requests
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Pull Request</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>github_pull_request_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists a repository's pull requests, newest first, with number, title, state, author, draft flag, head and base branches. Filters narrow it by state and by base or head branch.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **list** in the **Pull Request** row, then click **Add to agent**.

The agent now sees ``github_pull_request_getmany`` and calls it when a request needs it.

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
   * - ``state``
     - text
     - No
     - Which pull requests to list; default open. One of: open, closed, all.
   * - ``base``
     - text
     - No
     - Only pull requests into this branch. Example: main.
   * - ``head``
     - text
     - No
     - Only pull requests from this branch, written owner:branch. Example: octocat:feature/login-timeout.
   * - ``sort``
     - text
     - No
     - Default created. One of: created, updated, popularity, long-running.
   * - ``direction``
     - text
     - No
     - Default desc. One of: asc, desc.
   * - ``limit``
     - whole number
     - No
     - How many pull requests at most. Default: 50.

Other Pull Request tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="pull-request-get.html">Get a pull request</a><a href="pull-request-create.html">Open a pull request</a><a href="pull-request-update.html">Update a pull request</a><a href="pull-request-merge.html">Merge a pull request</a><a href="pull-request-listfiles.html">List a pull request&#x27;s files</a><a href="pull-request-requestreview.html">Request a review</a></div>
