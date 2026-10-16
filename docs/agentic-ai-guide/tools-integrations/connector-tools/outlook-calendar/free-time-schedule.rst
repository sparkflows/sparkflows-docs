:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Free Time</p>

Get free/busy schedules
=======================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Free Time</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-calendar.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the free/busy schedule of people or rooms over a period, one row per address: an availability view with one digit per slot (0 free, 1 tentative, 2 busy, 3 out of office, 4 working elsewhere) and the busy items. Use it to check availability before booking with Event create.

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
     - The mailbox that asks; it must be allowed to see the others' free/busy. Example: asha.rao@contoso.com.
   * - ``schedules``
     - People or rooms
     - list of text
     - Yes
     - The addresses of the people, rooms or distribution lists whose availability to read. Example: ["ravi.menon@contoso.com", "boardroom@contoso.com"].
   * - ``startDateTime``
     - From
     - text
     - Yes
     - Start of the period, as a local date and time without an offset, read in startTimeZone. Example: 2026-10-05T09:00:00.
   * - ``endDateTime``
     - To
     - text
     - Yes
     - End of the period, as a local date and time without an offset, read in endTimeZone. Example: 2026-10-05T18:00:00.
   * - ``startTimeZone``
     - From time zone
     - text
     - No
     - The time zone of startDateTime, as a Windows or IANA name. Example: India Standard Time. Default: UTC.
   * - ``endTimeZone``
     - To time zone
     - text
     - No
     - The time zone of endDateTime, as a Windows or IANA name. Example: India Standard Time. Default: UTC.
   * - ``intervalMinutes``
     - Slot length (minutes)
     - whole number
     - No
     - The length in minutes of each slot of the availability view, from 5 to 1440. Default: 30.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Calendar**, connect, and tick **schedule** in the **Free Time** row. The model sees it as ``outlook_calendar_free_time_schedule``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Calendar**, then **Get free/busy schedules**, and fill in the inputs above. It runs every time the flow reaches it.

Other Free Time tools
---------------------

.. raw:: html

   <div class="tool-related"><a href="free-time-find.html">Find meeting times</a></div>
