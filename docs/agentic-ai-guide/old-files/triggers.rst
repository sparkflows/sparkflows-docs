Triggers: How an Agent Starts
=============================

Every agent built on the canvas starts at a **Trigger** node. The Trigger says
*when* a run begins, and it sets the message and the values every later step can
read.

.. contents:: On this page
   :local:
   :depth: 1

Five ways to start
------------------

Drop a **Trigger** onto the canvas (it is the first tile under **Commonly used**)
or double-click the one already there. The drawer opens at one question: *How
does this agent start?*

.. figure:: ../_assets/agentic-ai-guide/triggers/kinds.png
   :alt: The Trigger drawer listing Manually, On a schedule, When something happens in an app, When a file arrives in a folder and When another system calls
   :width: 580px

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Pick
     - When it fits
   * - **Manually**
     - A person starts the run from the Execute page or a chat. The default.
   * - **On a schedule**
     - A report every Monday morning, a clean-up every night.
   * - **When something happens in an app**
     - A new Jira issue, a Salesforce lead, an email, a new database row.
   * - **When a file arrives in a folder**
     - A supplier drops ``orders_1001.csv`` into ``data/incoming/``.
   * - **When another system calls**
     - Your own application starts the agent over REST.

You can change your mind later: open the Trigger, press **Back**, and pick
another kind. The rest of the agent does not change.

Manually
--------

The person starting the run types what they want. The message on the node is
used only when they leave the box empty, so it doubles as a ready-made test.

.. figure:: ../_assets/agentic-ai-guide/triggers/manual.png
   :alt: Manual trigger details with a message and one named value, file_name = tickets.csv
   :width: 580px

   Name a value once and every later step can use it.

**Values the steps can use** are named inputs for the run. Here ``file_name`` is
``tickets.csv``, and a later Read/Write Files step reads it as
``${inputs.file_name}``. Whoever runs the agent can change the value on the
Execute page, so one agent serves many files.

On a schedule
-------------

Pick how often - every hour, day, week or month - then the day, the hour, the
minute and the time zone. The summary at the top reads the choice back in words
("Every Monday at 9:00").

.. figure:: ../_assets/agentic-ai-guide/triggers/schedule.png
   :alt: Schedule trigger set to every week, Monday, 9:00, Asia/Kolkata
   :width: 580px

**What the agent should do** is the message every scheduled run starts with,
because nobody is there to type one.

When you **Save** the agent, Sparkflows creates a schedule for it, named after
the agent with ``(Trigger node)`` at the end. It appears under **Agents >
Schedules** with every other schedule, where you can pause it with the toggle.
Switch the Trigger back to **Manually** and that schedule is removed.

.. figure:: ../_assets/agentic-ai-guide/triggers/schedules-list.png
   :alt: The Schedules tab listing agents whose name ends in (Trigger node), with their frequency and an on/off toggle
   :width: 100%

   Every scheduled or event Trigger has a schedule here. The toggle pauses it.

When something happens in an app
--------------------------------

Pick the app, then the event. Only apps that can report what changed are listed.

.. figure:: ../_assets/agentic-ai-guide/triggers/app-grid.png
   :alt: The app grid for event triggers - Salesforce, Microsoft Teams, Slack, OneDrive, Outlook Calendar, Outlook Mail, SharePoint, Gmail, Google Calendar and more, each with its number of events
   :width: 580px

Each app offers its own events. A database, for example, can start a run when a
row is added (by a date/time column or an increasing id) or when a row changes.

.. figure:: ../_assets/agentic-ai-guide/triggers/app-events.png
   :alt: PostgreSQL events - row added by a date/time column, row changed by an updated-at column, row added by an increasing id column
   :width: 580px

The details step asks for the **Connection**, what to watch (a table, a mailbox,
a project), **Check every (minutes)**, and **First check looks back (minutes)** -
how far back the very first check reaches.

Then press **Fetch a sample**. It reads a few recent records so you, and every
step after the Trigger, can see the fields a new record has. **Save trigger**
stays disabled until the sample has been fetched.

.. figure:: ../_assets/agentic-ai-guide/triggers/app-details.png
   :alt: PostgreSQL row-added trigger with a fetched sample showing the fields id, customer_id, product, amount, status and created_at
   :width: 100%

   The sample on the left is what a new record looks like. Click ``${}`` next to a field to put it in the message.

How it works, in one paragraph: every few minutes the agent asks the app what is
new since its last check. A check that finds something starts a run with the new
records; a check that finds nothing ends quietly. Nothing has to reach your
Sparkflows server from outside, so event triggers work on-premise and behind a
firewall.

When a file arrives in a folder
-------------------------------

The same idea for files on the machine the engine runs on. Pick **A file is
added** or **A file is added or changed**, then give a folder (``data/incoming/``)
or a pattern (``data/incoming/*.csv``, ``data/**/*.pdf``). Cloud paths such as
``s3://`` work too - see :doc:`/agentic-ai-guide/files`.

.. figure:: ../_assets/agentic-ai-guide/triggers/file-details.png
   :alt: File trigger watching data/agent-files-training/incoming/*.csv with a sample showing path, name, extension, size, modified, folder and kind
   :width: 100%

Each new file arrives with its ``path``, ``name``, ``extension``, ``size`` and
``modified`` time. A following Read/Write Files step reads it with
``${event.path}``.

When another system calls
-------------------------

Another application starts the run with one HTTP request, using an access token
from **Administration > Access Tokens** in the ``token`` header. The inputs in the
body are what the run starts with.

.. figure:: ../_assets/agentic-ai-guide/triggers/webhook.png
   :alt: Webhook trigger showing the POST request to /api/v1/agents/339/execute with a JSON body of inputs
   :width: 580px

The full request, how to wait for the result, and how to answer an approval
from your own code are on :doc:`/agentic-ai-guide/developer-api`.

What a Trigger hands to the next step
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 34 66

   * - Value
     - What it holds
   * - ``${userQuery}``
     - The message: what the person typed, or the message on the node.
   * - ``${inputs.<name>}``
     - A named value from **Values the steps can use**, or from the REST body.
   * - ``${trigger.type}``, ``${trigger.fired_at}``
     - How and when this run started.
   * - ``${event.<field>}``
     - For app and file triggers: the first new record, such as
       ``${event.id}`` or ``${event.path}``.
   * - ``events``
     - Every new record. Wire a :doc:`Loop Over Items </agentic-ai-guide/data-steps>`
       after the Trigger to handle them one at a time.

An event Trigger has two outlets. **R** (run) carries the new records on. **N**
(nothing new) is taken when a check finds nothing; leave it unwired and that
check simply ends.

.. figure:: ../_assets/agentic-ai-guide/triggers/outlets.png
   :alt: A Trigger node with its R and N outlets, R wired to a Loop Over Items node
   :width: 520px

.. tip::

   A small **$** on a node means its settings use ``${...}`` values from earlier
   steps. How to pick those values without typing them is on
   :doc:`/agentic-ai-guide/passing-data`.

Next: act in an app
-------------------

A Trigger starts the run; :doc:`/agentic-ai-guide/app-actions` is how the run
reads from and writes to your business apps.
