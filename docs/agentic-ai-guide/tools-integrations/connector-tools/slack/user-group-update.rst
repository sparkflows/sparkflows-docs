:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › User Group</p>

Update a user group
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>User Group</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Changes a user group's name, handle, description or default channels and returns the group. Its members are not changed here.

Prerequisites
-------------

* **Connection:** Slack connection. See :doc:`the Slack prerequisites <../slack>`.
* The connection's account must be allowed to change this data in Slack.

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
   * - ``usergroupId``
     - User group
     - text
     - Yes
     - The user group ID, for example S0123ABC; User Group getMany lists them.
   * - ``name``
     - Name
     - text
     - No
     - The new display name.
   * - ``handle``
     - Handle
     - text
     - No
     - The new mention name without @.
   * - ``description``
     - Description
     - text
     - No
     - The new description.
   * - ``channels``
     - Default channels
     - text
     - No
     - Comma-separated channel IDs, replacing the current default channels. Example: C0123ABC,C0456DEF.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **update** in the **User Group** row. The model sees it as ``slack_user_group_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **Update a user group**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other User Group tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="user-group-getmany.html">List user groups</a><a href="user-group-create.html">Create a user group</a><a href="user-group-enable.html">Enable a user group</a><a href="user-group-disable.html">Disable a user group</a></div>
