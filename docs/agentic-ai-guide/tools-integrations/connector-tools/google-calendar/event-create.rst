:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Event</p>

Create an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an event on a calendar and returns it, with its id, link and, when conferenceType asks for one, its Meet link. Give start and end as date-times with a zone offset, or startDate and endDate for an all-day event; guests in attendees are emailed an invitation unless sendUpdates says otherwise.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Calendar prerequisites <../google-calendar>`.
* The connection's account must be allowed to change this data in Google Calendar.

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
   * - ``calendarId``
     - Calendar
     - text
     - No
     - The calendar's id: an address such as asha@company.com, a shared calendar's id from List calendars, or primary; blank means the primary calendar.
   * - ``summary``
     - Title
     - text
     - No
     - The event's title. Example: Quarterly review with Acme.
   * - ``start``
     - Starts
     - text
     - No
     - When the event starts, as ISO 8601 with a zone offset, for example 2026-10-01T10:00:00+05:30; for an all-day event use startDate instead.
   * - ``end``
     - Ends
     - text
     - No
     - When the event ends, in the same format as start; for an all-day event use endDate instead. Example: 2026-10-01T10:30:00+05:30.
   * - ``startDate``
     - All-day start date
     - text
     - No
     - For an all-day event, its first day as YYYY-MM-DD, given instead of start. Example: 2026-10-02.
   * - ``endDate``
     - All-day end date
     - text
     - No
     - For an all-day event, the day after its last day as YYYY-MM-DD (the end is exclusive), given instead of end. Example: 2026-10-03.
   * - ``attendees``
     - Guests
     - list of JSON object
     - No
     - The guests as [{"email": "asha@company.com"}], adding "optional": true for an optional guest. Example: [{"email": "asha@company.com"}, {"email": "vikram@acme.example.com"}].
   * - ``description``
     - Description
     - text
     - No
     - The event's notes or agenda. Example: Agenda: Q3 numbers, renewal terms, next steps..
   * - ``location``
     - Location
     - text
     - No
     - A room, place or address. Example: Conference room 4B, Pune office.
   * - ``conferenceType``
     - Video meeting
     - text
     - No
     - hangoutsMeet adds a Google Meet link to the event; blank adds none.
   * - ``sendUpdates``
     - Email guests
     - text
     - No
     - Which guests Google emails about it: all, externalOnly (only guests outside the organisation) or none; all is used when it is left out. Default: all. One of: all, externalOnly, none.
   * - ``conferenceDataVersion``
     - Conference support
     - whole number
     - No
     - Keep 1, which is what lets Google create the Meet link conferenceType asks for; 0 drops it. Default: 1. One of: 0, 1.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Calendar**, connect, and tick **create** in the **Event** row. The model sees it as ``google_calendar_event_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Calendar**, then **Create an event**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-quickadd.html">Quick add an event</a></div>
