:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-calendar.html">Google Calendar</a> › Calendar</p>

List calendars
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

   Lists every calendar the account can see, its own, shared ones and subscribed ones such as holidays, with each calendar's id, name, time zone and access role. Use it to find the calendar id the event operations take.

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
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many calendars at most. Example: 50. Default: 50.
   * - ``minAccessRole``
     - At least this access
     - text
     - No
     - Only calendars where the account has at least this role; writer lists the ones it can add events to. One of: freeBusyReader, reader, writer, owner.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Calendar fields to return, for example ["id", "summary", "timeZone", "accessRole"]; blank returns every field.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Calendar**, connect, and tick **list** in the **Calendar** row. The model sees it as ``google_calendar_calendar_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Calendar**, then **List calendars**, and fill in the inputs above. It runs every time the flow reaches it.

Other Calendar tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-get.html">Get a calendar</a></div>
