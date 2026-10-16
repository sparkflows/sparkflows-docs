:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Event</p>

List events
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the events on a calendar, with repeating events expanded into single occurrences and sorted by start time by default. Bound the window with timeMin and timeMax, or it runs from the calendar's earliest event; searchText matches words in the title, description, location and guests.

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
   * - ``calendarId``
     - Calendar
     - text
     - No
     - The calendar's id: an address such as asha@company.com, a shared calendar's id from List calendars, or primary; blank means the primary calendar.
   * - ``timeMin``
     - From
     - text
     - No
     - Only events that end after this moment, as ISO 8601 with a zone offset, for example 2026-10-01T00:00:00+05:30.
   * - ``timeMax``
     - Until
     - text
     - No
     - Only events that start before this moment, in the same format as timeMin. Example: 2026-10-08T00:00:00+05:30.
   * - ``searchText``
     - Search text
     - text
     - No
     - Words to find in the title, description, location, organiser or guests of the events. Example: budget review.
   * - ``singleEvents``
     - Expand repeating events
     - true or false
     - No
     - true lists every occurrence of a repeating event on its own; false returns each series once. Default: True.
   * - ``orderBy``
     - Sort by
     - text
     - No
     - startTime sorts by start and needs singleEvents true; updated sorts by the last change. Default: startTime. One of: startTime, updated.
   * - ``updatedMin``
     - Changed since
     - text
     - No
     - Only events changed after this moment, deleted ones included, as ISO 8601 with a zone offset. Example: 2026-09-29T00:00:00Z.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many events at most. Example: 50. Default: 50.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Event fields to return, for example ["id", "summary", "start", "end", "attendees"]; blank returns every field.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Calendar**, connect, and tick **list** in the **Event** row. The model sees it as ``google_calendar_event_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Calendar**, then **List events**, and fill in the inputs above. It runs every time the flow reaches it.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-quickadd.html">Quick add an event</a></div>
