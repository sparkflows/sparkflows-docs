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
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_calendar_event_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes an event from a calendar and returns an empty result. Guests are emailed the cancellation unless sendUpdates is none.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-calendar>`.
* The account behind the connection must be allowed to change this data in Google Calendar.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Calendar** under **Connectors** and connect your Google connection.
#. Tick **delete** in the **Event** row, then click **Add to agent**.

The agent now sees ``google_calendar_event_delete`` and calls it when a request needs it.

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
   * - ``eventId``
     - text
     - Yes
     - The event's id, from List events or Create an event. Example: 5qk2m8r0ht7s3l1c9vfp2d4e6a.
   * - ``calendarId``
     - text
     - No
     - The calendar's id: an address such as asha@company.com, a shared calendar's id from List calendars, or primary; blank means the primary calendar.
   * - ``sendUpdates``
     - text
     - No
     - Which guests Google emails about it: all, externalOnly (only guests outside the organisation) or none; blank emails every guest. One of: all, externalOnly, none.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Calendar.

Need it on every run?
---------------------

To run **Delete an event** every time a flow reaches it, without the agent deciding, use the :doc:`Delete an event App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-calendar/event-delete>`.

Other Event tools
-----------------

.. raw:: html

   <div class="tool-related"><a href="event-get.html">Get an event</a><a href="event-getmany.html">List events</a><a href="event-create.html">Create an event</a><a href="event-update.html">Update an event</a><a href="event-quickadd.html">Quick add an event</a></div>
