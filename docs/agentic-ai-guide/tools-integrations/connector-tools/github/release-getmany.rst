:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Release</p>

List releases
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Release</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>github_release_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists a repository's releases, newest first, with tag, name, draft and prerelease flags, publish time and notes. GitHub returns them in one request here, so the page size caps the list at 100.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **list** in the **Release** row, then click **Add to agent**.

The agent now sees ``github_release_getmany`` and calls it when a request needs it.

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
   * - ``perPage``
     - whole number
     - No
     - How many rows GitHub returns in the single request this operation makes, at most 100; GitHub's own default is 30. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many releases at most. Default: 50.

Other Release tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="release-create.html">Create a release</a></div>
