:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Free Time</p>

Find meeting times
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Free Time</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Suggests meeting times when the organizer and the attendees are free, one row per suggestion with its time, a confidence score and who is available; when nothing fits, one row gives Graph's emptySuggestionsReason. Microsoft Graph serves this only to a connection signed in as a user, not to an app-only connection.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Outlook Calendar prerequisites <../outlook-calendar>`.

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
   * - ``mailbox``
     - Organizer
     - text
     - Yes
     - The organizer's address; the organizer's own calendar is checked too. Example: asha.rao@contoso.com.
   * - ``attendees``
     - Attendees
     - list of JSON object
     - No
     - The people to meet, as Graph attendee objects with an emailAddress and a type of required or optional. Example: [{"emailAddress": {"address": "ravi.menon@contoso.com"}, "type": "required"}].
   * - ``meetingDuration``
     - Duration
     - text
     - No
     - How long the meeting lasts, as an ISO 8601 duration such as PT30M or PT1H; blank means 30 minutes.
   * - ``timeSlots``
     - Search within
     - list of JSON object
     - No
     - The periods to search, each a start and an end with a dateTime and a timeZone; blank lets Outlook search the coming working days. Example: [{"start": {"dateTime": "2026-10-05T09:00:00", "timeZone": "UTC"}, "end": {"dateTime": "2026-10-05T17:00:00", "timeZone": "UTC"}}].
   * - ``activityDomain``
     - Hours
     - text
     - No
     - Which hours count: work (working hours, the default), personal or unrestricted. One of: work, personal, unrestricted.
   * - ``maxCandidates``
     - Suggestions
     - whole number
     - No
     - How many suggestions at most. Example: 5.
   * - ``isOrganizerOptional``
     - Organizer optional
     - true or false
     - No
     - true lets suggestions ignore the organizer's own availability.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Calendar**, connect, and tick **find** in the **Free Time** row. The model sees it as ``outlook_calendar_free_time_find``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Calendar**, then **Find meeting times**, and fill in the inputs above. It runs every time the flow reaches it.

Other Free Time tools
---------------------

.. raw:: html

   <div class="tool-related"><a href="free-time-schedule.html">Get free/busy schedules</a></div>
