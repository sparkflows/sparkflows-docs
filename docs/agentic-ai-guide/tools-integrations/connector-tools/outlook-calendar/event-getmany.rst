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
     <div><dt>Tool name</dt><dd><code>outlook_calendar_event_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists events in the mailbox's default calendar with subject, start and end, location, organizer, attendees, online meeting link and status. Give startDateTime and endDateTime to list what happens in a period, with each occurrence of a repeating meeting as its own row; without them a repeating meeting appears once, as its series. To read one event by id use Event get.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **list** in the **Event** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_event_getmany`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``mailbox``
     - text
     - Yes
     - The address whose calendar this is. Example: asha.rao@contoso.com.
   * - ``startDateTime``
     - text
     - No
     - Start of a date window; with endDateTime it switches the list to the calendar view. Example: 2026-10-01T00:00:00Z.
   * - ``endDateTime``
     - text
     - No
     - End of the date window; it only takes effect together with startDateTime. Example: 2026-10-08T00:00:00Z.
   * - ``filter``
     - text
     - No
     - An OData filter on event properties, such as subject eq 'Weekly sync' or createdDateTime ge 2026-09-01T00:00:00Z.
   * - ``orderBy``
     - text
     - No
     - A property and a direction, such as start/dateTime desc; with a date window the default is start/dateTime.
   * - ``fields``
     - list of text
     - No
     - Graph event properties to return, such as subject, start, end, location and attendees; keep start in the list, or rows come back in Graph's raw shape. Example: ["subject", "start", "end", "location"].
   * - ``timeZone``
     - text
     - No
     - The time zone to return start and end in, as a Windows or IANA name; blank returns them in UTC. Example: India Standard Time.
   * - ``limit``
     - whole number
     - No
     - How many events at most. Default: 50.

Need it on every run?
---------------------

To run **List events** every time a flow reaches it, without the agent deciding, use the :doc:`List events App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/event-getmany>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
