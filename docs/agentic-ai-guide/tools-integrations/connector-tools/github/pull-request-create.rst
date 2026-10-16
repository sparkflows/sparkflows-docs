:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Pull Request</p>

Open a pull request
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Pull Request</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>github_pull_request_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Opens a pull request from one branch into another and returns it with its number and URL. Both branches must exist and differ, and GitHub refuses a second open pull request for the same pair.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.
* The account behind the connection must be allowed to change this data in GitHub.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **create** in the **Pull Request** row, then click **Add to agent**.

The agent now sees ``github_pull_request_create`` and calls it when a request needs it.

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
   * - ``title``
     - text
     - Yes
     - The one-line title of the pull request. Example: Fix SSO login timeout.
   * - ``head``
     - text
     - Yes
     - The branch with the changes; owner:branch when it lives in a fork. Example: feature/login-timeout.
   * - ``base``
     - text
     - Yes
     - The branch to merge into. Example: main.
   * - ``body``
     - text
     - No
     - The pull request text in GitHub Markdown. Example: Raises the SSO token timeout to 60 seconds..
   * - ``draft``
     - true or false
     - No
     - true opens it as a draft. Example: false.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in GitHub.

Other Pull Request tools
------------------------

.. raw:: html

   <div class="tool-related"><a href="pull-request-get.html">Get a pull request</a><a href="pull-request-getmany.html">List pull requests</a><a href="pull-request-update.html">Update a pull request</a><a href="pull-request-merge.html">Merge a pull request</a><a href="pull-request-listfiles.html">List a pull request&#x27;s files</a><a href="pull-request-requestreview.html">Request a review</a></div>
