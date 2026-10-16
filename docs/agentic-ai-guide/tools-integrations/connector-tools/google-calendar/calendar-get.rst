:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Calendar</p>

Get a calendar
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_calendar.svg" alt="Google Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Calendar</dd></div>
     <div><dt>Resource</dt><dd>Calendar</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one calendar's name, description and time zone. With calendarId blank it returns the account's primary calendar, which is how to learn the account's own time zone.

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
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Calendar fields to return, for example ["id", "summary", "timeZone"]; blank returns every field.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Calendar**, connect, and tick **get** in the **Calendar** row. The model sees it as ``google_calendar_calendar_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Calendar**, then **Get a calendar**, and fill in the inputs above. It runs every time the flow reaches it.

Other Calendar tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-getmany.html">List calendars</a></div>
