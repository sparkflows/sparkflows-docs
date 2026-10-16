:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Event</p>

Delete an event
===============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Event</dd></div>
     <div><dt>Type</dt><dd>Delete · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes an event from a calendar and returns an empty result. Guests are emailed the cancellation unless sendUpdates is none.

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
   * - ``eventId``
     - Event id
     - text
     - Yes
     - The event's id, from List events or Create an event. Example: 5qk2m8r0ht7s3l1c9vfp2d4e6a.
   * - ``calendarId``
     - Calendar
     - text
     - No
     - The calendar's id: an address such as asha@company.com, a shared calendar's id from List calendars, or primary; blank means the primary calendar.
   * - ``sendUpdates``
     - Email guests
     - text
     - No
     - Which guests Google emails about it: all, externalOnly (only guests outside the organisation) or none; blank emails every guest. One of: all, externalOnly, none.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Calendar**, connect, and tick **delete** in the **Event** row. The model sees it as ``google_calendar_event_delete``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Calendar**, then **Delete an event**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-quickadd.html">Quick add an event</a></div>
