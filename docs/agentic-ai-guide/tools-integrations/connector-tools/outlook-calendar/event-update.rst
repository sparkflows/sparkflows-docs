:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Update an event
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

   Changes an existing event's title, times, location, description or attendees and returns the updated event. Only the fields given change; attendees, when given, replace the whole list.

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
     - The address whose calendar holds the event. Example: asha.rao@contoso.com.
   * - ``eventId``
     - Event id
     - text
     - Yes
     - The id of the event to change, from the id column of Event getMany. Example: AAMkAGI2TGuLAAA=.
   * - ``subject``
     - Title
     - text
     - No
     - The new title.
   * - ``start``
     - Starts
     - text
     - No
     - The new start, as a local date and time without an offset, read in timeZone. Example: 2026-10-05T11:00:00.
   * - ``end``
     - Ends
     - text
     - No
     - The new end, in the same form as start. Example: 2026-10-05T11:30:00.
   * - ``timeZone``
     - Time zone
     - text
     - No
     - The time zone of start and end; give it whenever start or end changes, since blank means UTC. Example: India Standard Time.
   * - ``location``
     - Location
     - text
     - No
     - The new location, as free text.
   * - ``body``
     - Description
     - text
     - No
     - The new description, as plain text.
   * - ``attendees``
     - Attendees
     - list of text
     - No
     - The full list of attendee addresses; it replaces the current attendees.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Calendar**, connect, and tick **update** in the **Event** row. The model sees it as ``outlook_calendar_event_update``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Calendar**, then **Update an event**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
