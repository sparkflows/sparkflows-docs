:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

List events
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists events in the mailbox's default calendar with subject, start and end, location, organizer, attendees, online meeting link and status. Give startDateTime and endDateTime to list what happens in a period, with each occurrence of a repeating meeting as its own row; without them a repeating meeting appears once, as its series. To read one event by id use Event get.

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
     - Mailbox
     - text
     - Yes
     - The address whose calendar this is. Example: asha.rao@contoso.com.
   * - ``startDateTime``
     - From
     - text
     - No
     - Start of a date window; with endDateTime it switches the list to the calendar view. Example: 2026-10-01T00:00:00Z.
   * - ``endDateTime``
     - To
     - text
     - No
     - End of the date window; it only takes effect together with startDateTime. Example: 2026-10-08T00:00:00Z.
   * - ``filter``
     - Filter
     - text
     - No
     - An OData filter on event properties, such as subject eq 'Weekly sync' or createdDateTime ge 2026-09-01T00:00:00Z.
   * - ``orderBy``
     - Order by
     - text
     - No
     - A property and a direction, such as start/dateTime desc; with a date window the default is start/dateTime.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph event properties to return, such as subject, start, end, location and attendees; keep start in the list, or rows come back in Graph's raw shape. Example: ["subject", "start", "end", "location"].
   * - ``timeZone``
     - Show times in
     - text
     - No
     - The time zone to return start and end in, as a Windows or IANA name; blank returns them in UTC. Example: India Standard Time.
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many events at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Calendar**, connect, and tick **list** in the **Event** row. The model sees it as ``outlook_calendar_event_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Calendar**, then **List events**, and fill in the inputs above. It runs every time the flow reaches it.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
