:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Calendar</p>

List calendars
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Calendar</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_calendar_calendar_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the calendars of a mailbox with their ids, names, colours, owners and which one is the default. The event operations always work on the default calendar.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **list** in the **Calendar** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_calendar_getmany`` and calls it when a request needs it.

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
     - The address whose calendars to list. Example: asha.rao@contoso.com.
   * - ``fields``
     - list of text
     - No
     - Graph calendar properties to return, such as id, name, isDefaultCalendar and canEdit; blank returns them all. Example: ["id", "name", "isDefaultCalendar"].
   * - ``limit``
     - whole number
     - No
     - How many calendars at most. Default: 50.

Need it on every run?
---------------------

To run **List calendars** every time a flow reaches it, without the agent deciding, use the :doc:`List calendars App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/calendar-getmany>`.

Other Calendar tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-get.html">Get a calendar</a></div>
