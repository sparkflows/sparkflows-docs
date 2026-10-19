:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Pull Request</p>

List a pull request's files
===========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Pull Request</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>github_pull_request_listfiles</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the files a pull request changes, with each file's status (added, modified, removed or renamed), added and deleted line counts and patch. GitHub returns them in one request here, so the page size caps the list at 100 files.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **listFiles** in the **Pull Request** row, then click **Add to agent**.

The agent now sees ``github_pull_request_listfiles`` and calls it when a request needs it.

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
   * - ``perPage``
     - whole number
     - No
     - How many rows GitHub returns in the single request this operation makes, at most 100; GitHub's own default is 30. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many files at most. Default: 50.

Other Pull Request tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="pull-request-get.html">Get a pull request</a><a href="pull-request-getmany.html">List pull requests</a><a href="pull-request-create.html">Open a pull request</a><a href="pull-request-update.html">Update a pull request</a><a href="pull-request-merge.html">Merge a pull request</a><a href="pull-request-requestreview.html">Request a review</a></div>
