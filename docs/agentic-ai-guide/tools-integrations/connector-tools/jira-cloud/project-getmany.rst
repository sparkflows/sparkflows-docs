:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Project</p>

List projects
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Project</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_project_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the projects the connection can see, with key, name, type and id, following Jira's paging up to the limit. Use it to find a project key by name before creating or searching issues.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **list** in the **Project** row, then click **Add to agent**.

The agent now sees ``jira_cloud_project_getmany`` and calls it when a request needs it.

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
   * - ``search``
     - text
     - No
     - Only projects whose name or key contains this text, ignoring case. Example: finance.
   * - ``typeKey``
     - text
     - No
     - Only projects of this type. One of: software, service\_desk, business.
   * - ``limit``
     - whole number
     - No
     - How many projects at most. Default: 50.

Need it on every run?
---------------------

To run **List projects** every time a flow reaches it, without the agent deciding, use the :doc:`List projects App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/project-getmany>`.

Other Project tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="project-get.html">Get a project</a></div>
