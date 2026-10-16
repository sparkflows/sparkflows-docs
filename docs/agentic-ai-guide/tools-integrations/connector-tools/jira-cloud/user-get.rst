:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › User</p>

Get a user
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/jira-cloud.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one user by Atlassian account id and returns the display name, email address (when the user's privacy settings show it), active flag and time zone. Use User search to find someone by name or email address.

Prerequisites
-------------

* **Connection:** Jira connection. See :doc:`the Jira Cloud prerequisites <../jira-cloud>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``accountId``
     - Account id
     - text
     - Yes
     - The user's Atlassian account id, from User search or from an issue's assignee or reporter. Example: 5b10ac8d82e05b22cc7d4ef5.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Jira Cloud**, connect, and tick **get** in the **User** row. The model sees it as ``jira_cloud_user_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Jira**, then **Get a user**, and fill in the inputs above. It runs every time the flow reaches it.

Other User tools
----------------

.. raw:: html

   <div class="tool-related"><a href="user-getmany.html">List users</a><a href="user-search.html">Find users</a></div>
