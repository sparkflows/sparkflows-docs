:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../microsoft-teams.html">Microsoft Teams</a> › Meeting</p>

Get an online meeting
=====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/msteams.svg" alt="Microsoft Teams logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Microsoft Teams</dd></div>
     <div><dt>Resource</dt><dd>Meeting</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/microsoft-teams.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one online meeting: subject, startDateTime, endDateTime, joinWebUrl, participants and dial-in details. The meeting id is the one Meeting create returned.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Microsoft Teams prerequisites <../microsoft-teams>`.

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
   * - ``meetingId``
     - Meeting
     - text
     - Yes
     - The online meeting id returned by Meeting create. Example: MSo1N2Y5ZGFjYy03MWJmLTQ3NDMtYjQxMy01M2EdFGkdRWHJlQ.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Microsoft Teams**, connect, and tick **get** in the **Meeting** row. The model sees it as ``msteams_meeting_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Microsoft Teams**, then **Get an online meeting**, and fill in the inputs above. It runs every time the flow reaches it.

Other Meeting tools
-------------------

.. raw:: html

   <div class="tool-related"><a href="meeting-create.html">Create an online meeting</a></div>
