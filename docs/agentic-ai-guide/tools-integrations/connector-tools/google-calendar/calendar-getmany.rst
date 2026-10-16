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
     <div><dt>Tool name</dt><dd><code>google_calendar_calendar_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every calendar the account can see, its own, shared ones and subscribed ones such as holidays, with each calendar's id, name, time zone and access role. Use it to find the calendar id the event operations take.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Calendar** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Calendar** row, then click **Add to agent**.

The agent now sees ``google_calendar_calendar_getmany`` and calls it when a request needs it.

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
   * - ``limit``
     - whole number
     - No
     - How many calendars at most. Example: 50. Default: 50.
   * - ``minAccessRole``
     - text
     - No
     - Only calendars where the account has at least this role; writer lists the ones it can add events to. One of: freeBusyReader, reader, writer, owner.
   * - ``fields``
     - list of text
     - No
     - Calendar fields to return, for example ["id", "summary", "timeZone", "accessRole"]; blank returns every field.

Need it on every run?
---------------------

To run **List calendars** every time a flow reaches it, without the agent deciding, use the :doc:`List calendars App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-calendar/calendar-getmany>`.

Other Calendar tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-get.html">Get a calendar</a></div>
