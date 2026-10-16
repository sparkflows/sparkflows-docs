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
     <div><dt>Tool name</dt><dd><code>outlook_calendar_event_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one event by its id with its times, location, organizer, attendees, online meeting link and status. Use it when the id is known from Event getMany.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Event** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_event_get`` and calls it when a request needs it.

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
     - The address whose calendar holds the event. Example: asha.rao@contoso.com.
   * - ``eventId``
     - text
     - Yes
     - The id of the event, from the id column of Event getMany. Example: AAMkAGI2TGuLAAA=.
   * - ``fields``
     - list of text
     - No
     - Graph event properties to return, such as subject, start, end and attendees; keep start in the list, or the row comes back in Graph's raw shape.
   * - ``timeZone``
     - text
     - No
     - The time zone to return start and end in, as a Windows or IANA name; blank returns them in UTC. Example: India Standard Time.

Need it on every run?
---------------------

To run **Get an event** every time a flow reaches it, without the agent deciding, use the :doc:`Get an event App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/event-get>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-delete.html">Delete an event</a><a href="event-accept.html">Accept a meeting invitation</a><a href="event-decline.html">Decline a meeting invitation</a><a href="event-cancel.html">Cancel a meeting</a></div>
