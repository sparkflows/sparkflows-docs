:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Free Time</p>

Find busy times
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Free Time</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the busy intervals of one or more calendars between timeMin and timeMax, so the free slots are the gaps between them. Use it to find a meeting time; it returns no event details.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Calendar prerequisites <../google-calendar>`.

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
   * - ``timeMin``
     - From
     - text
     - Yes
     - Start of the window, as ISO 8601 with a zone offset, for example 2026-10-01T09:00:00+05:30; resolve words such as Monday to dates first.
   * - ``timeMax``
     - Until
     - text
     - Yes
     - End of the window, in the same format as timeMin. Example: 2026-10-01T18:00:00+05:30.
   * - ``calendarId``
     - Calendar
     - text
     - No
     - The one calendar to check when calendars is blank, such as asha@company.com; blank means the primary calendar.
   * - ``calendars``
     - Calendars to check
     - list of JSON object
     - No
     - Several calendars or people to check at once, as [{"id": "asha@company.com"}, {"id": "primary"}]; it replaces calendarId. Example: [{"id": "asha@company.com"}, {"id": "vikram@company.com"}].
   * - ``timeZone``
     - Time zone
     - text
     - No
     - The IANA time zone for the busy times returned, for example Asia/Kolkata; blank returns UTC.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Calendar**, connect, and tick **find** in the **Free Time** row. The model sees it as ``google_calendar_free_time_find``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Calendar**, then **Find busy times**, and fill in the inputs above. It runs every time the flow reaches it.
