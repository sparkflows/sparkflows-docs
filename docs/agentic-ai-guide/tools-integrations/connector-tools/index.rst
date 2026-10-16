.. _connector-tools:

.. rst-class:: agentic-tutorial

Connector Tools
===============

.. container:: tutorial-intro

   Connector tools let an agent read from and act in the systems your business runs on. Each connector is one node on the canvas that expands into one named tool per operation you tick. 22 connectors and 418 operations are available today.

.. container:: tutorial-start

   **New to tools?** Read :doc:`/agentic-ai-guide/tools-integrations/tools-connectors` first. For tools that need no outside system, such as reading a CSV or calling a REST API, see :doc:`/agentic-ai-guide/tools-integrations/sparkflows-tools`.

.. figure:: ../../../_assets/agentic-ai-guide/tools/picker-connectors.png
   :alt: The Add a tool picker with the Connectors list
   :width: 100%

   Click **+ Tool** on an Agent Node, or **Add tools** in Agent Studio, to open the picker. Each tile shows the connector's resources and operations, and **connected** when a connection for it already exists.

.. contents:: On this page
   :local:
   :depth: 1
   :class: tool-toc

Choose a connector
------------------

Google Workspace
~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid tool-grid tool-grid-3">
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/gmail.svg" alt=""><h3><a href="gmail.html">Gmail</a></h3></div>
       <p>Search, read and label email, draft or send replies, and save attachments.</p>
       <p class="tutorial-tools">22 tools · 11 read, 11 write<br>Google connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/google_calendar.svg" alt=""><h3><a href="google-calendar.html">Google Calendar</a></h3></div>
       <p>List events, find busy times, and create or update events.</p>
       <p class="tutorial-tools">9 tools · 5 read, 4 write<br>Google connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/google_docs.svg" alt=""><h3><a href="google-docs.html">Google Docs</a></h3></div>
       <p>Read documents as text, create them and edit their content.</p>
       <p class="tutorial-tools">4 tools · 2 read, 2 write<br>Google connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/google_drive.svg" alt=""><h3><a href="google-drive.html">Google Drive</a></h3></div>
       <p>Search, read, upload, organise and share files and folders.</p>
       <p class="tutorial-tools">12 tools · 6 read, 6 write<br>Google connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/google_sheets.svg" alt=""><h3><a href="google-sheets.html">Google Sheets</a></h3></div>
       <p>Read rows, append and update them, and manage tabs.</p>
       <p class="tutorial-tools">9 tools · 3 read, 6 write<br>Google connection</p>
     </article>
   </div>

Microsoft 365
~~~~~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid tool-grid tool-grid-3">
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/outlook_mail.svg" alt=""><h3><a href="outlook-mail.html">Outlook Mail</a></h3></div>
       <p>Search and read email, reply, forward, draft, move and flag.</p>
       <p class="tutorial-tools">18 tools · 8 read, 10 write<br>Microsoft Graph connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/outlook_calendar.svg" alt=""><h3><a href="outlook-calendar.html">Outlook Calendar</a></h3></div>
       <p>Read calendars, check free/busy, and manage meetings.</p>
       <p class="tutorial-tools">12 tools · 6 read, 6 write<br>Microsoft Graph connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/onedrive.svg" alt=""><h3><a href="onedrive.html">OneDrive</a></h3></div>
       <p>Browse a OneDrive, read file text, upload, move and share.</p>
       <p class="tutorial-tools">11 tools · 5 read, 6 write<br>Microsoft Graph connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/sharepoint_online.svg" alt=""><h3><a href="sharepoint-online.html">SharePoint Online</a></h3></div>
       <p>Find sites, read and upload library files, and edit list items.</p>
       <p class="tutorial-tools">25 tools · 15 read, 10 write<br>Microsoft Graph or SharePoint connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/msteams.svg" alt=""><h3><a href="microsoft-teams.html">Microsoft Teams</a></h3></div>
       <p>Read teams, channels, posts and chats, and create meetings.</p>
       <p class="tutorial-tools">17 tools · 12 read, 5 write<br>Microsoft Graph connection</p>
     </article>
   </div>

Messaging and email
~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid tool-grid tool-grid-3">
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/slack.svg" alt=""><h3><a href="slack.html">Slack</a></h3></div>
       <p>Read channels and threads, look people up, and post messages.</p>
       <p class="tutorial-tools">37 tools · 16 read, 21 write<br>Slack connection · Bot Token</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/mail_tools.svg" alt=""><h3><a href="email-imap-smtp.html">Email (IMAP and SMTP)</a></h3></div>
       <div class="tool-chips"><span class="tool-chip is-new">New</span><span class="tool-chip">Agent tool only</span></div>
       <p>Read, search, move and reply to email in any IMAP mailbox.</p>
       <p class="tutorial-tools">12 tools · 5 read, 7 write<br>Email connection · host and password</p>
     </article>
   </div>

CRM and commerce
~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid tool-grid tool-grid-3">
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/salesforce.svg" alt=""><h3><a href="salesforce.html">Salesforce</a></h3></div>
       <p>Look up and change accounts, contacts, leads, opportunities and cases.</p>
       <p class="tutorial-tools">79 tools · 35 read, 44 write<br>Salesforce connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/stripe.svg" alt=""><h3><a href="stripe.html">Stripe</a></h3></div>
       <div class="tool-chips"><span class="tool-chip is-new">New</span><span class="tool-chip">Agent tool only</span></div>
       <p>Look up customers, invoices, subscriptions, charges and the balance.</p>
       <p class="tutorial-tools">14 tools · 11 read, 3 write<br>Stripe connection · Secret Key</p>
     </article>
   </div>

Developer and work tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid tool-grid tool-grid-3">
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/github.svg" alt=""><h3><a href="github.html">GitHub</a></h3></div>
       <div class="tool-chips"><span class="tool-chip is-new">New</span><span class="tool-chip">Agent tool only</span></div>
       <p>Work with issues, pull requests, files, workflows and releases.</p>
       <p class="tutorial-tools">31 tools · 17 read, 14 write<br>GitHub connection · Access Token</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/jira_cloud.svg" alt=""><h3><a href="jira-cloud.html">Jira Cloud</a></h3></div>
       <p>Search issues with JQL, create, update, transition and comment.</p>
       <p class="tutorial-tools">28 tools · 18 read, 10 write<br>Jira connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/notion.svg" alt=""><h3><a href="notion.html">Notion</a></h3></div>
       <div class="tool-chips"><span class="tool-chip is-new">New</span><span class="tool-chip">Agent tool only</span></div>
       <p>Search pages and databases, query rows, add pages and content.</p>
       <p class="tutorial-tools">13 tools · 7 read, 6 write<br>Notion connection · Integration Token</p>
     </article>
   </div>

Databases
~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid tool-grid tool-grid-3">
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/mysql.svg" alt=""><h3><a href="mysql.html">MySQL</a></h3></div>
       <p>Read, filter and count rows, describe tables, and write rows.</p>
       <p class="tutorial-tools">11 tools · 6 read, 5 write<br>MySQL connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/postgresql.svg" alt=""><h3><a href="postgresql.html">PostgreSQL</a></h3></div>
       <p>Read, filter and count rows, describe tables, and write rows.</p>
       <p class="tutorial-tools">11 tools · 6 read, 5 write<br>PostgreSQL connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/sqlserver.svg" alt=""><h3><a href="sql-server.html">SQL Server</a></h3></div>
       <p>Read, filter and count rows, describe tables, and write rows.</p>
       <p class="tutorial-tools">11 tools · 6 read, 5 write<br>SQL Server connection</p>
     </article>
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/database.svg" alt=""><h3><a href="sql-database.html">SQL Database</a></h3></div>
       <div class="tool-chips"><span class="tool-chip is-new">New</span><span class="tool-chip">Agent tool only</span></div>
       <p>Work with any SQL database: read and write rows, run SQL, manage tables.</p>
       <p class="tutorial-tools">18 tools · 8 read, 10 write<br>Database connection</p>
     </article>
   </div>

Web
~~~

.. raw:: html

   <div class="tutorial-grid tool-grid tool-grid-3">
     <article class="tutorial-card tool-card">
       <div class="tool-card-head"><img src="../../../_static/img/tools/web_tools.svg" alt=""><h3><a href="web-search.html">Web Search</a></h3></div>
       <p>Search the web and news, fetch pages, read feeds, call URLs.</p>
       <p class="tutorial-tools">14 tools · 10 read, 4 write<br>Serper connection</p>
     </article>
   </div>

Connections at a glance
-----------------------

Every connector signs in with a saved connection. Create it once under **Administration → Global/Group Connections → Add Connection** and reuse it in every agent. Connections for tools are listed under the **Tools** category.

.. figure:: ../../../_assets/agentic-ai-guide/tools/connections/add-connection-tools.png
   :alt: Add Connection, Select Connector step, with the Tools category: A2A, Confluence, Email (IMAP and SMTP), GitHub, Google, JDBC, Jira, MCP, Microsoft Graph, MySQL, Notion, Pinecone, PostgreSQL / PGVector, SQL Server, Salesforce, Serper Api, ServiceNow, SharePoint, Slack and Stripe
   :width: 100%

   **Add Connection → Tools** lists every connection type a tool can sign in with, including Slack, GitHub, Notion, Stripe and Email (IMAP and SMTP).

.. list-table::
   :header-rows: 1
   :widths: 20 38 42

   * - Connection
     - Used by
     - What it holds
   * - **Google**
     - :doc:`Gmail <gmail>`, :doc:`Google Calendar <google-calendar>`, :doc:`Google Docs <google-docs>`, :doc:`Google Drive <google-drive>`, :doc:`Google Sheets <google-sheets>`
     - Client ID, client secret and refresh token from a Google Cloud OAuth client. The scopes on the refresh token decide which apps it reaches.
   * - **Microsoft Graph**
     - :doc:`Outlook Mail <outlook-mail>`, :doc:`Outlook Calendar <outlook-calendar>`, :doc:`OneDrive <onedrive>`, :doc:`SharePoint Online <sharepoint-online>`, :doc:`Microsoft Teams <microsoft-teams>`
     - Tenant ID, client ID and client secret of an Entra ID app registration, with Graph application permissions granted by an admin.
   * - **SharePoint**
     - :doc:`SharePoint Online <sharepoint-online>`
     - An alternative to Microsoft Graph for SharePoint only.
   * - **Salesforce**
     - :doc:`Salesforce <salesforce>`
     - Your Salesforce org and user.
   * - **Jira**
     - :doc:`Jira Cloud <jira-cloud>`
     - Site URL, account email and API token.
   * - **Slack**
     - :doc:`Slack <slack>`
     - A **Bot Token** (``xoxb-``).
   * - **GitHub**
     - :doc:`GitHub <github>`
     - An **Access Token**: a classic or fine-grained personal access token.
   * - **Notion**
     - :doc:`Notion <notion>`
     - An **Integration Token**: an internal integration secret.
   * - **Stripe**
     - :doc:`Stripe <stripe>`
     - A **Secret Key** (``sk_``) or a restricted key (``rk_``).
   * - **Email (IMAP and SMTP)**
     - :doc:`Email (IMAP and SMTP) <email-imap-smtp>`
     - IMAP host, email address and password, plus an optional SMTP host.
   * - **Database (JDBC)**
     - :doc:`MySQL <mysql>`, :doc:`PostgreSQL <postgresql>`, :doc:`SQL Server <sql-server>`
     - JDBC URL, user and password.
   * - **Serper**
     - :doc:`Web Search <web-search>`
     - A Serper API key, used by the search tools only.

Slack, GitHub, Notion and Stripe connections hold one token and nothing else: each of these connectors calls its own fixed API host, so there is no URL or username to enter. **Test Connection** checks the token against that service before you save.

.. note::

   The other 17 connectors are also available as an :doc:`App Action </agentic-ai-guide/tools-integrations/app-actions>`: the same operations as a fixed workflow step that always runs exactly as set. GitHub, Notion, Stripe and Email (IMAP and SMTP) are offered as agent tools only; their App Action nodes are still marked **Coming soon**. Connectors that are not listed on this page are not available yet.

How a connector becomes tools
-----------------------------

#. **Connect.** Pick a connection and click **Test connection**. Nothing below unlocks until it passes, so a wrong token is caught before you tick anything.
#. **Choose the shape.** *A separate tool for each one* (recommended) hands the agent one named tool per operation. *One tool for everything* hands it a single tool that takes the resource and operation as arguments.
#. **Tick operations.** Reads sit left of the divider and writes right of it. Start from the **Look things up** pack and add only what the agent needs.
#. **Add to agent.** Everything you ticked arrives as one node on the canvas.

.. figure:: ../../../_assets/agentic-ai-guide/tools/connect-step.png
   :alt: Step 1 of a connector: Choose a connection, Test connection and Manage connections
   :width: 100%

   Step 1 on every connector. If no connection exists yet, **Manage connections** takes you to where it is created.

The full walkthrough, with packs and fixed settings, is in :doc:`/agentic-ai-guide/tools-integrations/tools-connectors`.

.. toctree::
   :hidden:

   Gmail <gmail>
   Google Calendar <google-calendar>
   Google Docs <google-docs>
   Google Drive <google-drive>
   Google Sheets <google-sheets>
   Outlook Mail <outlook-mail>
   Outlook Calendar <outlook-calendar>
   OneDrive <onedrive>
   SharePoint Online <sharepoint-online>
   Microsoft Teams <microsoft-teams>
   Slack <slack>
   Email (IMAP and SMTP) <email-imap-smtp>
   Salesforce <salesforce>
   Stripe <stripe>
   GitHub <github>
   Jira Cloud <jira-cloud>
   Notion <notion>
   MySQL <mysql>
   PostgreSQL <postgresql>
   SQL Server <sql-server>
   SQL Database <sql-database>
   Web Search <web-search>
