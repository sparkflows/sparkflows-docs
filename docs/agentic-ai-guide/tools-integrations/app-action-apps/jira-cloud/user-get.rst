:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">App Action Apps</a> › <a href="../jira-cloud.html">Jira</a> › User</p>

Get a user
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira logo">
     <dl class="tool-facts">
     <div><dt>App</dt><dd>Jira</dd></div>
     <div><dt>Resource</dt><dd>User</dd></div>
     <div><dt>Type</dt><dd>Reads</dd></div>
     <div><dt>Passes on</dt><dd>The records it reads, as rows</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Fetches one user by Atlassian account id and returns the display name, email address (when the user's privacy settings show it), active flag and time zone.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up </agentic-ai-guide/tools-integrations/connector-tools/jira-cloud>`.

Add this step
-------------

#. Drag **App Action** from **Commonly used** onto the canvas and connect it where the step belongs.
#. **App:** choose **Jira**.
#. **Action:** under **User**, choose **Get a user**.
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

Under **Advanced settings**:

.. list-table::
   :header-rows: 1
   :widths: 26 12 62
   :class: tool-params

   * - Box
     - Required
     - What to enter
   * - **Nested fields**
     - No
     - deep spreads nested objects all the way into dotted columns, for example fields.priority.name. oneLevel stops after one level (fields.priority holds JSON). json keeps each object as one JSON text column. Choices: ``deep``, ``oneLevel``, ``json``. Default: ``deep``.

What it passes on
-----------------

The records come out as rows, one per record. Click **Load the fields from Jira** to see the columns before you save.

Let an agent decide instead
---------------------------

To let an agent call **Get a user** only when a request needs it, add the :doc:`Get a user tool </agentic-ai-guide/tools-integrations/connector-tools/jira-cloud/user-get>` to an Agent Node.

Other User actions
------------------

.. raw:: html

   <div class="tool-related"><a href="user-getmany.html">List users</a><a href="user-search.html">Find users</a></div>
