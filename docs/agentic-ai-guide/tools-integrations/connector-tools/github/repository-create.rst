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
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a repository owned by the authenticated user and returns it with its full name and clone URLs. It cannot create a repository inside an organisation.

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

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **create** in the **Repository** row. The model sees it as ``github_repository_create``. Each call waits for human approval before it changes anything.

Other Repository tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="repository-get.html">Get a repository</a><a href="repository-getmany.html">List repositories</a><a href="repository-listbranches.html">List branches</a><a href="repository-listcommits.html">List commits</a></div>
