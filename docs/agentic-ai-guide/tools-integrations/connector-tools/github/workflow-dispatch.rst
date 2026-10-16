:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../github.html">GitHub</a> › Workflow</p>

Run a workflow
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/github.svg" alt="GitHub logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>GitHub</dd></div>
     <div><dt>Resource</dt><dd>Workflow</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Starts a workflow that has a workflow\_dispatch trigger, on a branch or tag, with optional inputs. GitHub answers with no content, so the new run shows up in Workflow listRuns a few seconds later.

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
   * - ``repository``
     - text
     - Yes
     - The repository as owner/name, for example octocat/hello-world.
   * - ``workflow``
     - text
     - Yes
     - The workflow's file name, for example deploy.yml, or its numeric id from Workflow getMany.
   * - ``ref``
     - text
     - Yes
     - The branch or tag to run the workflow on. Example: main.
   * - ``inputs``
     - JSON object
     - No
     - Values for the workflow's inputs, as a JSON object of input name to value. Example: {"environment": "staging"}.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **GitHub**, connect, and tick **dispatch** in the **Workflow** row. The model sees it as ``github_workflow_dispatch``. Each call waits for human approval before it changes anything.

Other Workflow tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="workflow-getmany.html">List workflows</a><a href="workflow-listruns.html">List workflow runs</a></div>
