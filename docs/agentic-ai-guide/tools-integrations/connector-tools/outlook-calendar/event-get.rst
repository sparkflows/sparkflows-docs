:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Event</p>

Get an event
============

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

   Returns one event by its id with its times, location, organizer, attendees, online meeting link and status. Use it when the id is known from Event getMany.

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
     - The address whose calendar holds the event. Example: asha.rao@contoso.com.
   * - ``eventId``
     - Event id
     - text
     - Yes
     - The id of the event, from the id column of Event getMany. Example: AAMkAGI2TGuLAAA=.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph event properties to return, such as subject, start, end and attendees; keep start in the list, or the row comes back in Graph's raw shape.
   * - ``timeZone``
     - Show times in
     - text
     - No
     - The time zone to return start and end in, as a Windows or IANA name; blank returns them in UTC. Example: India Standard Time.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Calendar**, connect, and tick **get** in the **Event** row. The model sees it as ``outlook_calendar_event_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Calendar**, then **Get an event**, and fill in the inputs above. It runs every time the flow reaches it.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
