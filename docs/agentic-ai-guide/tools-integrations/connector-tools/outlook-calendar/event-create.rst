:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Create an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an event in the mailbox's default calendar, sends invitations to any attendees, and returns the event with its id. Use it to book a meeting or block time; to change an existing event use Event update.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Outlook Calendar prerequisites <../outlook-calendar>`.
* The connection's account must be allowed to change this data in Outlook Calendar.

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
     - The address whose calendar gets the event; it is the organizer. Example: asha.rao@contoso.com.
   * - ``start``
     - Starts
     - text
     - Yes
     - When it starts, as a local date and time without an offset, read in timeZone. Example: 2026-10-05T10:00:00.
   * - ``end``
     - Ends
     - text
     - Yes
     - When it ends, in the same form as start. Example: 2026-10-05T10:30:00.
   * - ``subject``
     - Title
     - text
     - No
     - The event's title. Example: Q3 close review.
   * - ``timeZone``
     - Time zone
     - text
     - No
     - The time zone start and end are in, as a Windows or IANA name such as India Standard Time or UTC; blank means UTC.
   * - ``attendees``
     - Attendees
     - list of text
     - No
     - Addresses to invite as required attendees; Outlook sends each an invitation. Example: ["ravi.menon@contoso.com", "finance@contoso.com"].
   * - ``location``
     - Location
     - text
     - No
     - Where it takes place, as free text. Example: Board room, 4th floor.
   * - ``body``
     - Description
     - text
     - No
     - The event's description, as plain text.
   * - ``allDay``
     - All day
     - true or false
     - No
     - true makes it an all-day event, in which case start and end must be midnights and end the day after the last day.
   * - ``isOnlineMeeting``
     - Online meeting
     - true or false
     - No
     - true adds a Teams meeting link to the event.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Calendar**, connect, and tick **create** in the **Event** row. The model sees it as ``outlook_calendar_event_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Calendar**, then **Create an event**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-get.html">Get an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
