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
     <div><dt>Tool name</dt><dd><code>outlook_calendar_free_time_schedule</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the free/busy schedule of people or rooms over a period, one row per address: an availability view with one digit per slot (0 free, 1 tentative, 2 busy, 3 out of office, 4 working elsewhere) and the busy items. Use it to check availability before booking with Event create.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **schedule** in the **Free Time** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_free_time_schedule`` and calls it when a request needs it.

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
     - The mailbox that asks; it must be allowed to see the others' free/busy. Example: asha.rao@contoso.com.
   * - ``schedules``
     - list of text
     - Yes
     - The addresses of the people, rooms or distribution lists whose availability to read. Example: ["ravi.menon@contoso.com", "boardroom@contoso.com"].
   * - ``startDateTime``
     - text
     - Yes
     - Start of the period, as a local date and time without an offset, read in startTimeZone. Example: 2026-10-05T09:00:00.
   * - ``endDateTime``
     - text
     - Yes
     - End of the period, as a local date and time without an offset, read in endTimeZone. Example: 2026-10-05T18:00:00.
   * - ``startTimeZone``
     - text
     - No
     - The time zone of startDateTime, as a Windows or IANA name. Example: India Standard Time. Default: UTC.
   * - ``endTimeZone``
     - text
     - No
     - The time zone of endDateTime, as a Windows or IANA name. Example: India Standard Time. Default: UTC.
   * - ``intervalMinutes``
     - whole number
     - No
     - The length in minutes of each slot of the availability view, from 5 to 1440. Default: 30.

Need it on every run?
---------------------

To run **Get free/busy schedules** every time a flow reaches it, without the agent deciding, use the :doc:`Get free/busy schedules App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/free-time-schedule>`.

Other Free Time tools
---------------------

.. raw:: html

   <div class="tool-related"><a href="free-time-find.html">Find meeting times</a></div>
