:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Search</p>

Search code
===========

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

   Searches file contents across GitHub and returns the matching files with name, path, repository and URL, not the matching lines. Only default branches and files under 384 KB are searched, and GitHub allows about 10 code searches a minute.

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
     - Words plus qualifiers such as repo:, org:, language: or path:, for example timeout repo:acme/api language:python. Example: timeout repo:octocat/hello-world.
   * - ``perPage``
     - whole number
     - No
     - How many rows GitHub returns in the single request this operation makes, at most 100; GitHub's own default is 30. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many files at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **code** in the **Search** row. The model sees it as ``github_search_code``.

Other Search tools
------------------

.. raw:: html

   <div class="tool-related"><a href="search-issues.html">Search issues and pull requests</a><a href="search-repos.html">Search repositories</a></div>
