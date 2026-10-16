:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › User Group</p>

List user groups
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>User Group</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the workspace's user groups (the @handles that mention a team) with id, name, handle, description and, when asked, their user count and member IDs. User groups need a paid Slack plan.

Prerequisites
-------------

* **Connection:** Slack connection. See :doc:`the Slack prerequisites <../slack>`.

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
   * - ``includeUsers``
     - Include members
     - true or false
     - No
     - true adds each group's member user IDs (users).
   * - ``includeCount``
     - Include count
     - true or false
     - No
     - true adds user\_count.
   * - ``includeDisabled``
     - Include disabled
     - true or false
     - No
     - true lists disabled groups too.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **list** in the **User Group** row. The model sees it as ``slack_user_group_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **List user groups**, and fill in the inputs above. It runs every time the flow reaches it.

Other User Group tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="user-group-create.html">Create a user group</a><a href="user-group-update.html">Update a user group</a><a href="user-group-enable.html">Enable a user group</a><a href="user-group-disable.html">Disable a user group</a></div>
