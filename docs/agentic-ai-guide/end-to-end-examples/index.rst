.. _agentic-ai-end-to-end-examples:

.. rst-class:: agentic-tutorial

Build End-to-End Agentic AI Flows
==================================

.. container:: tutorial-intro

   Build a useful process, one step at a time. These eight walkthroughs show
   how to connect apps, work with records, add AI where it helps, and keep a
   person in control of important decisions.

.. container:: tutorial-start

   **New to the canvas? Start with the order-file loader.**

   :doc:`Load two order files into a database <order-file-loader>` uses small
   practice files and no language model. Learn the read → loop → write
   pattern, then add AI in a later tutorial.

   Need help first? :doc:`Choose a node <../node-reference>` ·
   :doc:`Connect an app <../app-setup>`

Choose what you want to build
-----------------------------

You can follow one tutorial on its own. Start with a familiar task; there
is no need to work through all eight or connect every app.

Files and reporting
~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid">
     <article class="tutorial-card">
       <p class="tutorial-kicker">Start here · No model required</p>
       <h3><a href="order-file-loader.html">Load order files into a database</a></h3>
       <p>Read two CSVs, process one file at a time and save three unique orders. Repeat the run without adding duplicate rows.</p>
       <p class="tutorial-tools">Files · Loop · PostgreSQL<br>Practice files and exact expected totals included</p>
     </article>
     <article class="tutorial-card">
       <p class="tutorial-kicker">Reporting · Exact calculations</p>
       <h3><a href="revenue-report.html">Publish a weekly revenue report</a></h3>
       <p>Calculate regional totals, publish an Excel report to a test SharePoint folder and prepare a summary email draft.</p>
       <p class="tutorial-tools">Summarize · Excel · SharePoint · Outlook</p>
     </article>
     <article class="tutorial-card">
       <p class="tutorial-kicker">Documents · AI summaries</p>
       <h3><a href="email-attachments.html">Turn attachments into a document log</a></h3>
       <p>Save two test attachments to Drive and add a short, source-based summary of each to a Google Sheet.</p>
       <p class="tutorial-tools">Gmail · Drive · Agent Node · Google Sheets</p>
     </article>
     <article class="tutorial-card">
       <p class="tutorial-kicker">Data enrichment · Explain the result</p>
       <h3><a href="finance-briefing.html">Write a sales and exchange-rate brief</a></h3>
       <p>Fetch a fictional rate fixture, validate its date and direction, then explain the calculated result in a Google Doc.</p>
       <p class="tutorial-tools">HTTP read · Code · Agent Node · Google Docs</p>
     </article>
   </div>

Customer and team operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid">
     <article class="tutorial-card">
       <p class="tutorial-kicker">Classification · Structured output</p>
       <h3><a href="ticket-triage.html">Triage tickets and draft a team digest</a></h3>
       <p>Keep open tickets, classify each one and save the result before writing a digest from the actual counts.</p>
       <p class="tutorial-tools">Filter · Agent Node · PostgreSQL · Outlook</p>
     </article>
     <article class="tutorial-card">
       <p class="tutorial-kicker">Two data sources · Avoid repeats</p>
       <h3><a href="lead-onboarding.html">Prepare welcome drafts for new leads</a></h3>
       <p>Compare incoming leads with the CRM, skip existing addresses and record which new leads were processed.</p>
       <p class="tutorial-tools">Merge · MySQL · Outlook drafts · Google Sheets</p>
     </article>
     <article class="tutorial-card">
       <p class="tutorial-kicker">Preparation · One brief per meeting</p>
       <h3><a href="meeting-preparation.html">Prepare customer meeting briefs</a></h3>
       <p>Match each test meeting to a customer, write a brief and collect the separate briefs in one document.</p>
       <p class="tutorial-tools">Outlook Calendar · Database lookup · Google Docs</p>
     </article>
     <article class="tutorial-card">
       <p class="tutorial-kicker">Rules · Pause for a person</p>
       <h3><a href="refund-approval.html">Review a refund request</a></h3>
       <p>Extract a fictional request, apply a threshold and record approval only after the correct branch completes. No payment is issued.</p>
       <p class="tutorial-tools">Condition · Human Approval · Database log</p>
     </article>
   </div>

Keep a running log without duplicates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <div class="tutorial-grid">
     <article class="tutorial-card">
       <p class="tutorial-kicker">Google · Skip what you have seen</p>
       <h3><a href="spreadsheet-dedup-google.html">Save Excel attachments to Drive, without duplicates</a></h3>
       <p>Read Excel attachments, save each new file to Drive and append one row per file. A second email never logs the same attachment twice.</p>
       <p class="tutorial-tools">Gmail · Merge dedup · Google Drive · Google Sheets</p>
     </article>
     <article class="tutorial-card">
       <p class="tutorial-kicker">Microsoft · Skip what you have seen</p>
       <h3><a href="spreadsheet-dedup-microsoft.html">Save Excel attachments to OneDrive, without duplicates</a></h3>
       <p>The same duplicate-safe flow with Outlook, OneDrive and a SharePoint list. Only genuinely new files are uploaded and recorded.</p>
       <p class="tutorial-tools">Outlook · Merge dedup · OneDrive · SharePoint</p>
     </article>
   </div>

Before your first run
---------------------

#. **Use a training project.** Keep practice files, mailboxes, folders and
   database tables separate from production.
#. **Connect only what the tutorial needs.** Check one small read before
   adding writes. A saved connection does not prove access to every target.
#. **Start manually with two records.** Inspect each step and compare its
   output with the checkpoint before continuing.
#. **Try the same input twice.** Check the tutorial's rerun notes before
   enabling a schedule or event trigger.

.. note::

   These are instructions for building your own flows, not pre-installed
   agents. Screenshots show configuration; they are not proof that an
   external write succeeded in your environment. Never use a real recipient
   or invite attendees during the introductory tests.

.. toctree::
   :hidden:

   order-file-loader
   revenue-report
   email-attachments
   spreadsheet-dedup-google
   spreadsheet-dedup-microsoft
   finance-briefing
   ticket-triage
   lead-onboarding
   meeting-preparation
   refund-approval
