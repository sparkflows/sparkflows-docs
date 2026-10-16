:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Workflow</p>

List workflow runs
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Workflow</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists recent GitHub Actions runs across all of a repository's workflows, with id, workflow name, branch, event, status, conclusion, actor and times. Filters narrow it by branch, status or conclusion, event, actor or creation time.

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
   * - ``repository``
     - text
     - Yes
     - The repository as owner/name, for example octocat/hello-world.
   * - ``branch``
     - text
     - No
     - Only runs on this branch. Example: main.
   * - ``status``
     - text
     - No
     - queued, in\_progress or completed, or a conclusion such as success, failure or cancelled.
   * - ``event``
     - text
     - No
     - What started the run, for example push, pull\_request, schedule or workflow\_dispatch.
   * - ``actor``
     - text
     - No
     - Only runs started by this GitHub login. Example: octocat.
   * - ``created``
     - text
     - No
     - A time range in GitHub search syntax, for example >=2026-09-30T00:00:00Z or 2026-09-01..2026-09-30.
   * - ``perPage``
     - whole number
     - No
     - How many rows GitHub returns in the single request this operation makes, at most 100; GitHub's own default is 30. Default: 100.
   * - ``limit``
     - whole number
     - No
     - How many runs at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **listRuns** in the **Workflow** row. The model sees it as ``github_workflow_listruns``.

Other Workflow tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="workflow-getmany.html">List workflows</a><a href="workflow-dispatch.html">Run a workflow</a></div>
