:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../slack.html">Slack</a> › User</p>

Get a user
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/slack.svg" alt="Slack logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Slack</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/slack.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one member's account: id, name, real\_name, profile (display name, email, title, phone), tz, is\_admin, is\_bot and deleted. The user ID comes from a message's user field, User getMany or User lookupByEmail.

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
   * - ``user``
     - User
     - text
     - Yes
     - The user ID, for example U0123ABC.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Slack**, connect, and tick **get** in the **User** row. The model sees it as ``slack_user_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Slack**, then **Get a user**, and fill in the inputs above. It runs every time the flow reaches it.

Other User tools
----------------

.. raw:: html

   <div class="tool-related"><a href="user-getmany.html">List users</a><a href="user-getprofile.html">Get a user&#x27;s profile</a><a href="user-getstatus.html">Get a user&#x27;s presence</a><a href="user-lookupbyemail.html">Find a user by email</a></div>
