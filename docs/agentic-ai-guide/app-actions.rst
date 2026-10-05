App Actions: Read and Write Your Business Apps
==============================================

An **App Action** is one fixed operation in a connected app: find open
tickets, append rows to a sheet, or update a database record. You choose the
app, action, connection and mappings. The action runs when the flow reaches
it; a language model does not choose its operation or arguments.

Use an App Action for the steps that must always happen. Give an
:doc:`Agent Node <agent-node>` a tool instead when choosing whether and how
to call it is part of the model's task.

**First time connecting an app?** Follow :doc:`app-setup` first. For a complete
flow, choose one of the :doc:`end-to-end-examples/index`. The
:doc:`app-action-catalogue` lists individual actions when you need a lookup.

.. figure:: ../_assets/agentic-ai-guide/app-actions/lookup-v5.png
   :alt: PostgreSQL App Action details with a customer key mapped from the current loop record
   :width: 680px

   A configured database lookup: choose the connection and table, then map
   the current customer's key. The flow runs this fixed action when it reaches
   the node. See :doc:`database-connectors-setup` to build your first lookup.

.. contents:: On this page
   :local:
   :depth: 1

Choose the right kind of step
-----------------------------

.. list-table::
   :header-rows: 1
   :widths: 34 33 33

   * - You need to…
     - Use
     - Who decides?
   * - Read five rows or save an approved record every time this branch runs
     - **App Action** on the normal flow path
     - Your configuration and the flow's branches.
   * - Summarize text or classify a support request
     - **Agent Node**, initially without tools
     - The model generates an answer from your instructions and inputs.
   * - Let the model look up information when needed
     - A read-only tool available to an **Agent Node**
     - The model chooses a tool call within the permissions you expose.
   * - Allow a write only after a person reviews it
     - **Human Approval**, then an **App Action** on **Approved**
     - The reviewer decides; the fixed step carries out the approved operation.

**Deterministic means configured, not identical forever.** A mapping such as
``${4.fields.customer_id}`` reads the current run's value. A database or API
can return different data on the next run. If a mapped value came from an
Agent Node, validate it before using it in a write. A fixed action does not
make an upstream model's answer factual or safe.

**Start small:** Trigger → one read-only App Action → Output. Add a write
only after the returned fields make sense. You do not need a model connection
for this first flow. Follow :doc:`database-connectors-setup` for the complete
database setup and all eleven available database actions.

The apps
--------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Group
     - Apps
   * - Microsoft 365
     - Outlook Mail, Outlook Calendar, SharePoint, OneDrive, Microsoft Teams
   * - Google Workspace
     - Gmail, Google Calendar, Google Drive, Google Sheets, Google Docs
   * - CRM, chat and tickets
     - Salesforce, Slack, Jira
   * - Databases
     - MySQL, PostgreSQL, SQL Server
   * - Web
     - Web Search, public page/feed reads and HTTP requests

Most apps use a connection you create once under the project's **Connections**
page (:doc:`/agentic-ai-guide/connections`). The databases also accept a generic
JDBC connection to the same database. Web searches use Serper; public page and
feed reads do not require a connection. See :doc:`app-setup` for the exceptions
and the first read to try for each app.

Add an App Action in three steps
--------------------------------

Drop **App Action** onto the canvas. The drawer walks you through **App**,
**Action** and **Details**; the bar at the top shows what you picked, and you
can click any step to go back to it.

**1. Pick the app.** Each card says how many actions the app offers. Type in
**Search apps** to narrow the list.

.. figure:: ../_assets/agentic-ai-guide/app-actions/app-grid.png
   :alt: The top of the current App Action drawer, with Search apps and the first six available apps
   :width: 580px

   Search for your app or scroll for more. The number on a card is its action
   count, not the number of configured connections.

**2. Pick what it should do.** Actions are grouped by what they work on (rows,
spreadsheets, sheets) and each says in one line what it does. **reads** leaves
the app as it was; **changes data** writes to it.

.. figure:: ../_assets/agentic-ai-guide/app-actions/action-list.png
   :alt: Google Sheets actions grouped as Row, Spreadsheet and Sheet, each marked reads or changes data; Append is selected
   :width: 580px

**3. Fill in the details.** The right side holds the connection and the action's
own settings. The left side shows **What arrives here** - the fields of the
records reaching this step - so you can click a field instead of typing it.

Reading from an app
-------------------

A read returns records, and those records become the rows the next step
receives. Fill in what to read—a PostgreSQL table, a trusted ``Where`` filter
if needed, and a small limit—then press **Load the fields from PostgreSQL**.
For predictable database ordering, follow :doc:`database-connectors-setup`;
do not assume that a preview's row order is a guarantee.

.. figure:: ../_assets/agentic-ai-guide/app-actions/read-details.png
   :alt: PostgreSQL Read rows with table sf_training_orders, where status = 'open', order by amount desc, limit 5, and the returned fields id, customer_id, product and amount
   :width: 100%

   After Load the fields, What this step returns shows the real columns and a sample row.

Loading the fields is required before **Save action** is enabled. It is what
tells every later step which fields it will receive, so they can offer them in
their own **What arrives here** panel.

.. tip::

   Not sure what the app holds? Open **Explore <app>** on the left. It lists
   what is there - tables and their rows, folders, mailboxes - through the same
   connection, without leaving the canvas.

   .. figure:: ../_assets/agentic-ai-guide/app-actions/explore.png
      :alt: The Explore PostgreSQL tab listing the rows of the sf_training_orders table
      :width: 100%

**Advanced settings** holds what you rarely change: extra query parameters,
timeouts, and **Nested fields**. ``deep`` (the default) turns a nested value
such as Jira's ``fields.priority.name`` into a column of its own, which is what
a Filter or a prompt can name.

Writing to an app
-----------------

A write sends the records arriving on its input to the app. With **Fields to
set** left empty, every arriving row is written as it is - each column becomes
the field of the same name. That is the right choice after a Filter, a Loop or a
database read whose columns already match.

.. figure:: ../_assets/agentic-ai-guide/app-actions/write-details.png
   :alt: PostgreSQL Insert or update rows by key into sf_learn_triage, key column ticket_id, with no fields set so the arriving rows are written
   :width: 100%

To write one record that you compose yourself, add fields. The chips offer the
fields the app expects (for an email: **To**, **Cc**, **Bcc**, **Subject**,
**Body**); type a value, or click in the box and then click a field on the left
to insert a reference such as ``${10.analysis}``. **What will be sent** shows
the exact request.

.. figure:: ../_assets/agentic-ai-guide/app-actions/fields-to-set.png
   :alt: Outlook Mail Send a message with Fields to set to, subject and body; the body holds ${10.analysis} from the Agent Node that wrote the digest
   :width: 100%

   The body is the answer of the Agent Node that wrote the digest. Lists, long text and nested formats are shaped for the app automatically.

**Edit as JSON (advanced)** shows the same request as raw JSON, for the rare
case the mapper does not cover.

What a write hands on
~~~~~~~~~~~~~~~~~~~~~

Every row comes back with three fields beside it:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Meaning
   * - ``result_status``
     - ``ok``, ``failed`` or ``skipped``.
   * - ``result_id``
     - The id the app gave the new or changed record - a message id, a sheet
       id, a row key. For the first returned record, use
       ``${<node>.fields.result_id}``, replacing ``<node>`` with the actual
       node number. Process the records themselves for multiple results.
   * - ``result_error``
     - Why the app refused the row, when it did.

**If a row is rejected** (under Advanced settings) decides what happens when the
app refuses one row: ``stop`` fails the run at the first rejection, ``continue``
writes the rest and marks the failed rows. Follow it with a
:doc:`Filter </agentic-ai-guide/data-steps>` on ``result_status`` to collect the
failures.

``stop`` does not undo earlier successful writes. A network error can also
leave you unsure whether the destination accepted the request. Inspect the
destination before retrying a create, append, send or upload.

.. figure:: ../_assets/agentic-ai-guide/app-actions/on-error.png
   :alt: The If a row is rejected setting, set to stop
   :width: 664px

Databases
---------

MySQL, PostgreSQL and SQL Server offer the same business actions:
**List rows**, **Get a row by key**, **Count rows**, **Describe a table**,
**Insert a row**, **Update a row by key**, **Insert or update a row**,
**Delete rows**, **List tables**, **List schemas**, and **Run a SQL statement**.

* **Run a SQL statement** can read or change data. The connector examines the
  statement to classify it; a leading ``WITH`` or ``SELECT`` alone does not
  prove that it is read-only. Use a read-only database account for exploration.
* Table and column identifiers are checked. Key-based row actions bind key
  values, and insert/update actions bind record values. **Where** and **SQL**
  are SQL text, not automatic parameter binding: never interpolate a user's
  message or a model-generated fragment into them.
* A database can also start the agent: see
  :doc:`/agentic-ai-guide/triggers`.

For connection types, schemas, keys, each action's inputs, result checks and
safe retry behavior, use :doc:`database-connectors-setup`.

.. raw:: html

   <details class="tutorial-details"><summary>See fixed App Actions in a complete workflow</summary>

.. figure:: ../_assets/agentic-ai-guide/app-actions/workflow-v5.png
   :alt: Actual meeting preparation canvas with a fixed customer lookup inside the Loop, one Agent Node for writing, and Google Docs creation and update after the Loop completes

   **1** The customer lookup is fixed; only the following writing step uses
   a model. **2** The document actions run after the Loop's **D** output, so
   they publish the collected pack, not a document for every meeting.
   This is the saved configuration, not proof of external execution.

.. raw:: html

   </details>

Check a write before enabling it
--------------------------------

#. **Name the destination.** Confirm the mailbox, folder, sheet, object or
   table belongs to your test environment.
#. **Choose the record set.** Inspect **What arrives here**. Two arriving
   records can mean two writes; one summary record can mean one write.
#. **Map only the required fields.** Check **What will be sent**, including
   nested JSON, identifiers, dates and recipients. A request preview is not
   proof that the provider accepts it.
#. **Resolve references.** Check that the referenced node runs before this
   action, and that a one-record reference is not accidentally selecting only
   the first record of a larger result.
#. **Run one controlled test.** Use a draft instead of a send where possible.
   Read the result and verify the destination itself.
#. **Plan the second run.** Inserts, appends, document creation and sends can
   repeat. Prefer a stable-key update/upsert when appropriate, or add an
   explicit check before creating something again.

.. tip::

   A tool attached to an Agent Node is not a substitute for a required write
   step. If saving the reviewed result must happen, connect an App Action on
   the approved flow path. Conversely, do not connect a send before the
   approval that is supposed to protect it.

Limits worth knowing
--------------------

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Where
     - Limit
   * - App Action records carried inline in the run state
     - Up to 500 rows in this build. Larger results use a dataset handle.
       This is not a guarantee of constant memory for every operation.
   * - A preview (Load the fields, Explore)
     - A small sample; it is a preview.
   * - A write while you configure it
     - Nothing is written until the agent runs.

For a large table or bulk processing, use a workflow designed for that
dataset and execution engine. Check which database/JDBC and other nodes
that engine supports. See :doc:`workflows-as-tools` for exposing a tested
workflow to an agent.

Next
----

:doc:`/agentic-ai-guide/passing-data` explains **What arrives here** and the
``${...}`` references in detail.

.. toctree::
   :hidden:

   app-setup
