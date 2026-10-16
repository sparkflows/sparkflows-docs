:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Repository</p>

List repositories
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Repository</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the repositories the authenticated user owns, collaborates on or reaches through an organisation, with full name, visibility, default branch, description and last push time. Use Search repos for repositories beyond the user's own.

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
   * - ``visibility``
     - text
     - No
     - Which repositories by visibility; default all. One of: all, public, private.
   * - ``affiliation``
     - text
     - No
     - Comma-separated owner, collaborator and organization\_member; default all three.
   * - ``sort``
     - text
     - No
     - Default full\_name. One of: created, updated, pushed, full\_name.
   * - ``direction``
     - text
     - No
     - Default asc when sorting by full\_name, desc otherwise. One of: asc, desc.
   * - ``limit``
     - whole number
     - No
     - How many repositories at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **list** in the **Repository** row. The model sees it as ``github_repository_getmany``.

Other Repository tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="repository-get.html">Get a repository</a><a href="repository-create.html">Create a repository</a><a href="repository-listbranches.html">List branches</a><a href="repository-listcommits.html">List commits</a></div>
