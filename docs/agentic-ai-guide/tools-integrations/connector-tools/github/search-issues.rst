:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Search</p>

Search issues and pull requests
===============================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Search</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Searches issues and pull requests across GitHub with GitHub's search syntax and returns number, title, state, labels, author and repository URL for each. Use Issue getMany to list one repository's issues without a query.

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
   * - ``query``
     - text
     - Yes
     - Qualifiers and words; include is:issue or is:pr, for example is:issue is:open repo:acme/api label:bug or is:pr author:octocat created:>=2026-09-01. Example: is:issue is:open repo:octocat/hello-world label:bug.
   * - ``sort``
     - text
     - No
     - created, updated or comments; blank sorts by best match.
   * - ``order``
     - text
     - No
     - Default desc. One of: desc, asc.
   * - ``perPage``
     - whole number
     - No
     - How many rows GitHub returns in the single request this operation makes, at most 100; GitHub's own default is 30. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many results at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **issues** in the **Search** row. The model sees it as ``github_search_issues``.

Other Search tools
------------------

.. raw:: html

   <div class="tool-related"><a href="search-code.html">Search code</a><a href="search-repos.html">Search repositories</a></div>
