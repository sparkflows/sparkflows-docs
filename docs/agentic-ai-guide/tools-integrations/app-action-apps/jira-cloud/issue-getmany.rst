:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../jira-cloud.html">Jira</a> › Issue</p>

List issues
===========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Jira</dd></div>
     <div><dt>Resource</dt><dd>Issue</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists issues that match an optional JQL filter (without one, the most recently created first), following Jira's paging up to the limit, with each issue's key, summary, status, assignee, priority and other navigable fields.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/jira-cloud>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Jira**.
#. **Action:** under **Issue**, choose **List issues**.
#. **Details:** choose your Jira connection, click **Test**, then fill in the boxes below.
#. Click **Load the fields from Jira** so later steps can use the columns, then **Save action**.

Fill in the details
-------------------

Type a value, or click a field under **What arrives here** to put a value from an earlier step into the box.

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Search text**
     - No
     - JQL, Jira's search language: project = FIN, status = Open, assignee = currentUser(), created >= -7d. For example ``project = FIN AND status = Open ORDER BY created DESC``.
   * - **Fields to return**
     - No
     - Comma-separated field names. Blank returns the default set. For example ``summary, status, assignee, priority``.
   * - **Limit**
     - No
     - How many rows at most. A run from the canvas previews 20. Default: ``100``.

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Extra query parameters (JSON)**
     - No
     - Sent to the API unchanged, for a filter this form has no field for. For example {"timeMin": "2026-09-01T00:00:00Z"}. For example ``{"expand": "changelog"}``.
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Jira** to see the columns before you save.

A run from the canvas previews 20 rows, whatever **Limit** says.

Start a flow from it
--------------------

A :doc:`Trigger </agentic-ai-guide/triggers-automation/triggers>` can watch Jira with this action and start the flow when something new turns up. Pick **Jira** in the Trigger, then the event.

.. list-table::
   :header-rows: 1
   :widths: 32 68
   :class: tool-table

   * - Event
     - What it reports
   * - **Issue created**
     - Reports each issue created since the last check, in every project the connection can see.
   * - **Issue updated**
     - Reports each issue every time it is updated: a new comment, a changed field or a transition.
   * - **Issue resolved**
     - Reports each issue resolved since the last check, with its resolution.
   * - **Issue status changed**
     - Reports each issue whose status changed since the last check; fields.status holds the new status.
   * - **Issue moved to a status**
     - Filter is the status name as the workflow shows it, for example In Review, without quotes. Reports each issue that moved into that status since the last check.
   * - **Issue created in a project**
     - Filter is the project key, for example FIN. Reports each issue created in that project since the last check.
   * - **Issue created matching JQL**
     - Filter is a JQL condition without ORDER BY, for example project = FIN AND issuetype = Bug. Reports each issue created since the last check that meets it.
   * - **Issue updated matching JQL**
     - Filter is a JQL condition without ORDER BY, for example project = FIN AND priority = Highest. Reports each issue updated since the last check that meets it.
   * - **Issue starts matching JQL**
     - Filter is a JQL condition without ORDER BY, for example status = Blocked or labels = escalation. The first check records the issues that already match; later checks report each issue that newly matches. Best for conditions that fewer than 500 issues meet.
   * - **Issue assigned to me**
     - Reports each issue assigned to the connection's own user since the last check.
   * - **Issue assigned to a person**
     - Filter is the person's Atlassian account id, which a User search returns. Reports each issue assigned to that person since the last check.
   * - **Issue priority changed**
     - Reports each issue whose priority changed since the last check; fields.priority holds the new one.
   * - **Issue became overdue**
     - Reports each unresolved issue once, on the first check after its due date passes. The first check records the issues that are already overdue.

Let an agent decide instead
---------------------------

To let an agent call **List issues** only when a request needs it, add the :doc:`List issues tool </agentic-ai-guide/tools-integrations/connector-tools/jira-cloud/issue-getmany>` to an Agent Node.

Other Issue actions
-------------------

.. raw:: html

   <div class="tool-related"><a href="issue-get.html">Get an issue</a><a href="issue-search.html">Search issues</a><a href="issue-create.html">Create an issue</a><a href="issue-update.html">Update an issue</a><a href="issue-delete.html">Delete an issue</a><a href="issue-transition.html">Change an issue&#x27;s status</a><a href="issue-listtransitions.html">List an issue&#x27;s transitions</a><a href="issue-assign.html">Assign an issue</a><a href="issue-changelog.html">Get an issue&#x27;s history</a></div>
