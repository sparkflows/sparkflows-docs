:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Meeting</p>

Create an online meeting
========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Meeting</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/microsoft-teams.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a Teams online meeting on behalf of a user and returns its joinWebUrl, id, start and end. The meeting is not put in anyone's calendar, and an app-only connection also needs an application access policy for that user, granted by a Teams admin.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Microsoft Teams prerequisites <../microsoft-teams>`.
* The connection's account must be allowed to change this data in Microsoft Teams.

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
   * - ``organizer``
     - Organizer
     - text
     - Yes
     - The organizer's Microsoft Entra user object id (a GUID), which Team members and Channel members return as userId; the meeting belongs to this user. Example: 6e0f2c1a-9b8d-4f3e-a2c1-7d6e5f4a3b2c.
   * - ``subject``
     - Subject
     - text
     - Yes
     - The meeting title. Example: Quarterly review.
   * - ``startDateTime``
     - Starts
     - text
     - No
     - When the meeting starts, with a time zone, for example 2026-10-01T10:00:00Z.
   * - ``endDateTime``
     - Ends
     - text
     - No
     - When the meeting ends, with a time zone, for example 2026-10-01T10:30:00Z.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **create** in the **Meeting** row. The model sees it as ``msteams_meeting_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **Create an online meeting**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Meeting tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="meeting-get.html">Get an online meeting</a></div>
