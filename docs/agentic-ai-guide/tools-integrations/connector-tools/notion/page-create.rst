:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../notion.html">Notion</a> › Page</p>

Create a page
=============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/notion.svg" alt="Notion logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Notion</dd></div>
     <div><dt>Resource</dt><dd>Page</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>notion_page_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a page as a row of a database or under another page, with its property values and optional content blocks, and returns it with its id and URL. Database get shows the property names and types a database row takes.

Before you start
----------------

* A Notion connection. See :doc:`how to set one up <../notion>`.
* The account behind the connection must be allowed to change this data in Notion.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Notion** under **Connectors** and connect your Notion connection.
#. Tick **create** in the **Page** row, then click **Add to agent**.

The agent now sees ``notion_page_create`` and calls it when a request needs it.

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
   * - ``properties``
     - JSON object
     - Yes
     - The page's property values in Notion's JSON, keyed by property name in a database, or only title under a page. Example: {"Name": {"title": [{"text": {"content": "Q3 review"}}]}, "Status": {"select": {"name": "Open"}}, "Due": {"date": {"start": "2026-10-15"}}}.
   * - ``databaseId``
     - text
     - No
     - The database the page becomes a row of; give this or parentPageId, not both. Example: d9824bdc-8445-4327-be8b-5b47500af6ce.
   * - ``parentPageId``
     - text
     - No
     - The page it goes under as a sub-page, whose properties may then hold only title; give this or databaseId, not both. Example: 59833787-2cf9-4fdf-8782-e53db20768a5.
   * - ``children``
     - list of JSON object
     - No
     - The page content as up to 100 Notion block objects. Example: [{"object": "block", "type": "paragraph", "paragraph": {"rich\_text": [{"type": "text", "text": {"content": "Agenda to follow."}}]}}].

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Notion.

Other Page tools
----------------

.. raw:: html

   <div class="tool-related"><a href="page-get.html">Get a page</a><a href="page-update.html">Update page properties</a></div>
