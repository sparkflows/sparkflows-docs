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
     <div><dt>Tool name</dt><dd><code>google_calendar_calendar_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one calendar's name, description and time zone. With calendarId blank it returns the account's primary calendar, which is how to learn the account's own time zone.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Calendar** under **Connectors** and connect your Google connection.
#. Tick **get** in the **Calendar** row, then click **Add to agent**.

The agent now sees ``google_calendar_calendar_get`` and calls it when a request needs it.

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
   * - ``calendarId``
     - text
     - No
     - The calendar's id: an address such as asha@company.com, a shared calendar's id from List calendars, or primary; blank means the primary calendar.
   * - ``fields``
     - list of text
     - No
     - Calendar fields to return, for example ["id", "summary", "timeZone"]; blank returns every field.

Need it on every run?
---------------------

To run **Get a calendar** every time a flow reaches it, without the agent deciding, use the :doc:`Get a calendar App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-calendar/calendar-get>`.

Other Calendar tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-getmany.html">List calendars</a></div>
