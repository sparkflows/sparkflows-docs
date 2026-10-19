:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Repository</p>

Create a repository
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Repository</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>github_repository_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a repository owned by the authenticated user and returns it with its full name and clone URLs. It cannot create a repository inside an organisation.

Before you start
----------------

* A GitHub connection. See :doc:`how to set one up <../github>`.
* The account behind the connection must be allowed to change this data in GitHub.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **GitHub** under **Connectors** and connect your GitHub connection.
#. Tick **create** in the **Repository** row, then click **Add to agent**.

The agent now sees ``github_repository_create`` and calls it when a request needs it.

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
   * - ``name``
     - text
     - Yes
     - The repository name, without the owner. Example: billing-service.
   * - ``description``
     - text
     - No
     - A one-line description of the repository. Example: Invoices and payment runs.
   * - ``private``
     - true or false
     - No
     - true makes the repository private; default false.
   * - ``autoInit``
     - true or false
     - No
     - true creates a first commit with an empty README, so branches and files can be added at once.
   * - ``gitignoreTemplate``
     - text
     - No
     - A .gitignore template name, for example Python or Node.
   * - ``licenseTemplate``
     - text
     - No
     - A license keyword, for example mit or apache-2.0.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in GitHub.

Other Repository tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="repository-get.html">Get a repository</a><a href="repository-getmany.html">List repositories</a><a href="repository-listbranches.html">List branches</a><a href="repository-listcommits.html">List commits</a></div>
