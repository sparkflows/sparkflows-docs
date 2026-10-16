:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-calendar.html">Outlook Calendar</a> › Calendar</p>

Get a calendar
==============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_calendar.svg" alt="Outlook Calendar logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Calendar</dd></div>
     <div><dt>Resource</dt><dd>Calendar</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_calendar_calendar_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one calendar by its id with its name, colour, owner and edit and sharing rights. Use Calendar getMany to find the id.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-calendar>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Calendar** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Calendar** row, then click **Add to agent**.

The agent now sees ``outlook_calendar_calendar_get`` and calls it when a request needs it.

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
     - The address the calendar belongs to. Example: asha.rao@contoso.com.
   * - ``calendarId``
     - text
     - Yes
     - The id of the calendar, from the id column of Calendar getMany. Example: AAMkAGI2TGuLAAAuAAAAAAAiQ8W967B7TKBjgx9rVEURAQAiIsqMbYjsT5e-T7KzowPTAAAAAAEGAAA=.
   * - ``fields``
     - list of text
     - No
     - Graph calendar properties to return, such as name, owner and canEdit; blank returns them all.

Need it on every run?
---------------------

To run **Get a calendar** every time a flow reaches it, without the agent deciding, use the :doc:`Get a calendar App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-calendar/calendar-get>`.

Other Calendar tools
--------------------

.. raw:: html

   <div class="tool-related"><a href="calendar-getmany.html">List calendars</a></div>
