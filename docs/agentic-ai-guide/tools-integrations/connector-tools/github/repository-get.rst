:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Repository</p>

Get a repository
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Repository</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>github_repository_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one repository and returns its description, default branch, visibility, topics, open issue count, stars, forks and URLs. Use Repository getMany to list the repositories the connection can reach.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **get** in the **Repository** row, then click **Add to agent**.

The agent now sees ``github_repository_get`` and calls it when a request needs it.

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

Other Repository tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="repository-getmany.html">List repositories</a><a href="repository-create.html">Create a repository</a><a href="repository-listbranches.html">List branches</a><a href="repository-listcommits.html">List commits</a></div>
